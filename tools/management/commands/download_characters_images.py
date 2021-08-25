import json
import os
import sys
import subprocess
import requests
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Download images from links stored on 'genshin-db' repo"

    def add_arguments(self, parser):
        parser.add_argument("folder_repo", nargs="?", default="genshin-db", type=str)
        parser.add_argument("path", nargs="?", default=None, type=str)

    def handle(self, *args, **options):
        directory_repo = options["folder_repo"]
        path = (
            os.path.dirname(__file__) if options["path"] is None else options["path"]
        )

        path = self.make_static_folder()
        file_dir = self.images_path_dir(directory_repo)
        images_urls = self.handle_images_urls(file_dir, path)
        self.download_images(images_urls, path)
        sys.stdout.write("Finished\n")

    def handle_images_urls(self, file_dir: str, path:str) -> dict:
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

    def download_images(self, urls: dict, path:str) -> None:
        """Download images from dict which "key:CharacterName" and "Value:Url",
        it will overwrite previous images stored in the folder

        Args:
            urls (dict): "albedo":"https://..."
        """
        for key, value in urls.items():
            response = requests.get(value)
            with open(f"{path}/static/images/characters/{key}.png", "wb") as image_data:
                image_data.write(response.content)

    @staticmethod
    def make_static_folder() -> str:
        """Create folder "static" to store images if it doesn't exists

        Returns:
            str: return static folder directory
        """
        caminho = os.path.abspath(os.path.dirname(__file__))
        subprocess.call(f"{caminho}/clone_repo.sh")
        os.makedirs("static", exist_ok=True)
        return os.path.abspath(os.path.dirname(__name__))

    @staticmethod
    def images_path_dir(directory) -> str:
        """Return characters json with all urls

        Args:
            directory (str): 'src/data/image/characters.json'

        Returns:
            str: 'genshin-db/src/data/image/characters.json'
        """
        return os.path.join(directory, f"src/data/image/characters.json")