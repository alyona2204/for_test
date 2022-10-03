import unittest
from parameterized import parameterized
from ya_api import create_folder
import requests

class TestFunction(unittest.TestCase):
    @parameterized.expand(
        [
            ('hello world', (201, 'Папка hello world была добавлена в Я.Диск')),
            ('hello world', (409, 'Папка hello world не была добавлена в Я.Диск'))

        ]

    )
    def test_create_folder(self, a, result):
        f_result = create_folder(a)
        self.assertEqual(f_result, result)