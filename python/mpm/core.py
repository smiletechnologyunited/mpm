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

from __future__ import print_function
import os
import sys
import site
import logging
import json

import util


logging.basicConfig(level=logging.INFO)


class MpmError(Exception):
    pass


class MpmConfigurationError(MpmError):
    pass


class MpmSyncError(MpmError):
    pass


class MpmRuntimeError(MpmError):
    pass


class PackageEnvironment(object):
    DIR_TYPES = [
        ("MAYA_SCRIPT_PATH", "scripts"),
        ("MAYA_PLUG_IN_PATH", "plug-ins"),
        ("XBMLANGPATH", "icons"),
        ("PYTHONPATH", "python"),
    ]

    def __init__(self):
        if util.is_osx() or util.is_linux():
            self._sp_c = ":"
        elif util.is_win():
            self._sp_c = ";"

    def _add_path(self, envname, path):
        if envname == "PYTHONPATH":
            if path in sys.path:
                return

            site.addsitedir(path)
            logging.info("add {0}".format(path))
        else:
            if not envname in os.environ:
                return

            paths = os.environ[envname].split(self._sp_c)
            if path in paths:
                return

            os.environ[envname] += ":"+path
            logging.info("add {0}".format(path))

    def add_package(self, p):
        # TODO: check directory construction.
        pass

        # add path
        for (envname, dirname) in self.DIR_TYPES:
            path = os.path.join(p, dirname)
            self._add_path(envname, path)


class Configuration(object):
    def __init__(self, filename=None):
        if filename:
            with open(filename) as fp:
                self._conf = json.load(fp)
        else:
            self._conf = []

    def get_packages(self):
        result = []
        for c in self._conf:
            tmp = {
                "name": c["name"],
                "path": c["origin"],
                "scm": None,
                "revision": None,
                "disable": False,
                "origin": c["origin"],
            }
            result.append(tmp)
        return result


class Sync(object):
    def __init__(self):
        pass

    def sync():
        pass

    def revision():
        pass


class SyncNothing(Sync):
    def __init__(self):
        pass

    def sync():
        pass

    def revision():
        pass


class SyncGit(Sync):
    def __init__(self):
        pass

    def sync():
        pass

    def revision():
        pass


if __name__ == '__main__':
    pass

# EOF
