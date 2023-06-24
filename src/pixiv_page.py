"""
PixivPage.py
Author: Jack Lee
Date: 2023-06-25
This module defines a class that extracts specific information from the HTML of a Pixiv webpage.
"""

import re


class PixivPage:
    """
    The PixivPage class extracts specific information from the HTML of a Pixiv webpage.
    """

    def __init__(self, page_text):
        """
        Constructor for the PixivPage class.

        Parameters:
        page_text (str): The HTML text of the webpage.
        """
        self.page_text = page_text

    def get_date(self):
        """
        Extracts the date from the webpage's HTML.

        Returns:
        str: The extracted date.
        """
        date = re.findall(r'\[\w+\.\w+\.\w+\]', self.page_text)[0]
        return date.strip('[').strip(']')

    def get_image_names(self):
        """
        Extracts the names of images from the webpage's HTML.

        Returns:
        list: A list of extracted image names.
        """
        names = re.findall(r'"noopener">.*?>', self.page_text)[1:51]

        for i in range(len(names)):
            names[i] = names[i].strip('"noopener">').strip('</a>')
            names[i] = names[i].replace('/', '.').replace('\\', '.').replace('*', '.').replace(
                ':', '.').replace('?', '.').replace('"', '.').replace('<', '.').replace('>', '.').replace('|', '.')

        return names

    def get_image_urls(self):
        """
        Extracts the URLs of images from the webpage's HTML.

        Returns:
        list: A list of extracted image URLs.
        """
        return re.findall(r'/artworks/\d*', self.page_text)[::2]
