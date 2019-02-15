import os
from app.api_2.models.connection import connection

class Config:


    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True
    DB_NAME = os.getenv('DATABASE_NAME')
    SECRET_KEY = os.getenv('SECRET_KEY', 'my_precious')

class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    DATABASE_NAME = os.getenv('DATABASE_TEST_NAME')
    SECRET_KEY = os.getenv('SECRET_KEY', 'my_precious')

class ProductionConfig(Config):
    pass


config = {
    'development' : DevelopmentConfig,
    'testing' : TestingConfig,
    'production' : ProductionConfig,

    'default' : DevelopmentConfig,
}
