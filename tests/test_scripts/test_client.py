import unittest
from unittest.mock import patch
from requests import Session, Response
from pydantic.error_wrappers import ValidationError
from scripts.client import RequestSession, Client, PhotoClient
from scripts.errors import RequestError

data_fixture = {
    "albumId": 1,
    "id": 1,
    "title": "accusamus beatae ad facilis cum similique qui sunt",
    "url": "https://via.placeholder.com/600/92c952",
    "thumbnailUrl": "https://via.placeholder.com/150/92c952"
}


class TestRequestSession(unittest.TestCase):
    def setUp(self):
        self.request_session = RequestSession()

    def test_args_self(self):
        assert type(self.request_session._session) == Session
        assert all(item in dir(self.request_session) for item in ['_session', 'request'])

    @patch('scripts.client.RequestSession.request')
    def test_request(self, mock_request):
        self.request_session.request('HTTPS', '/some_url')
        mock_request.assert_called_once()

    def tearDown(self) -> None:
        del self.request_session


class TestClient(unittest.TestCase):
    def setUp(self):
        self.client = Client()

    def test_args_self(self):
        assert type(self.client.session_) == RequestSession
        assert all(item in dir(self.client) for item in ['send', 'handle_errors'])

    @patch('scripts.client.RequestSession.request')
    def test_send_pass(self, mock_request):
        mock_request.return_value.status_code = 200
        self.client.send('POST', 'http/some_url')
        mock_request.assert_called_once()

    @patch('scripts.client.RequestSession.request')
    def test_send_fail(self, mock_request):
        mock_request.return_value.status_code = 100
        with self.assertRaises(RequestError):
            self.client.send('POST', 'http/some_url')
        mock_request.assert_called_once()

    def test_handle_errors(self):
        with self.assertRaises(RequestError):
            self.client.handle_errors(Response())

    def tearDown(self) -> None:
        del self.client


class TestPhotoClient(unittest.TestCase):
    def setUp(self):
        self.photo_client = PhotoClient()

    def test_inherit(self):
        assert isinstance(self.photo_client, Client)

    @patch('scripts.client.Client.send')
    def test_get(self, mock_send):
        mock_send.return_value.json.return_value = [data_fixture]
        self.photo_client.get('/some_url')

    @patch('scripts.client.Client.send')
    def test_get_fail(self, mock_send):
        data_fixture['albumId'] = 'fail'
        mock_send.return_value.json.return_value = [data_fixture]
        with self.assertRaises(ValidationError):
            self.photo_client.get('/some_url')

    def tearDown(self) -> None:
        del self.photo_client
