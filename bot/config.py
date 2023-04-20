import os import environ

class Config:

    BOT_TOKEN = environ['BOT_TOKEN']

    SESSION_NAME = environ['SESSION_NAME']

    API_ID = environ['API_ID']

    API_HASH = environ['API_HASH']

    CLIENT_ID = environ['CLIENT_ID']

    CLIENT_SECRET = CLIENT_SECRET']

    AUTH_USERS = list({int(x) for x in environ.get("AUTH_USERS", "").split()})

    VIDEO_DESCRIPTION = environ['VIDEO_DESCRIPTION']

    VIDEO_CATEGORY = environ['VIDEO_CATEGORY']

    VIDEO_TITLE_PREFIX = environ['VIDEO_TITLE_PREFIX']

    VIDEO_TITLE_SUFFIX = environ['VIDEO_TITLE_SUFFIX']
    
    DEBUG = bool()

    UPLOAD_MODE = environ['UPLOAD_MODE']
    
    CRED_FILE = "auth_token.txt"
