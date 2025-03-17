"""
This module contains the Brochure class for representing a brochure.
"""
from dataclasses import dataclass
from datetime import datetime

@dataclass
class Brochure:
    """Represents a brochure with its attributes.

    :param title: The title of the brochure.
    :param thumbnail: The URL of the brochure thumbnail.
    :param shop_name: The name of the shop.
    :param valid_from: The valid from date of the brochure.
    :param valid_to: The valid to date of the brochure.
    """

    def __init__(
        self, title: str, thumbnail: str, shop_name: str, valid_from: str, valid_to: str
    ):
        self.title = title
        self.thumbnail = thumbnail
        self.shop_name = shop_name
        self.valid_from = valid_from
        self.valid_to = valid_to
        self.parsed_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def to_dict(self) -> dict:
        """
        Converts the object to a dictionary.

        Returns:
            dict: The object as a dictionary.
        """
        return {
            "title": self.title,
            "thumbnail": self.thumbnail,
            "shop_name": self.shop_name,
            "valid_from": self.valid_from,
            "valid_to": self.valid_to,
            "parsed_time": self.parsed_time,
        }
