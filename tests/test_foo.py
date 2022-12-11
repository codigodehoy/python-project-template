# -*- coding: utf-8 -*-

import unittest

from project_name import foo


class FooTest(unittest.TestCase):
    def test_repeat_bar(self):
        self.assertEqual(foo.repeat_bar(10), "bar!" * 10)
        self.assertEqual(foo.repeat_bar(0), "")
        self.assertEqual(foo.repeat_bar(-10), "")


if __name__ == "__main__":
    unittest.main()
