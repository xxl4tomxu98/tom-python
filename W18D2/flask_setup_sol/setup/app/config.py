import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or "key-for-devs"
    # we utilize os to get the enviornment variables for our application
    # here, we set our enviornment variables in our .flaskenv file
