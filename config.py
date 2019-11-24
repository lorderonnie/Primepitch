class Config:
    '''
    This is the general configuration parent class
    '''
   



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