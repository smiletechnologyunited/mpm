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
import logging

import pymel.core as pm

import mpm.core
import mpm.util


logging.basicConfig(level=logging.INFO)


CONFNAME = "mpm.json"
SYNCDIR = "~/mpm"


def _find_conf():

    if "MAYA_APP_DIR" in os.environ:
        # MAYA_APP_DIR
        app_dir = os.environ["MAYA_APP_DIR"]
    else:
        # default
        if mpm.util.is_osx():
            app_dir = os.path.expanduser(
                "~/Library/Preferences/Autodesk/maya/")
        elif mpm.util.is_win():
            app_dir = os.path.expanduser("~/Documents/maya/")
        elif mpm.util.is_linux():
            app_dir = os.path.expanduser("~/maya/")
        else:
            raise mpm.core.MpmConfigurationError("unsupported platform.")

    version = pm.about(version=True)

    version_dir = version
    if pm.about(is64=True):
        version_dir = "{0}-x64".format(version)

    filename = os.path.join(app_dir, version_dir, CONFNAME)
    return filename


def _load():
    conf = _find_conf()
    mpm.core.Configuration(conf)


def info():
    """
    display package info.
    """
    _load()

    return


def install():
    """
    install packages.
    """

    # TODO: clone packages.
    pass


def update():
    """
    update packages.
    """
    # TODO: unload all plug-ins
    pass

    # TODO: update packages.
    pass


def initialize():
    """
    update packages.
    """

    '''
    import pprint
    pp = pprint.PrettyPrinter(indent=4, stream=sys.stderr)

    pp.pprint(os.environ["PATH"].split(":"))
    pp.pprint(os.environ["MAYA_SCRIPT_PATH"].split(":"))
    pp.pprint(os.environ["MAYA_PLUG_IN_PATH"].split(":"))
    pp.pprint(os.environ["XBMLANGPATH"].split(":"))
    pp.pprint(sys.path)
    '''

    # TODO: read configuration.
    conf = mpm.core.Configuration()
    pkgs = conf.get_packages()

    # TODO: manage SCM.

    # edit environment variables.
    pkgenv = mpm.core.PackageEnvironment()
    for p in pkgs:
        if p["disable"]:
            continue
        pkgenv.add_package(p["path"])


def gui():
    """
    open manager window.
    """
    dialog = pm.loadUI(
        uiFile='/Users/ryo/Dropbox/dev/STU/mpm/src/qtui/mainwindow.ui')
    pm.showWindow(dialog)

if __name__ == '__main__':
    pass

# EOF
