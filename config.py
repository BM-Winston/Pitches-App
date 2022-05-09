import os

class Config:
    SQLALCHEMY_DATABASE_URI =



class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True

config_options = {
    'development':DevConfig,
    'production':ProdConfig,

}