from requests import Response, Session
from scripts.errors import RequestError
from scripts.model import ExternalPhoto


class RequestSession:
    """
    Allows to make request
    """

    def __init__(self):
        self._session = Session()

    def request(self, method: str, url: str) -> Response:
        """
        Requests to given url with appropriate method
        :param method: HTTP Method #TODO this could be Enum with HTTP methods
        :param url:
        :return:
        """
        return self._session.request(method, url)


class Client:
    """
    Client to initiate session and create send method based on url and method
    Base for Clint Factory design
    """
    session_ = RequestSession()

    def send(self, method: str, url: str) -> Response:
        """
        Requests to given url with appropriate method
        :param method: HTTP Method
        :param url:
        :return:
        """
        response = self.session_.request(method, url)
        if response.status_code < 200 or response.status_code >= 300:
            self.handle_errors(response)
        return response

    def handle_errors(self, response: Response) -> Exception:
        """
        Handles response errors # TODO analyze more errors
        :param response: from send method
        """
        raise RequestError


class PhotoClient(Client):
    """
    Client dedicated to get Photo data
    """

    def get(self, url: str):
        """
        Simple get with Pydantic validation (validation shouldn't be here)
        :param url: from send method
        """
        response = self.send(method='GET', url=url)
        for r in response.json():
            validate = ExternalPhoto(**r)
        return response.json()


if __name__ == '__main__':
    URL = 'https://jsonplaceholder.typicode.com/photos'
    client = PhotoClient()
    # Printing data to terminal just for example purpose
    print(client.get(URL))
