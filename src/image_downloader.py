"""
ImageDownloader.py
Author: Jack Lee
Date: 2023-06-25
This module defines a class that is responsible for downloading images from the Pixiv website.
"""

import requests
import time
import re


class ImageDownloader:
    """
    The ImageDownloader class handles the downloading of images.
    It is a static class and does not need to be instantiated.
    """

    @staticmethod
    def download_image(url, count, name, picpath):
        """
        Downloads an image from a specific URL and saves it to a specific path.

        Parameters:
        url (str): URL of the image to download.
        count (int): The count of the current image. Used for naming the saved image file.
        name (str): The name of the image.
        picpath (str): The directory path where the image will be saved.

        Returns:
        None
        """

        # Attempt to get the webpage at the specified URL.
        r = requests.get("http://www.pixiv.net"+url)

        # Attempt to find the URL of the original image in the webpage's text.
        u = re.findall(r'https://i.pximg.net/img-original/img.*?g', r.text)

        if r.status_code == 200:  # If the webpage was retrieved successfully...
            try:
                # Create the full path for the new image file.
                filename = picpath+"/" + "#" + \
                    str(count+1)+" "+str(name[count]) + ".jpg"

                # Define headers for the upcoming GET request.
                headers = {
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',
                    'referer': 'http://www.pixiv.net%s' % str(url)
                }

                # Attempt to get the image at the URL.
                r = requests.get(u[0], headers=headers)

                # If successful, write the image to a file at the specified path.
                with open(filename, 'wb') as f:
                    f.write(r.content)

                # Sleep for a bit to prevent overloading the server with requests.
                time.sleep(0.2)
            except:
                # If anything went wrong with the above, print an error message.
                print('download image failure', str(
                    count+1)+" "+str(name[count]))
        else:  # If the webpage could not be retrieved...
            # Print an error message.
            print("Cannot connect url", "http://www.pixiv.net"+url)
