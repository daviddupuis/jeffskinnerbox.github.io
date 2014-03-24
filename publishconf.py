#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = 'http://jeffskinnerbox.me'
RELATIVE_URLS = False

FEED_DOMAIN = SITEURL
FEED_ALL_ATOM = 'feeds/all.atom.xml'
FEED_ALL_RSS = 'feeds/all.rss.xml'
#TAG_FEED_ATOM = 'feeds/%s.tag.atom.xml'
#CATEGORY_FEED_ATOM = 'feeds/%s.category.atom.xml'
FEED_MAX_ITEMS = 100

# List of templates that are used directly to render content.
DIRECT_TEMPLATES = ('index', 'tags', 'categories', 'archives', 'sitemap')
SITEMAP_SAVE_AS = 'sitemap.xml'

DELETE_OUTPUT_DIRECTORY = True
DISPLAY_REPOST_BUTTON = True
GOOGLE_ANALYTICS_ON = True
DISQUS_ON = True
