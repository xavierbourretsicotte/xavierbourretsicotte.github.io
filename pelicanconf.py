#!/usr/bin/env python
# -*- coding: utf-8 -*- #

from __future__ import unicode_literals
import platform

def is_windows():
    if platform.system() == 'Windows': return True
    else: return False

def system_path(path):
    """Return path with forward or backwards slashes as necessary based on OS"""
    if is_windows(): return path.replace('/', '\\')
    else: return path.replace('\\', '/')

########################### General Settings ###################################


AUTHOR = u'Xavier Bourret Sicotte'
SITENAME = u"Xavier 's Data Blog"
SITESUBTITLE = u"A blog dedicated to data, mathematics and good looking graphs"
SITEURL = ''

PATH = 'content'
DELETE_OUTPUT_DIRECTORY = True

TIMEZONE = 'Europe/Paris'
DEFAULT_LANG = u'en'

USE_FOLDER_AS_CATEGORY = True


# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None


# Blogroll
LINKS = (
         ('Centre National des Arts et Metiers', 'http://www.cnam.fr/portail/conservatoire-national-des-arts-et-metiers-821166.kjsp'),
         )

# Social widget
SOCIAL = (('github', 'https://github.com/xavierbourretsicotte'),
          ('linkedin', 'https://www.linkedin.com/in/xavier-bourret-sicotte/'),
          )

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True


STATIC_PATHS = ['images']



#Theme
MARKUP = ('md',)

PLUGIN_PATHS = ['./plugins']

PLUGINS = ['ipynb.liquid','i18n_subsites']

THEME = 'pelican-themes/pelican-bootstrap3'
JINJA_ENVIRONMENT = {
    'extensions': ['jinja2.ext.i18n'],
}


