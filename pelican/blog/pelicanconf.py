#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u"Ian Barton"
SITENAME = u"ian-barton.com"
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
SOCIAL = (('Twitter', 'http://twitter.com/ianbarton'),
          ('Github', 'http://github.com/geekinthesticks'),)

DEFAULT_PAGINATION = 10

OUTPUT_PATH = "/srv/http"

STATIC_PATHS = (['images'])

#NEWEST_FIRST_ARCHIVES (True)

FEED_ALL_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'

ARTICLE_URL = "posts/{date:%Y}/{date:%b}/{date:%d}/{slug}/"
ARTICLE_SAVE_AS = "posts/{date:%Y}/{date:%b}/{date:%d}/{slug}/index.html"

DISQUS_SITENAME = "ianbarton"
GITHUB_URL = "https://github.com/geekinthesticks"
GOOGLE_ANALYTICS = "UA-7259094-1"
TWITTER_USERNAME = 'ianbarton'
