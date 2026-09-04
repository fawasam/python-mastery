"""
Advanced Web Automation: Fetching Data via HTTP API with Custom Headers.
"""

from typing import Any
import httpx


def fetch_github_repo_info(repo_name: str) -> dict[str, Any]:
    """Fetch public repository metadata from GitHub REST API with fallback error handling."""
    url = f"https://api.github.com/repos/{repo_name}"
    headers = {"User-Agent": "Python-Automation-Script"}
    
    try:
        with httpx.Client(timeout=5.0) as client:
            resp = client.get(url, headers=headers)
            if resp.status_code == 200:
                data = resp.json()
                return {
                    "name": data.get("full_name"),
                    "stars": data.get("stargazers_count"),
                    "language": data.get("language")
                }
            return {"error": f"HTTP {resp.status_code}"}
    except (httpx.ConnectError, httpx.RequestError) as err:
        return {"offline_mode": True, "repo": repo_name, "message": f"Network unavailable: {err}"}


if __name__ == "__main__":
    # Test with python/cpython repo metadata
    info = fetch_github_repo_info("python/cpython")
    print("Fetched GitHub Metadata:", info)
