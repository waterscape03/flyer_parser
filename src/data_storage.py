"""
This module handles saving brochures to JSON.
"""

import json
from typing import List
from src.brochure import Brochure


class DataStorage:
    """
    Handles saving brochures to JSON.

    :param brochures: A list of Brochure objects.
    """

    @staticmethod
    def save_to_json(
        brochures: List[Brochure], filename: str = "brochures.json"
    ) -> None:
        """
        Saves brochures to a JSON file.

        :param brochures: A list of Brochure objects.
        :param filename: The name of the output file.

        :return: None
        """
        with open(filename, "w", encoding="utf-8") as f:
            json.dump([b.to_dict() for b in brochures], f, ensure_ascii=False, indent=4)
        print(f"Saved {len(brochures)} brochures to {filename}")
