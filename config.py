import os
import ProxyCloud
# Bot
BOT_TOKEN = '5954082825:AAE6EFqMAmk3SJTfdKcTMu7nYsnEHvlZ8dY'
TG_API_ID = '9902519'
TG_API_HASH = '9d8097d05bbc90a6ed2a7a81abcd4e8a'
TG_ADMIN = 'Abolanos3'
TG_USER = 'Abolanos3'
# Database
DB_LOCAL = False
DB_HOST = 'sql.freedb.tech'
DB_HOST_USERNAME = 'freedb_hiyabo'
DB_HOST_PASSWORD = '?vj&ZrZhGu5txSW'
DB_NAME = 'freedb_educaDb'

if DB_LOCAL:
    # Database Local
    DB_HOST = ''
    DB_HOST_USERNAME = ''
    DB_HOST_PASSWORD = ''
    DB_NAME = 'clutilprodb'
