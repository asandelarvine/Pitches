import os

class Config:
    '''
    General configuration parent class
    '''
    SECRET_KEY = 'TheDifference'
    SQLALCHEMY_DATABASE_URI = 'postgres://zniawonteukrvv:8397fa400f727b9abf77a2fa7fea8dcb90e4ba9da4db74b358a829ed8ad957db@ec2-54-147-207-184.compute-1.amazonaws.com:5432/desdivf220kn0v'
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    
    #  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587 
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'asandelarvine@gmail.com'
    MAIL_PASSWORD = 'chaviva2000'

    SUBJECT_PREFIX = 'Pitch-Zone'
    SENDER_EMAIL = 'asandelarvine@gmail.com'

    # simple mde  configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True

class TestConfig(Config):
     SQLALCHEMY_DATABASE_URI = 'postgres://zniawonteukrvv:8397fa400f727b9abf77a2fa7fea8dcb90e4ba9da4db74b358a829ed8ad957db@ec2-54-147-207-184.compute-1.amazonaws.com:5432/desdivf220kn0v'

class ProdConfig(Config):
    '''
    Production  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = 'postgres://zniawonteukrvv:8397fa400f727b9abf77a2fa7fea8dcb90e4ba9da4db74b358a829ed8ad957db@ec2-54-147-207-184.compute-1.amazonaws.com:5432/desdivf220kn0v'
    
class DevConfig(Config):
    '''
    Development  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    

    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}