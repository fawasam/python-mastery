"""
Web Scraper Engine.
"""

from html.parser import HTMLParser


class AnchorParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.links: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag == "a":
            for k, v in attrs:
                if k == "href" and v:
                    self.links.append(v)


def parse_links_from_html_string(html: str) -> list[str]:
    parser = AnchorParser()
    parser.feed(html)
    return parser.links
