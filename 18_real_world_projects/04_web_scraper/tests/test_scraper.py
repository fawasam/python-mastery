"""
Tests for Web Scraper.
"""

from app.scraper import parse_links_from_html_string


def test_parse_links() -> None:
    html = "<a href='https://python.org'>Python</a>"
    links = parse_links_from_html_string(html)
    assert links == ["https://python.org"]
