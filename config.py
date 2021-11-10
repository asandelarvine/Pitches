import os

class Config:
    '''
    General configuration parent class
    '''
    SECRET_KEY = 'TheDifference'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://access:monkey@localhost/pitches1'
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
     SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://access:monkey@localhost/pitches_test1'

class ProdConfig(Config):
    '''
    Production  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://access:monkey@localhost/pitches1'
    
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