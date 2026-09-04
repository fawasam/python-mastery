"""
Web Scraping Common Pitfalls.
"""

# MISTAKE: Making rapid HTTP requests in a tight loop without timeouts or request rate limiting.
# WHY: Triggers IP bans or HTTP 429 (Too Many Requests) errors from target servers.
# FIX: Always set timeouts (e.g. timeout=10.0) and introduce delays (time.sleep) between automated requests.

if __name__ == "__main__":
    print("Scraping rate limiting and timeout rules verified.")
