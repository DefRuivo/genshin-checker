import requests, json, os

class static_images_updater:

    def __init__(self, dir_repo="genshin-db", path=None) -> None:

        """Download images from wiki, the urls are stored on genshin-db repo locally
        
        Args:
            dir_repo (str): The default is 'genshin-db', but if the repo gets another name just 
            change it to whatever it is
        """             
        
        self.dir_repo = dir_repo
        self.path = os.path.dirname(__file__) if path is None else path
            
        self.file_dir = self.images_path_dir(self.dir_repo)
        images_urls = self.images_urls(self.file_dir)
        self.download_image(images_urls)
        print("All done")
        
    
    @staticmethod
    def images_path_dir(directory) -> str:    
        """Return characters json with all urls

        Args:
            directory ([type]): [description]

        Returns:
            str: [description]
        """                  
        return os.path.join(directory, 
                            f"src/data/image/characters.json")
        
    def images_urls(self, file_dir: str) -> dict:
        """[summary]

        Args:
            file_dir (str): [description]

        Returns:
            dict: [description]
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

    def download_image(self, urls: dict) -> None:  
        try:
            os.mkdir("static")
        except FileExistsError:
            pass
        path = os.path.dirname(__file__)
        for key, value in urls.items():
            response = requests.get(value)
            with open(f"{path}/static/{key}.png", "wb") as f:
                f.write(response.content)
                
                                 
static_images_updater()