class Config(object):
    POSTS_PER_PAGE = 10


class ProdConfig(Config): 
    SECRET_KEY = "U\x16\xc6>\xb9*\r'R\xae\x1a\xd1]\xbc\x1cx\x00`\x12\x93\xbb\x1ff/"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'


class DevConfig(Config): 
    DEBUG = True
    SECRET_KEY = 'Y\x8ek\x88\xb1\xc50\x9b\x11Z\xfbg\x02\x0c\xb0*\xb2r\x10\xa8\x9c\x0e\x84!'
    SQLALCHEMY_DATABASE_URI = "sqlite:///database.db"
    SQLALCHEMY_ECHO = True

