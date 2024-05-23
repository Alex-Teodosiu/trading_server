from flask import Flask
from flask_bcrypt import Bcrypt
from flask_restx import Api
from flask_jwt_extended import JWTManager
from .config import Config
from .routes import initialize_routes  # Import the function to initialize your routes
import os

# declaring flask application
app = Flask(__name__)

# calling the dev configuration
config = Config()
app.config.from_object(config.dev_config)

# load the secret key defined in the .env file
app.secret_key = os.environ.get("SECRET_KEY")
bcrypt = Bcrypt(app)

# Setup the Flask-JWT-Extended extension
jwt = JWTManager(app)

# Create API instance
api = Api(app, doc='/')  # Swagger documentation will be at /documentation

# Initialize routes
initialize_routes(api)
