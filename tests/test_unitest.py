import unittest
from parameterized import parameterized
from main import get_doc_shelf, delete_doc, add_new_shelf

class TestFunction(unittest.TestCase):
    @parameterized.expand(
        [
            ('11-2', '1'),
            ('2207 876234', '1'),
            #('5455 028765', '1'),
            ('10006', '2')

        ]

    )
    def test_get_doc_shelf(self, a, result):
        def_result = get_doc_shelf(a)
        self.assertEqual(def_result, result)

class TestFunction2(unittest.TestCase):
    @parameterized.expand(
        [
            ('11-2', ('11-2', True)),
            ('2207 876234', ('2207 876234', True)),
            #('5455 028765',('5455 028765', True)),
            ('10006',('10006', True))

        ]

    )
    def test_delete_doc(self, b, results):
        d_result = delete_doc(b)
        self.assertEqual(d_result, results)

class TestFunction3(unittest.TestCase):
    @parameterized.expand(
        [
            ('1', False),
            ('2', False),
            ('3', False),
            ('4', True)

        ]

    )
    def test_delete_doc(self, a, result):
        d_result = add_new_shelf(a)
        self.assertEqual(d_result, result)