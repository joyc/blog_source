#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'hython'
SITENAME = "Hython's Blog"
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Asia/Tokyo'

DEFAULT_LANG = 'en'

THEME = 'theme'
BOOTSTRAP_THEME = 'lumen'
PYGMENTS_STYLE = 'native'

# Markdown扩展
MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
        'markdown.extensions.tables': {  # 表格
        },
        'markdown.extensions.toc': {     # 目录，设置看https://python-markdown.github.io/extensions/toc/
            'title': 'TOC:',      # 目录题头
            'toc_depth': 3,
        },
    },
    'output_format': 'html5',
}

PLUGIN_PATHS = ['plugins/', ]

PLUGINS = ['i18n_subsites', ]

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),)

# Social widget
SOCIAL = (('Twitter', 'https://twitter.com/joyc'),
          ('Github', 'https://github.com/joyc'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

OUTPUT_PATH = '../output'

JINJA_ENVIRONMENT = {
    'extensions': ['jinja2.ext.i18n'],
}

ARTICLE_PATHS = ['articles']
PAGE_PATHS = ['pages']

# Defining the URL Structure
ARTICLE_URL = 'articles/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'articles/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'
PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = 'pages/{slug}/index.html'
CATEGORY_URL = 'category/{slug}'
CATEGORY_SAVE_AS = 'category/{slug}/index.html'
TAG_URL = 'tag/{slug}'
TAG_SAVE_AS = 'tag/{slug}/index.html'

# Setting Domain
DELETE_OUTPUT_DIRECTORY = True
OUTPUT_RETENTION = ['CNAME']

# Disqus comments config
DISQUS_SITENAME = 'hython'

# google Analystic
GOOGLE_ANALYTICS = 'UA-136778315-2'

CC_LICENSE = 'CC-BY-NC-SA'
