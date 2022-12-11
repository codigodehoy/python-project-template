# -*- coding: utf-8 -*-

from project_name.subpackage import bar


def test_bar():
    assert bar.return_bar() == "bar!"
