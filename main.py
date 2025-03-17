"""
This is the main file that runs the scraper and stores the data.
"""
from src.scraper import Scraper
from src.data_storage import DataStorage


def main():
    """
    The main function that runs the scraper and stores the data.
    """
    scraper = Scraper()
    data = DataStorage()
    html = scraper.fetch_page()

    if not html:
        print("Failed to fetch page content.")
        return

    brochures = scraper.parse_brochures(html)

    if not brochures:
        print("No brochures found.")
        return

    data.save_to_json(brochures)


if __name__ == "__main__":
    main()
