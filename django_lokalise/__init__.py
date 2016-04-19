#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of django-lokalise.
# https://github.com/yarlson/django-lokalise

# Licensed under the BSD license:
# http://www.opensource.org/licenses/BSD-license
# Copyright (c) 2016, Yar Kravtsov <yarlson@gmail.com>

import errno
import os
import re

from django.conf import settings

from django_lokalise.version import __version__  # NOQA

VERSION = '0.0.1'


def get_locale_path():
    p = os.path.dirname(os.path.normpath(os.sys.modules[settings.SETTINGS_MODULE].__file__))
    return os.path.join(re.sub(r"settings$", "", p), 'locale')


def make_dir(folder_name):
    try:
        os.makedirs(folder_name)
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise
