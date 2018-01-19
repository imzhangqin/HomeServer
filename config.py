# config for hs

import os
from flask_appbuilder.security.manager import AUTH_OID, AUTH_REMOTE_USER, AUTH_DB, AUTH_LDAP, AUTH_OAUTH
basedir = os.path.abspath(os.path.dirname(__file__))

SECRET_KEY = 'testhomeserver'
DEBUG = True
# BCRYPT_LOG_ROUNDS = 13
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data', 'hs.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False
# Flask-WTF flag for CSRF
CSRF_ENABLED = True

#------------------------------
# APP Builder config
#------------------------------
APP_NAME = "HS"
#APP_ICON = "static/img/logo.jpg"
AUTH_TYPE = AUTH_DB
AUTH_ROLE_ADMIN = 'Admin'
#AUTH_ROLE_PUBLIC = 'Public'
AUTH_USER_REGISTRATION = True
AUTH_USER_REGISTRATION_ROLE = "Public"

# Uncomment to setup OpenID providers example for OpenID authentication
#OPENID_PROVIDERS = [
#    { 'name': 'Yahoo', 'url': 'https://me.yahoo.com' },
#    { 'name': 'AOL', 'url': 'http://openid.aol.com/<username>' },
#    { 'name': 'Flickr', 'url': 'http://www.flickr.com/<username>' },
#    { 'name': 'MyOpenID', 'url': 'https://www.myopenid.com' }]
#---------------------------------------------------
# Babel config for translations
#---------------------------------------------------
# Setup default language
BABEL_DEFAULT_LOCALE = 'en'
BABEL_DEFAULT_FOLDER = 'translations'
LANGUAGES = {
    'en': {'flag':'gb', 'name':'English'},
    # 'pt': {'flag':'pt', 'name':'Portuguese'},
    # 'pt_BR': {'flag':'br', 'name': 'Pt Brazil'},
    # 'es': {'flag':'es', 'name':'Spanish'},
    # 'de': {'flag':'de', 'name':'German'},
    'zh': {'flag':'cn', 'name':'Chinese'},
    # 'ru': {'flag':'ru', 'name':'Russian'},
    # 'pl': {'flag':'pl', 'name':'Polish'}
}
#---------------------------------------------------
# Image and file configuration
#---------------------------------------------------
# The file upload folder, when using models with files
UPLOAD_FOLDER = basedir + '/app/static/uploads/'

# The image upload folder, when using models with images
IMG_UPLOAD_FOLDER = basedir + '/app/static/uploads/'

# The image upload url, when using models with images
IMG_UPLOAD_URL = '/static/uploads/'
# Setup image size default is (300, 200, True)
#IMG_SIZE = (300, 200, True)

# Theme configuration
# these are located on static/appbuilder/css/themes
# you can create your own and easily use them placing them on the same dir structure to override
#APP_THEME = "bootstrap-theme.css"  # default bootstrap
#APP_THEME = "cerulean.css"
#APP_THEME = "amelia.css"
#APP_THEME = "cosmo.css"
#APP_THEME = "cyborg.css"
#APP_THEME = "flatly.css"
#APP_THEME = "journal.css"
#APP_THEME = "readable.css"
#APP_THEME = "simplex.css"
#APP_THEME = "slate.css"
#APP_THEME = "spacelab.css"
#APP_THEME = "united.css"
#APP_THEME = "yeti.css"
