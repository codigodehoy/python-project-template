# -*- coding: utf-8 -*-

import utils  # for ModuleNotFoundError
from project_name import foo
import unittest


class FooTest(unittest.TestCase):
    def test_bar(self):
        self.assertEqual(foo.bar(), "bar!")

    def test_zoo(self):
        self.assertEqual(foo.zoo(), "zoo!")


if __name__ == "__main__":
    unittest.main()
