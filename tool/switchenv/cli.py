#!/usr/bin/env python
# coding=utf-8

u"""
Maya.envを切り替える
"""

from __future__ import absolute_import, division, print_function

import argparse
import logging
import sys


import impl


logger = logging.getLogger('stu.switchenv')


def main():
    # 引数の定義
    parser = argparse.ArgumentParser(description=u'hello world')
    parser.add_argument(
        '-f', '--file',
        dest='filename',
        metavar='PATH',
        help=u'input file path.'
    )
    parser.add_argument(
        '--config',
        dest='config',
        metavar='PATH',
        help=u'config dir path.'
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


    envs = impl.MayaEnv.glob()
    for env in envs:
        logger.info(unicode(env))

    maya_env = impl.get_maya_env()
    logger.info(maya_env)

    return 0


if __name__ == '__main__':
    sys.exit(main())

# EOF
