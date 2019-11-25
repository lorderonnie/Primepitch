import os
class Config:
    '''
    This is the general configuration parent class
    '''
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://ronald:1645@localhost/primepitch' 
    SECRET_KEY='lorderonnie'
    UPLOADED_PHOTOS_DEST='app/static/photos'
    MAIL_SERVER='smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME='rontheking45@gmail.com'
    MAIL_PASSWORD='ronald1645'

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