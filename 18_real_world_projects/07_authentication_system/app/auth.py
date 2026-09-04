"""
Auth Engine and Token Generation.
"""

import base64
from datetime import datetime, timedelta, timezone
import hashlib
import hmac
import json

SECRET_KEY = "super_secret_jwt_key_change_in_production"


def create_token(user_id: str, role: str, expires_in_seconds: int = 3600) -> str:
    """Construct signed HMAC token."""
    header = {"alg": "HS256", "typ": "JWT"}
    now = int(datetime.now(timezone.utc).timestamp())
    payload = {"sub": user_id, "role": role, "iat": now, "exp": now + expires_in_seconds}

    b64_header = base64.urlsafe_b64encode(json.dumps(header).encode()).decode().rstrip("=")
    b64_payload = base64.urlsafe_b64encode(json.dumps(payload).encode()).decode().rstrip("=")
    
    signature = hmac.new(SECRET_KEY.encode(), f"{b64_header}.{b64_payload}".encode(), hashlib.sha256).hexdigest()
    return f"{b64_header}.{b64_payload}.{signature}"


def verify_token(token: str) -> dict[str, Any] | None:
    """Verify HMAC token signature and expiration."""
    try:
        parts = token.split(".")
        if len(parts) != 3:
            return None
        b64_header, b64_payload, signature = parts
        
        expected = hmac.new(SECRET_KEY.encode(), f"{b64_header}.{b64_payload}".encode(), hashlib.sha256).hexdigest()
        if not hmac.compare_digest(expected, signature):
            return None
            
        padded_b64 = b64_payload + "=" * (-len(b64_payload) % 4)
        payload = json.loads(base64.urlsafe_b64decode(padded_b64).decode())
        
        now = int(datetime.now(timezone.utc).timestamp())
        if payload.get("exp", 0) < now:
            return None
            
        return payload
    except Exception:
        return None
