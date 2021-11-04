import cloudinary
from os import getenv

cloudinary.config(
    cloud_name = getenv('CLOUD_NAME'),
    api_key = getenv('API_KEY'),
    api_secret = getenv('API_SECRET')
)