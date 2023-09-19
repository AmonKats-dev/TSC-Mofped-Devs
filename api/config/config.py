import os
from decouple import config
from datetime import timedelta
class Config:
    SECRET_KEY=config('SECRET_KEY','secret')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(minutes=30)
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(minutes=30)
    JWT_SECRET_KEY=config('JWT_SECRET_KEY','jwt_secret')
class DevConfig(Config):
    DEBUG = config('DEBUG',cast=bool)
    SQLALCHEMY_ECHO  = True
    SQLALCHEMY_DATABASE_URI = 'mysql://root:@localhost/helpdesk_db'
class TestConfig(Config):
    pass
class ProdConfig(Config):
    pass

Config_dict={
    'dev':DevConfig,
    'prod':ProdConfig,
    'test':TestConfig
}