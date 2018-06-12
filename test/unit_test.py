import unittest

from src.models import UserModel
from src.resources import create_response


class TestGeneral(unittest.TestCase):
    def test_hash(self):
        password = "password"
        pass_hash = UserModel.generate_hash(password)
        self.assertTrue(UserModel.verify_hash(password, pass_hash))

    def test_response_200(self):
        response = create_response({'a': 'a'}, 200)
        self.assertTrue(response.status_code == 200)

    def test_response_404(self):
        response = create_response({'a': 'a'}, 404)
        self.assertTrue(response.status_code == 404)

    def test_cors_headers(self):
        response = create_response({'a': 'a'}, 200)
        headers_list = []
        for h in response.headers:
            headers_list.append(h)

        self.assertTrue(('Access-Control-Allow-Origin', '*') in headers_list)
        self.assertTrue(('Access-Control-Allow-Methods',
                         'PUT, GET, POST, DELETE, OPTIONS') in headers_list)
        self.assertTrue(('Access-Control-Allow-Headers',
                         'Origin, Accept, Content-Type, Authorization') in headers_list)


if __name__ == '__main__':
    unittest.main()
