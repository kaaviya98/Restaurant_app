from .base import *
import environ


env = environ.Env()
environ.Env.read_env()

DEBUG = True

DATABASES = {
    "default": {
        "ENGINE": env("DATABASE_ENGINE"),
        "NAME": env("DATABASE_NAME"),
        "USER": env("DATABASE_USER"),
        "PASSWORD": env("DATABASE_PASSWORD"),
        "HOST": env("HOST"),
        "PORT": env("PORT"),
    }
}
