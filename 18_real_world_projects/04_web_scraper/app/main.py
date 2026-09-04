"""
Web Scraper Main Entrypoint.
"""

from app.scraper import parse_links_from_html_string


def main() -> None:
    sample_page = "<html><body><a href='/news/1'>News 1</a><a href='/about'>About</a></body></html>"
    links = parse_links_from_html_string(sample_page)
    print("Scraped Links:", links)


if __name__ == "__main__":
    main()
