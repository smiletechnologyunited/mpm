#!/usr/bin/env python
# coding=utf-8

u"""
Maya.envを切り替える
"""

from __future__ import absolute_import, division, print_function

import glob
from logging import getLogger
import os
import re
import sys
import shutil


logger = getLogger('stu.switchenv')


def thisdir(filename=""):
    if hasattr(sys, "frozen") and sys.frozen in ("windows_exe", "console_exe"):
        path = os.path.dirname(unicode(sys.executable, sys.getfilesystemencoding()))
    else:
        path = os.path.dirname(unicode(__file__, sys.getfilesystemencoding()))

    return os.path.normpath(os.path.abspath(os.path.join(path, filename)))


def get_maya_env(version="2016"):
    u"""環境変数などを参照してMaya.envをフルパスで取得"""

    maya_app_dir = os.path.join(os.environ["USERPROFILE"], "Documents\\maya")
    if "MAYA_APP_DIR" in os.environ:
        maya_app_dir = os.environ["MAYA_APP_DIR"]

    dirpath = os.path.join(maya_app_dir, version)

    maya_env = os.path.join(dirpath, "Maya.env")
    return maya_env


class MayaEnv(object):
    u"""Maya.env単体で管理"""

    def __init__(self, path):
        self.path = os.path.normpath(os.path.abspath(path))
        self.key = None

        m = re.match("Maya_(?P<key>[^.]+).env", os.path.basename(self.path))
        if m:
            self.key = m.group("key")

    def __unicode__(self):
        return self.path

    def get_key(self):
        return self.key

    def is_valid(self):
        return self.key is not None

    def populate(self, version):
        maya_env = get_maya_env(version)
        # logger.info("shutil.copy('{0}', '{1}')".format(self.path, maya_env))
        logger.info(u"Copy {0} --> {1}".format(self.path, maya_env))
        shutil.copy(self.path, maya_env)

    @classmethod
    def glob(self, pattern=thisdir("config/*")):
        u"""指定したパターンにマッチするMaya.envを取得"""

        result = []
        for path in glob.glob(pattern):
            maya_env = MayaEnv(path)
            if not maya_env.is_valid():
                continue
            result.append(maya_env)
        return result


if __name__ == '__main__':
    pass

# EOF
