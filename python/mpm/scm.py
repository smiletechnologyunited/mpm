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
import subprocess

import mpm.util


class Sync(object):
    def __init__(self):
        pass

    def clone(self, origin, dirpath):
        pass

    def update(self, dirpath):
        pass


class SyncRsync(Sync):
    def __init__(self):
        pass

    def clone(self, origin, dirpath):
        pass

    def update(self, dirpath):
        pass


class SyncGit(Sync):
    def __init__(self):
        if mpm.util.is_win():
            self.shell = True
        else:
            self.shell = False

    def clone(self, origin, dirpath):
        if os.path.isdir(dirpath):
            return

        cmd = ["git", "clone", origin, dirpath]

        sys.stderr.write(" ".join(cmd))
        p = subprocess.Popen(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            shell=self.shell)
        (stdout, stderr) = p.communicate()
        if p.returncode:
            #sys.stdout.write(stdout)
            #sys.stderr.write(stderr)
            raise mpm.util.MpmSyncError(stderr)

    def update(self, dirpath):
        if not os.path.isdir(dirpath):
            return

        cmd = ["git", "pull", dirpath]

        p = subprocess.Popen(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            shell=self.shell)
        (stdout, stderr) = p.communicate()
        #if p.returncode and not p.returncode == 1:
        if p.returncode:
            #sys.stdout.write(stdout)
            #sys.stderr.write(stderr)
            raise mpm.util.MpmSyncError(stderr)



if __name__ == '__main__':
    pass

# EOF
