"""
PixivDownloader.py
Author: Jack Lee
Date: 2023-06-25
This module defines a class that handles downloading a series of images from the Pixiv website.
"""

import os
import requests
from tqdm import tqdm
from .pixiv_page import PixivPage
from .image_downloader import ImageDownloader


class PixivDownloader:
    """
    The PixivDownloader class handles the download of images from the Pixiv website.
    """

    def __init__(self, base_url='https://www.pixiv.net/ranking.php/'):
        """
        Constructor for the PixivDownloader class.

        Parameters:
        base_url (str): The URL of the webpage where the images are listed.
        """
        self.base_url = base_url

    def download_pixiv_images(self):
        """
        Downloads images listed on the Pixiv webpage.

        Returns:
        None
        """

        # Attempt to get the webpage at the specified URL.
        web_page = requests.get(self.base_url)

        if web_page.status_code == 200:  # If the webpage was retrieved successfully...

            print("Connect url", self.base_url)

            # Create a PixivPage object based on the webpage's text.
            pixiv_page = PixivPage(web_page.text)

            # Extract the date from the webpage.
            date = pixiv_page.get_date()

            # Create a directory for the date if it doesn't already exist.
            os.makedirs("./data/"+date, exist_ok=True)

            # Get the names of the images and their URLs.
            names = pixiv_page.get_image_names()
            urls = pixiv_page.get_image_urls()

            # Initialize a progress bar.
            progress = tqdm(total=50)

            # For each URL...
            for count, url in enumerate(urls):
                # Update the progress bar.
                progress.update(1)

                # Download the image.
                ImageDownloader.download_image(url, count, names, './data/'+date)

        else:  # If the webpage could not be retrieved...

            # Print an error message.
            print("Cannot connect url", self.base_url)
