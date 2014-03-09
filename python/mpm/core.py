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
import re

import mpm.util
import mpm.scm


logging.basicConfig(level=logging.INFO)


class PackageEnvironment(object):
    DIR_TYPES = [
        ("MAYA_SCRIPT_PATH", "scripts"),
        ("MAYA_PLUG_IN_PATH", "plug-ins"),
        ("XBMLANGPATH", "icons"),
        ("PYTHONPATH", "python"),
    ]

    def __init__(self):
        if mpm.util.is_osx() or mpm.util.is_linux():
            self._sp_c = ":"
        elif mpm.util.is_win():
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

            os.environ[envname] = "{0}{1}{2}".format(
                os.environ[envname], self._sp_c, path)
            logging.info("add {0}".format(path))

    def add_package(self, p):
        # TODO: check directory construction.
        pass

        # add path
        for (envname, dirname) in self.DIR_TYPES:
            path = os.path.join(p, dirname)
            if os.path.exists(path):
                self._add_path(envname, path)


class Configuration(object):
    def __init__(self, conf_filepath, sync_dirpath="./"):
        with open(conf_filepath) as fp:
            self._conf = json.load(fp)

        self._sync_dirpath = sync_dirpath

    def detect(self, origin):
        pass

    def get_packages(self):
        packages = []
        for c in self._conf:
            # name
            if "name" in c:
                name = c["name"]
            else:
                name = os.path.basename(c["origin"])
                if name.endswith(".git"):
                    name = name[:-4]

            # origin
            protocol = None
            m = re.search(r"^[^:]*", c["origin"])
            if m:
                protocol = m.group()

            if protocol in ["http", "https"]:
                uri = c["origin"]
                if c["origin"].endswith(".git"):
                    scm = mpm.scm.SyncGit
                else:
                    scm = mpm.scm.SyncSvn
            elif protocol in ["git"]:
                uri = c["origin"]
                scm = mpm.scm.SyncGit
            elif protocol in ["svn"]:
                uri = c["origin"]
                scm = mpm.scm.SyncGit
            elif protocol in ["ssh"]:
                uri = c["origin"]
                scm = mpm.scm.SyncGit
            elif c["origin"].startswith("/"):
                uri = c["origin"]
                scm = mpm.scm.SyncRsync
            else:
                uri = "git://github.com/{0}".format(c["origin"])
                scm = mpm.scm.SyncGit

            # path
            path = os.path.join(self._sync_dirpath, name)

            # other
            if "revision" in c:
                revision = c["revision"]
            else:
                revision = None

            packages.append({
                "name": name,
                "path": path,
                "origin": uri,
                "revision": revision,
                "scm": scm,
            })
        return packages


if __name__ == '__main__':
    pass

# EOF
