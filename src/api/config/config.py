class Config(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOAD_FOLDER = 'images'


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root@localhost:3306/author-manager"


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root@localhost:3306/author-manager"
    SQLALCHEMY_ECHO = False
    JWT_SECRET_KEY = "secret key"
    SECRET_KEY = 'your_secured_key_here'
    SECURITY_PASSWORD_SALT = 'your_security_password_here'
    MAIL_DEFAULT_SENDER = 'your_email_address'
    MAIL_SERVER = 'email_providers_smtp_address'
    MAIL_PORT = 1234  # <mail_server_port>
    MAIL_USERNAME = 'your_email_address'
    MAIL_PASSWORD = 'your_email_password'
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True


class TestingConfig(Config):
    TESTING = True
    # SQLALCHEMY_DATABASE_URI = "sqlite:///test.db"
    SQLALCHEMY_ECHO = False
    JWT_SECRET_KEY = 'JWT-SECRET'
    SECRET_KEY = 'SECRET-KEY'
    SECURITY_PASSWORD_SALT = 'PASSWORD-SALT'
    MAIL_DEFAULT_SENDER = ''
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USERNAME = ''
    MAIL_PASSWORD = ''
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
