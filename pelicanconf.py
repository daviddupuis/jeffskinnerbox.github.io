#!/usr/bin/env python
# -*- coding: utf-8 -*- #
#
# All the setting identifiers must be set in all-caps, otherwise they will not
# be processed.  Setting values that are numbers (5, 20, etc.), booleans
# (True, False, None, etc.), dictionaries, or tuples should not be enclosed in
# quotation marks.  All other values (i.e., strings) must be enclosed in
# quotation marks.
#
# For a more complete listing of the configuration parameters, see
#       http://docs.getpelican.com/en/3.3.0/settings.html#basic-settings
#       https://github.com/getpelican/pelican/wiki/Tips-n-Tricks
#       https://github.com/getpelican/pelican/tree/master/docs

from __future__ import unicode_literals

# Default language to be used in articles
#DEFAULT_LANG = u'en'

DATE_FORMATS = {'en': '%A&nbsp;&nbsp;&nbsp;&nbsp;%B %d, %Y'}
TIMEZONE = 'America/New_York'
#DEFAULT_DATE = (2012, 3, 2, 14, 1, 1)

# Default author of articles
AUTHOR = u'Jeff Irland'

DISPLAY_BREADCRUMBS = False

# Web site icon (aka tab icon or bookmark icon)
FAVICON = 'favicon.ico'

# If False, content with dates in the future will get default status of draft.
WITH_FUTURE_DATES = False

# Site title to appear in the header
HIDE_SITENAME = False
SITENAME = u"Jeff's Skinner Box"

# Include articles comment count on home page
SUMMARY_COMMENT_COUNT = False

# Logo to appear before the site name
HIDE_SITELOGO = True
SITELOGO = 'favicon.ico'
SITELOGO_SIZE = '32px'

# Display the Repost button (you need an account for your site)
DISPLAY_REPOST_BUTTON = False

# A subtitle to appear in the header
DISPLAY_PICTURE_ON_SIDEBAR = True
SIDEBAR_PICTURE = 'extra/frustrated-engineer.jpg'
SIDEBAR_TITLE = 'My Electronics Projects And Other Diversions'

# Whether to display pages and categories on the navigation menu.
# Only pages that are not "Status: hidden" will be shown.
# (Some templates may or may not honor these setting.)
DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_ARCHIVES_ON_MENU = True

# Formating for the side bar
DISPLAY_RECENT_POSTS_ON_SIDEBAR = False
DISPLAY_CATEGORIES_ON_SIDEBAR = False
DISPLAY_TAGS_ON_SIDEBAR = False
RECENT_POST_COUNT = 5

# generate a tag cloud with all your tags (Note: The a TAG_CLOUD_STEPS
# value greater than 4 requires a custom CSS file.  See extra/custom.css)
TAG_CLOUD_STEPS = 8
TAG_CLOUD_MAX_ITEMS = 100

# Comment out SITEURL during development, which will essentially give you
# root-relative URLs. Preview the site locally via python -m SimpleHTTPServer.
# When deploying to production, uncomment SITEURL, generate, and deploy.
#SITEURL = ''
RELATIVE_URLS = True        # always set to False when you're ready to publish

# Specify the Pelican theme to be used
#THEME = '/home/jeff/blogging/pelican-themes/pelican-bootstrap3'
THEME = '/home/jeff/blogging/theme'

# Bootstrap theme to be use.  Supported themes are: amelia, cerulean, cosmo,
# cyborg, flatly, journal, readable, readable-old, simplex, slate, spacelab,
# united, yeti, and <nothing>
# See http://bootswatch.com/
BOOTSTRAP_THEME = 'flatly'
BOOTSTRAP_NAVBAR_INVERSE = False

GITHUB_RIBBON = True
GITHUB_RIBBON_LEFT = False
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
GOOGLE_ANALYTICS_ON = False
GOOGLE_ANALYTICS_ID = 'UA-43272292-1'

# Specify the Disqus short name identifier for comments
DISQUS_ON = False
DISQUS_SITENAME = 'jeffskinnerbox'
DISQUS_DISPLAY_COUNTS = True

# Feed generation is usually not desired when developing
FEED_DOMAIN = None
FEED_ATOM = None
FEED_ALL_ATOM = None
TAG_FEED_ATOM = None
CATEGORY_FEED_ATOM = None
FEED_RSS = None
FEED_ALL_RSS = None
TAG_FEED_RSS = None
CATEGORY_FEED_RSS = None
TRANSLATION_FEED_ATOM = None

# Feeds
#FEEDS = (('All posts', 'feeds/all.atom.xml'),
#        ('Category', 'feeds/category'),
#        ('OPW', 'feeds/tag/opw.atom.xml'),)

# This CSS file will over ride the other CCS specifications
CUSTOM_CSS = 'static/custom.css'

# static paths will be copied without parsing their contents
STATIC_PATHS = ['images', 'extra', 'notebooks', 'extra/custom.css', ]

# path-specific metadata,
# files will be moved to web site root (and some renamed)
EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/CNAME': {'path': 'CNAME'},
    'extra/htaccess': {'path': '.htaccess'},
    'extra/404.html': {'path': '404.html'},
    'extra/custom.css': {'path': 'static/custom.css'},
    'extra/jeffskinnerbox-favicon-(32x32).ico': {'path': 'favicon.ico'}, }

# Links to appear in the “social” section
SOCIAL = (('Github', 'https://github.com/jeffskinnerbox'),
          ('Twitter', 'https://twitter.com/jeffskinnerbox'),
          ('Linkedin', 'https://linkedin.com/in/jeffreyirland'),)
TWITTER_USERNAME = 'jeffskinnerbox'

# links to appear on the header (aka Blogroll)
LINKS = (('Scratch Pad', '/pages/scratch-pad.html'),
        ('RPi Packages',
            '/pages/linux-and-python-packages-for-my-raspberry-pi.html'),
        ('Reference Page', '/pages/reference-page.html'),
        ('Vim Cheat Sheet', '/pages/vim-cheat-sheet.html'),)

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

# Specify the Pelican plugins to be used when formating content
PLUGIN_PATH = 'pelican-plugins/'
PLUGINS = ['latex', ]

# List of the extensions that the Markdown processor will use.
# The styles manni, emacs, native seem to work.
MD_EXTENSIONS = ['extra', 'codehilite(noclasses=True, pygments_style=manni, \
                 guess_lang=False)']

# code blocks with line numbers
#PYGMENTS_RST_OPTIONS = {'linenos': 'table'}

# Syntax highlighting style used by Pygment.  Supported styles are: autumn,
# borland, bw, colorful, default, emacs, friendly, fruity, manni, monokai,
# murphy, native, pastie, perldoc, solarizeddark, solarizedlight,
# tango, trac, vim, vs
# See http://pygments.org/demo/218030/?style=default
PYGMENTS_STYLE = 'default'

# Paths to find content from which it can be served
PATH = 'content'
PAGE_DIR = 'pages'
ARTICLE_DIR = 'articles'
ARTICLE_EXCLUDES = ('drafts', 'TBD',)

# List of directories to exclude when looking for pages.
PAGE_EXCLUDES = ('drafts', 'TBD',)

# Locations where files will be saved in output directory.
OUTPUT_PATH = 'output/'
PAGE_URL = 'pages/{slug}.html'
PAGE_SAVE_AS = 'pages/{slug}.html'
ARTICLE_URL = 'posts/{date:%Y}/{date:%b}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%b}/{date:%d}/{slug}/index.html'

CATEGORY_URL = "category/{slug}"
CATEGORY_SAVE_AS = "category/{slug}/index.html"

TAG_URL = "tag/{slug}/"
TAG_SAVE_AS = "tag/{slug}/index.html"

# Location of per-year and per-month archives of your posts
YEAR_ARCHIVE_SAVE_AS = 'archives/{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = 'archives/{date:%Y}/{date:%b}/index.html'

DEFAULT_PAGINATION = 10
PAGINATED_DIRECT_TEMPLATES = ('index',)
