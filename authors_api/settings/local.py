from .base import *
from .base import env

SECRET_KEY = env("DJANGO_SECRET_KEY",
   default="fkrhmDq-pJIY_dQTk19wQjNXesJu6zM9ox4NUQ34-A3nEOH-VTw"
)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

CSRF_TRUSTED_ORIGINS = ["http://localhost:8080"]