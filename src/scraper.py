"""
This module contains the Scraper class for parsing brochures from the Prospektmaschine website.
"""

import re
import logging
from datetime import datetime
from typing import List

import requests
from bs4 import BeautifulSoup

from src.brochure import Brochure

logging.basicConfig(
    level=logging.ERROR, format="%(asctime)s - %(levelname)s - %(message)s"
)


class Scraper:
    """
    Scraper for parsing brochures from the Prospektmaschine website.

    :param session: A requests session object.
    :param BASE_URL: The base URL of the website.
    """

    BASE_URL = "https://www.prospektmaschine.de/hypermarkte/"

    def __init__(self):
        self.session = requests.Session()

    def fetch_page(self) -> str:
        """
        Fetches the HTML page and returns its content as text.

        :return: The HTML content of the page.
        """
        try:
            response = self.session.get(self.BASE_URL, timeout=10)
            response.raise_for_status()
            return response.text
        except requests.RequestException as e:
            logging.error("Error fetching page: %s", e)
            return ""

    def parse_brochures(self, html: str) -> List[Brochure]:
        """
        Extracts brochures from the HTML page.

        :param html: The HTML content of the page.

        :return: A list of Brochure objects.
        """
        soup = BeautifulSoup(html, "html.parser")
        brochures = []

        for brochure_element in soup.find_all("div", class_="brochure-thumb"):
            title = self.extract_title(brochure_element)
            thumbnail = self.extract_thumbnail(brochure_element)
            shop_name = self.extract_shop_name(brochure_element)
            valid_from, valid_to = self.extract_validity_dates(brochure_element)

            if title and thumbnail and shop_name and valid_from:
                brochures.append(
                    Brochure(title, thumbnail, shop_name, valid_from, valid_to)
                )

        return brochures

    def extract_title(self, brochure_element) -> str:
        """
        Extracts the title of the brochure.

        :param brochure_element: The HTML element of the brochure.

        :return: The title of the brochure.
        """
        title_tag = brochure_element.find("p", class_="grid-item-content")
        return title_tag.text.strip() if title_tag else ""

    def extract_thumbnail(self, brochure_element) -> str:
        """
        Extracts the URL of the brochure thumbnail.

        :param brochure_element: The HTML element of the brochure.

        :return: The URL of the brochure thumbnail.
        """
        img_tag = brochure_element.find("img")
        return (img_tag.get("src") or img_tag.get("data-src") or "") if img_tag else ""

    def extract_shop_name(self, brochure_element) -> str:
        """
        Extracts the shop name.

        :param brochure_element: The HTML element of the brochure.

        :return: The name of the shop.
        """
        logo_tag = brochure_element.find("div", class_="grid-logo")
        if logo_tag and logo_tag.find("img"):
            return logo_tag.find("img").get("alt", "").replace("Logo ", "")
        return ""

    def extract_validity_dates(self, brochure_element) -> tuple:
        """
        Extracts the validity dates of the brochure.

        :param brochure_element: The HTML element of the brochure.

        :return: A tuple containing the valid from and valid to dates.
        """
        date_tag = brochure_element.find("small", class_="hidden-sm")
        if not date_tag:
            return "", ""

        date_text = date_tag.text.strip()
        date_range = date_text.split("-") if "-" in date_text else [date_text, ""]

        current_date = datetime.now().date()

        date_match = re.search(r"(\d{2}\.\d{2}\.\d{4})", date_range[0])
        if date_match:
            first_date_str = date_match.group(1)
            first_date = datetime.strptime(first_date_str, "%d.%m.%Y").date()

            if len(date_range) > 1 and re.search(
                r"(\d{2}\.\d{2}\.\d{4})", date_range[1]
            ):
                end_date_match = re.search(r"(\d{2}\.\d{2}\.\d{4})", date_range[1])
                valid_to = datetime.strptime(
                    end_date_match.group(1), "%d.%m.%Y"
                ).strftime("%Y-%m-%d")
                valid_from = first_date.strftime("%Y-%m-%d")
            else:
                valid_from = (
                    first_date.strftime("%Y-%m-%d")
                    if first_date <= current_date
                    else ""
                )
                valid_to = None if valid_from else first_date.strftime("%Y-%m-%d")
        else:
            valid_from, valid_to = "", ""

        return valid_from, valid_to
