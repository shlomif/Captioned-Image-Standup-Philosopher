#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2022 Shlomi Fish < https://www.shlomifish.org/ >
#
# Licensed under the terms of the Expat license.

"""

"""

import re
import sys

delta = 30.0
starty = 60.0
ys = [None]

y = starty + 0
for n in range(3):
    for _ in range(2):
        ys.append(y + 0)
    y += delta


def get_y(m):
    y = ys.pop(0)
    ret = float(m.group(1))
    if y is not None:
        ret += y
    return "{}".format(ret)


def wrapper(mself):
    """docstring for wrapper"""
    return " y=\"" + get_y(mself) + "\""


for line in sys.stdin:
    print(re.sub(" y=\"([0-9\\.\\-]+)\"", wrapper, line), end='')
