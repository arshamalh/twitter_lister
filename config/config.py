from os import environ
from dotenv import dotenv_values

config = {
    **dotenv_values(".env"),  # load shared development variables
    **environ,  # override loaded values with environment variables
}

def get_config(key, default=None):
    return config.get(key, default)
