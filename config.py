import os
class Config:
    '''
    This is the general configuration parent class
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://ronald:1645@localhost/primepitch' 
    SECRET_KEY = 'lorderonnie'


class ProdConfig(Config):
    '''
    Parental production  configuration child class
    '''
    pass


class DevConfig(Config):
    '''
     The development  configuration child class
    '''

    DEBUG = True
    
config_options = {
'development':DevConfig,
'production':ProdConfig
}