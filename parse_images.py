import json
import os

import requests


class static_images_updater:
    def __init__(self, dir_repo="genshin-db", path=None) -> None:

        """Download images from wiki, the urls are stored on genshin-db repo locally

        Args:
            dir_repo (str): The default is 'genshin-db', but if the repo gets another name just
            change it to whatever it is
        """

        self.directory_repo = dir_repo
        self.path = os.path.dirname(__file__) if path is None else path
        self.file_dir = self.images_path_dir(self.directory_repo)
        images_urls = self.handle_images_urls(self.file_dir)
        self.download_images(images_urls)
        print("All done")

    @staticmethod
    def images_path_dir(directory) -> str:
        """Return characters json with all urls

        Args:
            directory ([type]): [description]

        Returns:
            str: [description]
        """
        return os.path.join(directory, f"src/data/image/characters.json")

    def handle_images_urls(self, file_dir: str) -> dict:
        """Get JSON file and parse for images urls, returning a dictionary with names and urls

        Args:
            file_dir (str): "genshin-db/src/data/image/characters.json"

        Returns:
            dict: "albedo":"https://..."
        """
        urls = {}
        with open(file_dir, "r") as json_file:
            json_dictionary = json.load(json_file)
            for key, value in json_dictionary.items():
                _ = key.split(".")
                try:
                    urls[_[0]] = json_dictionary[key]["icon"]
                except KeyError:
                    pass
        return urls

    def download_images(self, urls: dict) -> None:
        """Download images from dict which "key:CharacterName" and "Value:Url",
        it will overwrite previous images stored in the folder

        Args:
            urls (dict): "albedo":"https://..."
        """

        self.make_directory()
        path = os.path.dirname(__file__)
        print(path)
        for key, value in urls.items():
            response = requests.get(value)
            with open(f"{path}/static/{key}.png", "wb") as image_data:
                image_data.write(response.content)

    @staticmethod
    def make_directory() -> None:
        """Create folder "static" to store images if it doesn't exists"""
        try:
            os.mkdir("static")
        except FileExistsError:
            pass


static_images_updater()
