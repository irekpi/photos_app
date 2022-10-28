import json
import unittest
from pydantic.error_wrappers import ValidationError
from scripts.file_client import FilePhotoClient

data_fixture = [{
    "albumId": 1,
    "id": 1,
    "title": "accusamus beatae ad facilis cum similique qui sunt",
    "url": "https://via.placeholder.com/600/92c952",
    "thumbnailUrl": "https://via.placeholder.com/150/92c952"
}]


def prepare_bytes(data):
    return json.dumps(data, indent=2, separators=(',', ': ')).encode('utf-8')


class TestFilePhotoClient(unittest.TestCase):
    def setUp(self):
        self.file_photo_client = FilePhotoClient()

    def test_args_self(self):
        assert all(item in dir(self.file_photo_client) for item in ['parse', 'get_local'])

    def test_parse(self):
        parsed = self.file_photo_client.parse(prepare_bytes(data_fixture))
        self.assertEqual(parsed, data_fixture)

    def test_parse_fail(self):
        data_fixture[0]['albumId'] = 'fail'
        data = prepare_bytes(data_fixture)
        with self.assertRaises(ValidationError):
            self.file_photo_client.parse(data)
