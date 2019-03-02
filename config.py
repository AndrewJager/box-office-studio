import os

class BaseConfig(object):
    DEBUG = False
    SECRET_KEY = '39qhfpq948hgqpcma;lkda;noivcnaoeruivbpe4ouvuqbp'
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']


class DevelopmentConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    DEBUG = False