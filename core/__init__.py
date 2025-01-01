# from flask import Flask
# from decouple import config
# from flask_restx import Api

# app = Flask(__name__)
# app.config.from_object(config("APP_SETTINGS"))
# api = Api(
#     app,
#     version='1.0',
#     title='Horoscope API',
#     description='Get horoscope data easily using the below APIs',
#     license='MIT',
#     contact='bhavina',
#     contact_email='bhavina.sk.2024@gmail.com',
#     doc='/',
#     prefix='/api/v1'
# )

# from core import routes

from flask import Flask
from decouple import config
from flask_restx import Api

app = Flask(__name__)
app.config.from_object(config("APP_SETTINGS"))

# Initialize API
api = Api(
    app,
    version='1.0',
    title='Horoscope API',
    description='Get horoscope data easily using the below APIs',
    license='MIT',
    contact='bhavina',
    contact_email='bhavina.sk.2024@gmail.com',
    doc='/',
    prefix='/api/v1'
)

# Routes will be registered here
from core import routes

# If running locally, app.run() will not be used in Vercel deployments
# Avoid app.run() in serverless environments (Vercel will automatically manage this)
