import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'fsfsfwreqwrcqerct84vrtv'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///app.db' #ELE CRIA UMA PASTA CHAMADA INSTANCE
    SQLALCHEMY_TRACK_MODIFICATIONS = False