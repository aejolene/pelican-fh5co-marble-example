#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os

AUTHOR = 'Claudio Walser'
SITENAME = 'FH5CO Marble Example'
SITEDESCRIPTION = 'this is just an example page for the pelican-fh5co-marble theme.'
SITEURL = 'http://localhost:8081'

# plugins
PLUGIN_PATHS = ['../pelican-plugins']
PLUGINS = ['i18n_subsites', 'tipue_search']
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}

# theme and theme localization
THEME = '../pelican-fh5co-marble'
I18N_GETTEXT_LOCALEDIR = '../pelican-fh5co-marble/locale/'
I18N_GETTEXT_DOMAIN = 'messages'
I18N_GETTEXT_NEWSTYLE = True
TIMEZONE = 'Europe/Zurich'
DEFAULT_DATE_FORMAT = '%a, %d %b %Y'
I18N_TEMPLATES_LANG = 'en_US'
DEFAULT_LANG = 'en'
LOCALE = 'en_US'

# content paths
PATH = 'content'
PAGE_PATHS = ['pages/en']
ARTICLE_PATHS = ['blog/en']
# logo path, needs to be stored in PATH Setting
LOGO = '/images/logo.svg'

# special content
HERO = [
  {
    'image': '/images/hero/background-1.jpg',
    # for multilanguage support, create a simple dict
    'title': {
      'en':'Some special content'
    },
    'text': {
      'en': 'Any special content you want to tease here'
    },
    'links': [
      {
        'icon': 'icon-code',
        'url': 'https://github.com/claudio-walser/pelican-fh5co-marble',
        'text': 'Github'
      }
    ]
  }, {
    'image': '/images/hero/background-2.jpg',
    # keep it a string if you dont need multiple languages
    'title': 'Uh, special too',
    # keep it a string if you dont need multiple languages
    'text': 'Keep hero.text and hero.title a string if you dont need multilanguage.',
    'links': []
  }, {
    'image': '/images/hero/background-3.jpg',
    'title': 'No Blogroll yet',
    'text': 'Because of space issues in the man-nav, i didnt implemented Blogroll links yet.',
    'links': []
  }, {
    'image': '/images/hero/background-4.jpg',
    'title': 'Ads missing as well',
    'text': 'And since i hate any ads, this is not implemented as well',
    'links': []
  }
]

# Social widget
SOCIAL = (
  ('Github', 'https://www.github.com/claudio-walser/gitcd'),
  ('Read the Docs', 'https://gitcd.readthedocs.io/en/latest/?badge=latest'),
  ('Travis', 'https://travis-ci.org/claudio-walser/gitcd')
)

ABOUT = {
  'image': '/images/about/about.jpeg',
  'mail': 'info@gitcd.io',
  # keep it a string if you dont need multiple languages
  'text': {
    'en': 'Learn more about the creator of this theme or just drop a message.'
  },
  'link': 'contact.html',
  # the address is also taken for google maps
  'address': 'Zürich, Schweiz',
  'phone': '+555-shoe'
}

# navigation and homepage options
DISPLAY_PAGES_ON_MENU = True
DISPLAY_PAGES_ON_HOME = True
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_TAGS_ON_MENU = False
USE_FOLDER_AS_CATEGORY = True
PAGE_ORDER_BY = 'order'

MENUITEMS = [
  ('Archive', 'archives.html'),
  ('Contact', 'contact.html')
]

DIRECT_TEMPLATES = [
  'index',
  'tags',
  'categories',
  'authors',
  'archives',
  'search', # needed for tipue_search plugin
  'contact' # needed for the contact form
]

# setup disqus
DISQUS_SHORTNAME = 'gitcd-dev'
DISQUS_ON_PAGES = False # if true its just displayed on every static page, like this you can still enable it per page

# setup google maps
GOOGLE_MAPS_KEY = 'AIzaSyCefOgb1ZWqYtj7raVSmN4PL2WkTrc-KyA'












# other config options
# FEED_ALL_ATOM = None
# CATEGORY_FEED_ATOM = None
# TRANSLATION_FEED_ATOM = None
# AUTHOR_FEED_ATOM = None
# AUTHOR_FEED_RSS = None




# PYGMENTS_RST_OPTIONS = {}





# I18N_SUBSITES = {
#   'en': {
#     'PAGE_PATHS': ['pages/en'],
#     'ARTICLE_PATHS': ['blog/en'],
#     'LOCALE': 'en_US'
#   }, 'fr': {
#     'PAGE_PATHS': ['pages/fr'],
#     'ARTICLE_PATHS': ['blog/fr'],
#     'LOCALE': 'fr_FR'
#   }, 'es': {
#     'PAGE_PATHS': ['pages/es'],
#     'ARTICLE_PATHS': ['blog/es'],
#     'LOCALE': 'es_ES'
#   }
# }





# DEFAULT_PAGINATION = 2

