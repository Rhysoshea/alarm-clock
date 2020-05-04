import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or '7d441f27d441f27567d441f2b6176a'