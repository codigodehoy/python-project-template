# -*- coding: utf-8 -*-

from .subpackage import bar


def repeat_bar(num: int) -> str:
    return bar.return_bar() * num
