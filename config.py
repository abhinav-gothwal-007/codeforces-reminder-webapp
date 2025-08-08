import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY            = os.getenv('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Mail
    MAIL_SERVER           = os.getenv('MAIL_SERVER')
    MAIL_PORT             = int(os.getenv('MAIL_PORT', 25))
    MAIL_USE_TLS          = os.getenv('MAIL_USE_TLS') == 'true'
    MAIL_USERNAME         = os.getenv('MAIL_USERNAME')
    MAIL_PASSWORD         = os.getenv('MAIL_PASSWORD')
    MAIL_DEFAULT_SENDER   = os.getenv('MAIL_DEFAULT_SENDER')
