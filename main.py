"""
main.py
Author: Jack Lee
Date: 2023-06-25
This script uses the PixivDownloader class to download images from the Pixiv website.
"""

# Import the PixivDownloader class from the src module.
from src.pixiv_downloader import PixivDownloader

# This script only executes if it is the main entry point, not if it has been imported by another script.
if __name__ == '__main__':

    # Create a PixivDownloader object.
    downloader = PixivDownloader()

    # Use the PixivDownloader object to download images.
    downloader.download_pixiv_images()
