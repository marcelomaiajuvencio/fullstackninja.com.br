#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Pedro Henrique Rodrigues'
SITENAME = 'FullStack Ninja'
SITEURL = 'http://fullstackninjaa.com.br'
CONTACT_EMAIL = '<email>'

PATH = 'content'

TIMEZONE = 'America/Sao_Paulo'

DEFAULT_DATE_FORMAT = '%d de %B de %Y'

# Default theme language.
I18N_TEMPLATES_LANG = 'pt_BR'
# Your language.
DEFAULT_LANG = 'pt_BR'
OG_LOCALE = 'pt_BR'
LOCALE = ('pt','bra', 'pt_BR')
LANGUAGE = 'pt_BR'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

RELATIVE_URLS = True

STATIC_PATHS = ['extra/CNAME', 'images']

EXTRA_PATH_METADATA = {
    'extra/CNAME': {'path': 'CNAME'}
}

# Plugins
PLUGIN_PATHS = ['./pelican-plugins']
PLUGINS = ['sitemap']

# Theme
THEME = 'theme'
DISPLAY_CATEGORIES_ON_MENU = True;

BROWSER_COLOR = '#333'
ROBOTS = 'index, follow'

#Config slugs
ARTICLE_URL = '{slug}/'
ARTICLE_SAVE_AS = '{slug}/index.html'
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'
AUTHOR_URL = 'autor/{slug}/'
AUTHOR_SAVE_AS = 'autor/{slug}/index.html'
CATEGORY_URL = 'categoria/{slug}/'
CATEGORY_SAVE_AS = 'categoria/{slug}/index.html'
TAG_URL = 'tag/{slug}/'
TAG_SAVE_AS = 'tag/{slug}/index.html'
ARCHIVES_URL = 'arquivo/'
ARCHIVES_SAVE_AS = 'arquivo/index.html'

# PAGINATED_DIRECT_TEMPLATES = ['archives']
PAGINATION_PATTERNS = (
    (1, '{base_name}/', '{base_name}/index.html'),
    (2, '{base_name}/page/{number}/', '{base_name}/page/{number}/index.html'),
)
DEFAULT_PAGINATION = 20
SUMMARY_MAX_LENGTH = 30

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}

DEFAULT_ADSENSE = {
	'adClientId' : '',
	'adSlot' : {
		'top_responsible' : '',
		'rside_300x600' : '',
		'bottom_responsible' : ''
	}
}

AUTHORS = {
    'Gustavo Furtado de Oliveira Alves': {
        'summary': 'É mestre em computação aplicada pelo Institudo Nacional de Pesquisas Espaciais, '+
                  'Engenheiro da Computação pela ETEP Faculdades e '+
                  'Técnico em Informática pela Escola Técnica Pandiá Calógeras. '+
                  'Possui as certificações SCJP-6, SCWCD-5 e ASF '+
                  'e trabalha com desenvolvimento de softwares desde 2007.',
        'image': '/images/author-gustavo.jpeg',
        'adsense': {
          'adClientId' : 'ca-pub-6041601556788047',
          'adSlot' : {
            'top_responsible' : '9578335779',
            'rside_300x600' : '3531802173',
            'bottom_responsible' : '7962001772'
          }
        }
    }
}