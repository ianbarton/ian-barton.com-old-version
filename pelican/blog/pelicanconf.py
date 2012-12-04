#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u"Ian Barton"
SITENAME = u"Ian's Blog"
SITEURL = 'http://www.ian-barton.com'

TIMEZONE = 'Europe/Paris'
MARKUP = (('rst', 'md', 'yml'))
DEFAULT_LANG = 'en'

# Blogroll
LINKS =  (('Pelican', 'http://docs.notmyidea.org/alexis/pelican/'),
          ('Python.org', 'http://python.org'),
          ('Jinja2', 'http://jinja.pocoo.org'),
          ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

OUTPUT_PATH = "~/dropbox/public_html/pelican"

STATIC_PATHS = (['images'])

ARTICLE_URL = "posts/{date:%Y}/{date:%b}/{date:%d}/{slug}/"
ARTICLE_SAVE_AS = "posts/{date:%Y}/{date:%b}/{date:%d}/{slug}/index.html"
