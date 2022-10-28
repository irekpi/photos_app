import json
from scripts.model import ExternalPhoto
from typing import List


class FilePhotoClient:
    """
    Class created for json files handling
    Pydantic is used to validate external data
    """

    def parse(self, data: bytes) -> List[dict]:
        """
        Method used for data parse and validation
        :param data: data provided from either REST or file
        :return:
        """
        json_data = json.loads(data)
        for item in json_data:
            validate = ExternalPhoto(**item)
        return json_data

    def get_local(self, path: str) -> List[dict]:
        """
        Method used to get data from file
        :param path: Filepath
        :return:
        """
        with open(path, 'rb') as f:
            data = self.parse(f.read())
        return data


if __name__ == '__main__':
    URL = 'https://jsonplaceholder.typicode.com/photos'
    client = FilePhotoClient()
    data = client.get_local('scripts/sample/data.json')
    # Printing data to terminal just for example purpose
    print(data)
