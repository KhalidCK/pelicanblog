# Theme-specific settings
SITENAME = 'Tech exploration'
DOMAIN = 'khalidck.fr'
BIO_TEXT = 'KhalidCK - Devops stories'
FOOTER_TEXT = 'Powered by <a href="http://getpelican.com">Pelican</a>'
THEME='pneumatic'

SITE_AUTHOR = 'Khalid CK'
TWITTER_USERNAME = ''
GOOGLE_PLUS_URL = ''
INDEX_DESCRIPTION = 'Blog on devops topics - KhalidCK'

SIDEBAR_LINKS = []

ICONS_PATH = 'images/icons'

SOCIAL_ICONS = [
    ('https://github.com/khalidck', 'GitHub', 'fa-github'),
    ('https://www.linkedin.com/in/khalid-chakhmoun-83876033', 'LinkedIN', 'fa-linkedin'),
]


# Pelican settings
RELATIVE_URLS = True
SITEURL = 'https://khalidck.fr'
TIMEZONE = 'Europe/Paris'
DEFAULT_DATE = 'fs'
DEFAULT_DATE_FORMAT = '%-d %B %Y'
DEFAULT_PAGINATION = False
SUMMARY_MAX_LENGTH = 42

ARTICLE_URL = '{date:%Y}/{date:%m}/{slug}/'
ARTICLE_SAVE_AS = ARTICLE_URL + 'index.html'

PAGE_URL = '{slug}/'
PAGE_SAVE_AS = PAGE_URL + 'index.html'

ARCHIVES_SAVE_AS = 'archive/index.html'
YEAR_ARCHIVE_SAVE_AS = '{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = '{date:%Y}/{date:%m}/index.html'

# Disable authors, categories, tags, and category pages
DIRECT_TEMPLATES = ['index', 'archives']
CATEGORY_SAVE_AS = ''

# Disable Atom feed generation
FEED_ATOM = 'atom.xml'
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

TYPOGRIFY = True

MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.admonition': {},
        'markdown.extensions.codehilite': {'linenums': None},
        'markdown.extensions.extra': {},
    },
    'output_format': 'html5',
}

CACHE_CONTENT = False
DELETE_OUTPUT_DIRECTORY = True
OUTPUT_PATH = 'develop'
PATH = 'content'

templates = ['404.html']
TEMPLATE_PAGES = {page: page for page in templates}

STATIC_PATHS = ['images', 'files', 'extra']
IGNORE_FILES = ['.DS_Store', 'pneumatic.scss', 'pygments.css']

extras = ['CNAME', 'favicon.ico', 'keybase.txt', 'robots.txt']
EXTRA_PATH_METADATA = {'extra/%s' % file: {'path': file} for file in extras}

PLUGIN_PATHS = ['plugins']
PLUGINS = ['assets', 'neighbors', 'render_math']
ASSET_SOURCE_PATHS = ['static']
ASSET_CONFIG = [
    ('cache', False),
    ('manifest', False),
    ('url_expire', False),
    ('versions', False),
]
