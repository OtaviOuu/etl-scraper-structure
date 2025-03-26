from selectolax.parser import HTMLParser
import requests
from typing import Dict, Union


class HtmlCollector:

    @classmethod
    def collect_essentials(cls, html: str) -> list[Dict[str, str]]:
        tree = HTMLParser(html)

        artist_name_list = tree.css_first(".BodyText")
        artist_name_list_items = artist_name_list.css("a")

        essential_information = []
        for artist_name_list_item in artist_name_list_items:
            names = artist_name_list_item.text(deep=True)
            links = "https://web.archive.org" + artist_name_list_item.attributes.get(
                "href"
            )

            essential_information.append({"name": names, "link": links})

        return essential_information
