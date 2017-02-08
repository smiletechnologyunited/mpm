#!/usr/bin/env python
# coding=utf-8

u"""
Maya.envを切り替える
"""

from __future__ import absolute_import, division, print_function

import argparse
import logging
import sys

from PySide import QtGui
# from PySide import QtCore

import impl
import ui.switchenv


logger = logging.getLogger('stu.switchenv')


class MainWindow(QtGui.QMainWindow, ui.switchenv.Ui_MainWindow):
    TITLE = "Switch Env"

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        self.setWindowTitle(self.TITLE)

        versions = ["2015-x64", "2016", "2016.5", "2017"]
        for version in versions:
            self.version.addItem(version, version)

        envs = impl.MayaEnv.glob()
        for env in envs:
            self.project.addItem(env.get_key(), env)

        self.btn_switch.clicked.connect(self.callback_switch)

    def callback_switch(self):
        index = self.version.currentIndex()
        version_data = self.version.itemData(index)
        logger.debug(version_data)

        index = self.project.currentIndex()
        project_data = self.project.itemData(index)
        logger.debug(project_data)

        project_data.populate(version_data)


def main():
    # 引数の定義
    parser = argparse.ArgumentParser(description=u'hello world')
    parser.add_argument(
        '-f', '--file',
        dest='filename',
        type=str, default=None,
        metavar='PATH',
        help=u'input file path.'
    )
    parser.add_argument(
        '-D', '--debug',
        dest='debug',
        action="store_true", default=False,
        help=u'debug mode.'
    )
    args = parser.parse_args()

    # ロガー初期化
    if args.debug:
        LOG_FORMAT = r"%(asctime)s %(name)s [%(levelname)s] %(filename)s:%(lineno)d %(message)s"
        LOG_LEVEL = logging.DEBUG
    else:
        LOG_FORMAT = r"[%(levelname)s] %(message)s"
        LOG_LEVEL = logging.INFO

    _logger = logging.getLogger('stu')
    _logger.handlers = []
    _stream_handler = logging.StreamHandler()
    _formatter = logging.Formatter(LOG_FORMAT)
    _stream_handler.setFormatter(_formatter)
    _logger.addHandler(_stream_handler)
    _logger.setLevel(LOG_LEVEL)

    # PySide初期化
    app = QtGui.QApplication(sys.argv)

    frame = MainWindow()
    frame.show()

    app.exec_()

    return 0


if __name__ == '__main__':
    sys.exit(main())

# EOF
