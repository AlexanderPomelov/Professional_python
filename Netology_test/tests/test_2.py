from Netology_test.tests import config
from unittest import TestCase
from Netology_test.API.api_yd import Ya_disk

class MyTestCase(TestCase):
    def setUp(self) -> None:
        self.ya = Ya_disk()
    def test_create_folder(self):

        result = self.ya.create_folder('test_folder')
        expected = 'test_create_folder'
        self.assertNotEquals(expected, result)

    def test_resopnse_status_code(self):
        result = self.ya.response_status()
        expected = 200
        self.assertEqual(result, expected)
#
if __name__ == '__main__':
    res = MyTestCase()
    res.test_create_folder()
    res.test_resopnse_status_code()


