# -*- coding: utf-8 -*-

from project_name import foo


def test_repeat_bar():
    assert foo.repeat_bar(10) == "bar!" * 10
    assert foo.repeat_bar(0) == ""
    assert foo.repeat_bar(-10) == ""
