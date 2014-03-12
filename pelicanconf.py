#!/usr/bin/env python
# -*- coding: utf-8 -*- #
#
# All the setting identifiers must be set in all-caps, otherwise they will not
# be processed.  Setting values that are numbers (5, 20, etc.), booleans
# (True, False, None, etc.), dictionaries, or tuples should not be enclosed in
# quotation marks.  All other values (i.e., strings) must be enclosed in
# quotation marks.
#
# For a complete listing of the configuration parameters, see
#       http://docs.getpelican.com/en/3.3.0/settings.html#basic-settings
#       https://github.com/getpelican/pelican/wiki/Tips-n-Tricks
#       https://github.com/getpelican/pelican/tree/master/docs

from __future__ import unicode_literals

# Default language to be used in articles
DEFAULT_LANG = u'en'

# Default author of articles
AUTHOR = u'Jeff Irland'

# Web site icon (aka tab icon or bookmark icon)
FAVICON = 'favicon.ico'

# If False, content with dates in the future will geta default status of draft.
WITH_FUTURE_DATES = False

# Site title to appear in the header
HIDE_SITENAME = False
SITENAME = u"Jeff's Skinner Box"

# Logo to appear before the site name
HIDE_SITELOGO = True
SITELOGO = 'favicon.ico'
SITELOGO_SIZE = '32px'

# Display the Repost button (you need an account for your site)
DISPLAY_REPOST_BUTTON = True

# A subtitle to appear in the header
DISPLAY_PICTURE_ON_SIDEBAR = True
SIDEBAR_PICTURE = 'extra/frustrated-engineer.jpg'
SIDEBAR_TITLE = 'My Electronics Projects And Other Diversions'

# Whether to display pages and categories on the navigation menu.
# Only pages that are not "Status: hidden" will be shown.
# (Some templates may or may not honor these setting.)
DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = False

# Formating for the side bar
DISPLAY_RECENT_POSTS_ON_SIDEBAR = False
DISPLAY_CATEGORIES_ON_SIDEBAR = False
DISPLAY_TAGS_ON_SIDEBAR = False
RECENT_POST_COUNT = 5

# Comment out SITEURL during development, which will essentially give you
# root-relative URLs. Preview the site locally via python -m SimpleHTTPServer.
# When deploying to production, uncomment SITEURL, generate, and deploy.
SITEURL = ''
RELATIVE_URLS = True        # set to False when you're ready to publish

# Specify the Pelican theme to be used
#THEME = '/home/jeff/blogging/pelican-themes/pelican-bootstrap3'
THEME = '/home/jeff/blogging/theme'

# Bootswatch theme to use on Bootstrap
#BOOTSTRAP_THEME = ''
BOOTSTRAP_THEME = 'flatly'

GITHUB_RIBBON = True
GITHUB_USER = 'jeffskinnerbox'
GITHUB_URL = 'https://github.com/jeffskinnerbox/\
jeffskinnerbox.github.io/tree/source'

# your GitHub URL for a GitHub ribbon

COPYRIGHT = 'Copyright Jeffrey C. Irland, 2014'

#A list of tuples (Title, URL) for additional menu items
# to appear at the beginning of the main menu.
MENUITEMS = (('Blog', '/index.html'),
            ('Open Notebook', '/pages/open-notebook.html'),)

# Provide Google Analytics Tracking ID (i.e. ‘UA-XXXX-YYYY’)
GOOGLE_ANALYTICS = 'UA-43272292-1'

# Specify the Disqus short name identifier for comments
DISQUS_SITENAME = 'jeffskinnerbox'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None                    # Relative URL to output the Atom feed
FEED_ALL_RSS = None                     # Relative URL to output the RSS feed
CATEGORY_FEED_ATOM = None               # Where to put the category Atom feeds
TRANSLATION_FEED_ATOM = None
#FEED_ALL_RSS = 'feeds/all.rss.xml'
#CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'

# static paths will be copied without parsing their contents
STATIC_PATHS = ['images', 'extra', 'notebooks', ]

# path-specific metadata, files will be copied to your web root
EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/CNAME': {'path': 'CNAME'},
    'extra/jeffskinnerbox-favicon-(32x32).ico': {'path': 'favicon.ico'}, }
#    'extra/htaccess': {'path': '.htaccess'},

# Feeds
FEEDS = (('All posts', 'feeds/all.atom.xml'),
        ('Category', 'feeds/category'),
        ('OPW', 'feeds/tag/opw.atom.xml'),)

# Links to appear in the “social” section
SOCIAL = (('Github', 'https://github.com/jeffskinnerbox'),
          ('Twitter', 'https://twitter.com/jeffskinnerbox'),
          ('Linkedin', 'https://linkedin.com/in/jeffreyirland'),)
TWITTER_USERNAME = 'jeffskinnerbox'

# links to appear on the header (aka Blogroll)
LINKS = (('Scratch Pad', '/pages/scratch-pad.html'),
        ('RPi Packages',
            '/pages/linux-python-packages-for-my-raspberry-pi.html'),
        ('Reference Page', '/pages/reference-page.html'),
        ('Vim Cheat Sheet', '/pages/vim-cheat-sheet.html'),)

DATE_FORMATS = {'en': '%A  %B %d, %Y'}
TIMEZONE = 'America/Washington'
#DEFAULT_DATE = (2012, 3, 2, 14, 1, 1)

# When you don’t specify a category in your post metadata,
# set this setting to True, and organize your articles in subfolders,
# the subfolder will become the category of your post. If set to False,
# DEFAULT_CATEGORY will be used as a fallback.
USE_FOLDER_AS_CATEGORY = False
DEFAULT_CATEGORY = 'misc'       # The default category to fall back on.

# Delete the output directory, and all of its contents,
# before generating new files.
DELETE_OUTPUT_DIRECTORY = True

# If set to True, several typographical improvements will be incorporated
# into the generated HTML via the Typogrify
TYPOGRIFY = True

# If False, content with dates in the future will have "Status: draft"
WITH_FUTURE_DATES = False

#LOGOIMAGE = '/theme/macdrifter-logo-art/macdrifter-logo_280px.png'

# Specify the Pelican plugins to be used
PLUGIN_PATH = '/home/jeff/blogging/pelican-plugins'
#PLUGINS = ['latex', 'neighbors', 'summary']

# List of the extensions that the Markdown processor will use.
# The styles manni, emacs, native seem to work.
MD_EXTENSIONS = ['extra', 'codehilite(noclasses=True, pygments_style=manni, \
                 guess_lang=False)']

# code blocks with line numbers
#PYGMENTS_RST_OPTIONS = {'linenos': 'table'}

# syntax highlighting style used by Pygment
#PYGMENTS_STYLE = 'native'
#PYGMENTS_STYLE = 'xcode'

# Paths to find content from which it can be served
PATH = 'content'
PAGE_DIR = 'pages'
ARTICLE_DIR = 'articles'
ARTICLE_EXCLUDES = ('draft', 'TBD',)

# List of directories to exclude when looking for pages.
PAGE_EXCLUDES = ('draft', 'TBD',)

# Locations where files will be saved in output.
OUTPUT_PATH = 'output/'
ARTICLE_URL = 'posts/{date:%Y}/{date:%b}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%b}/{date:%d}/{slug}/index.html'
PAGE_URL = 'pages/{slug}.html'
PAGE_SAVE_AS = 'pages/{slug}.html'

CATEGORY_URL = "category/{slug}"
CATEGORY_SAVE_AS = "category/{slug}/index.html"

TAG_URL = "tag/{slug}/"
TAG_SAVE_AS = "tag/{slug}/index.html"

# Location of per-year and per-month archives of your posts
YEAR_ARCHIVE_SAVE_AS = 'archives/{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = 'archives/{date:%Y}/{date:%b}/index.html'

DEFAULT_PAGINATION = 10
PAGINATED_DIRECT_TEMPLATES = ('index',)
