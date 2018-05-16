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


AUTHOR = 'Xavier Bourret Sicotte'
SITENAME = 'Data Blog'
SITESUBTITLE = u'Data Science, Machine Learning and Statistics'
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

ENABLE_MATHJAX = True

STATIC_PATHS = ['images', 'figures', 'downloads']

ABOUT_PAGE = '/pages/about.html'
TWITTER_USERNAME = ''
GITHUB_USERNAME = 'xavierbourretsicotte'
STACKOVERFLOW_ADDRESS = 'https://stats.stackexchange.com/users/192854/xavier-maxime'
AUTHOR_BLOG = 'http://xavierbourretsicotte.github.io/'
AUTHOR_CV = ""
SHOW_ARCHIVES = True
SHOW_FEED = False  # Need to address large feeds


# for liquid tags
#CODE_DIR = 'downloads/code'
NOTEBOOK_DIR = 'downloads/notebooks'

#Theme
MARKUP = ('md',)

PLUGIN_PATHS = ['./plugins']

PLUGINS = ['ipynb.liquid','i18n_subsites','render_math']

THEME = 'pelican-themes/aboutwilson'

JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}




