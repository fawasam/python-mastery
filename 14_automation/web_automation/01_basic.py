"""
Web Automation Basics: Parsing HTML using html.parser standard library.
"""

from html.parser import HTMLParser


class LinkExtractor(HTMLParser):
    """Simple HTML parser extracting hyper-links (href attributes) from HTML documents."""
    def __init__(self) -> None:
        super().__init__()
        self.links: list[tuple[str, str]] = []
        self._current_href: str | None = None

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag == "a":
            for attr, val in attrs:
                if attr == "href" and val:
                    self._current_href = val

    def handle_data(self, data: str) -> None:
        if self._current_href:
            self.links.append((self._current_href, data.strip()))
            self._current_href = None


def extract_links_from_html(html_content: str) -> list[tuple[str, str]]:
    parser = LinkExtractor()
    parser.feed(html_content)
    return parser.links


if __name__ == "__main__":
    sample_html = """
    <html>
        <body>
            <h1>Python Resources</h1>
            <a href="https://docs.python.org">Python Docs</a>
            <a href="https://pypi.org">PyPI Packages</a>
        </body>
    </html>
    """
    links = extract_links_from_html(sample_html)
    print("Extracted Links:", links)
