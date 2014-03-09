#!/usr/bin/env python
# coding=utf-8

# Copyright (c) 2014 Smile Technology United, inc.
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
# OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
# DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE
# OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


import unittest
import os

import mpm.core


def thisDir(name):
    current = os.path.abspath(os.path.dirname(__file__))
    return os.path.join(current, name)


class MpmTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def test_load_config(self):
        pass

        conf_filepath = thisDir("fixtures/mpm.conf")
        sync_dirpath = thisDir("./temp/")
        conf = mpm.core.Configuration(conf_filepath, sync_dirpath)

        # clone packages.
        for p in conf.get_packages():
            s = p["scm"]()
            s.clone(p["origin"], p["path"])


# EOF
