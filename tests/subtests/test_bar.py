# -*- coding: utf-8 -*-

from package.subpackage import bar


def test_bar():
    assert bar.return_bar() == "bar!"
