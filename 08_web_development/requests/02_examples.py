"""
POST Request with JSON Payload and Custom Headers.
"""

import httpx


def post_user_payload(username: str, role: str) -> dict[str, str] | None:
    headers = {"User-Agent": "PythonMasteryClient/1.0", "Authorization": "Bearer fake_token_123"}
    payload = {"username": username, "role": role}

    with httpx.Client(timeout=5.0) as client:
        try:
            response = client.post("https://httpbin.org/post", json=payload, headers=headers)
            response.raise_for_status()
            res_data = response.json()
            return res_data.get("json", {})
        except httpx.HTTPError as err:
            print(f"POST request failed: {err}")
            return None


if __name__ == "__main__":
    echoed_json = post_user_payload("alice", "developer")
    if echoed_json:
        print(f"Server echoed posted JSON payload: {echoed_json}")
