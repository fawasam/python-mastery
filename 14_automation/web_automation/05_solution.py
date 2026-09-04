"""
Solutions: Web Automation Exercises.
"""

from html.parser import HTMLParser


class HeadingExtractor(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.headings: list[str] = []
        self._in_h1 = False

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag == "h1":
            self._in_h1 = True

    def handle_endtag(self, tag: str) -> None:
        if tag == "h1":
            self._in_h1 = False

    def handle_data(self, data: str) -> None:
        if self._in_h1 and data.strip():
            self.headings.append(data.strip())


def extract_headings_from_html(html_str: str) -> list[str]:
    parser = HeadingExtractor()
    parser.feed(html_str)
    return parser.headings


if __name__ == "__main__":
    html = "<html><body><h1>Welcome Title</h1><h1>Second Title</h1></body></html>"
    print("Extracted H1 Headings:", extract_headings_from_html(html))
