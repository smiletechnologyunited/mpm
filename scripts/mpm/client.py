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
import shutil

import pymel.core as pm

import mpm.core
import mpm.util


logging.basicConfig(level=logging.INFO)


CONFNAMENAME = "mpm.conf"
SYNCDIRNAME = "mpm"


def _get_app_dirpath():

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
            raise mpm.util.MpmConfigurationError("unsupported platform.")

    return app_dir


def _get_version_dirname():
    version = pm.about(version=True)

    version_dir = version
    if pm.about(is64=True):
        version_dir = "{0}-x64".format(version)

    return version_dir


def _get_conf_filepath():
    app_dir = _get_app_dirpath()
    version_dir = _get_version_dirname()
    filename = os.path.join(app_dir, version_dir, CONFNAMENAME)
    return filename


def _get_sync_dirpath():
    app_dir = _get_app_dirpath()
    version_dir = _get_version_dirname()
    dirname = os.path.join(app_dir, version_dir, SYNCDIRNAME)
    return dirname


def _get_conf_info():
    conf_filepath = _get_conf_filepath()
    if not os.path.isfile(conf_filepath):
        raise mpm.util.MpmConfigurationError("can't find configuration file.")

    sync_dirpath = _get_sync_dirpath()
    if not os.path.isdir(sync_dirpath):
        logging.info("make directory. ({0})".format(sync_dirpath))
        os.makedirs(sync_dirpath)

    return (conf_filepath, sync_dirpath)


def info():
    """
    display package info.
    """
    (conf_filepath, sync_dirpath) = _get_conf_info()
    conf = mpm.core.Configuration(conf_filepath, sync_dirpath)

    for p in conf.get_packages():
        sys.stdout.write("")

    '''
    import pprint
    pp = pprint.PrettyPrinter(indent=4, stream=sys.stderr)

    pp.pprint(os.environ["PATH"].split(":"))
    pp.pprint(os.environ["MAYA_SCRIPT_PATH"].split(":"))
    pp.pprint(os.environ["MAYA_PLUG_IN_PATH"].split(":"))
    pp.pprint(os.environ["XBMLANGPATH"].split(":"))
    pp.pprint(sys.path)
    '''


def install():
    """
    install packages.
    """
    (conf_filepath, sync_dirpath) = _get_conf_info()
    conf = mpm.core.Configuration(conf_filepath, sync_dirpath)

    # clone packages.
    for p in conf.get_packages():
        s = p["scm"]()
        s.clone(p["origin"], p["path"])

    # initialize again
    initialize()


def clean():
    """
    clean up packages.
    """
    (conf_filepath, sync_dirpath) = _get_conf_info()

    for p in os.listdir(sync_dirpath):
        target = os.path.join(sync_dirpath, p)
        if os.path.isdir(target):
            shutil.rmtree(target)
        else:
            os.remove(target)
        logging.info("rm {0}".format(target))


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
    initialize environment.
    """
    # read configuration.
    (conf_filepath, sync_dirpath) = _get_conf_info()
    conf = mpm.core.Configuration(conf_filepath, sync_dirpath)

    pkgenv = mpm.core.PackageEnvironment()

    # edit environment variables.
    for p in conf.get_packages():
        pkgenv.add_package(p["path"])


def gui():
    """
    open window.
    """
    dialog = pm.loadUI(
        uiFile='/Users/ryo/Dropbox/dev/STU/mpm/src/qtui/mainwindow.ui')
    pm.showWindow(dialog)


if __name__ == '__main__':
    pass

# EOF
