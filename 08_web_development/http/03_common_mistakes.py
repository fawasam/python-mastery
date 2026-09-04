"""
Common Mistakes in HTTP Protocol Understanding.
"""


# MISTAKE: Assuming GET requests can send body payloads reliably across all HTTP proxies
def mistake_get_body() -> None:
    # DANGER: Standard HTTP specification discourages sending request bodies in GET requests!
    # Many proxy servers strip body content from GET requests. Use POST or PUT for payloads.
    pass


if __name__ == "__main__":
    print("Always use appropriate HTTP methods: GET for reads, POST for creation, PUT/PATCH for updates, DELETE for removal.")
