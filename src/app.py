import dash
import dash_bootstrap_components as dbc
import configparser
from flask_login import UserMixin
import os
from create_database import *

config = configparser.ConfigParser()

dash_app = dash.Dash(__name__,server=app, external_stylesheets=[dbc.themes.SLATE],suppress_callback_exceptions=True)

server = app.server

app.config.update(
    SECRET_KEY=os.urandom(12),
    SQLALCHEMY_TRACK_MODIFICATIONS=False
)


class MyUsers(UserMixin, Users):
    pass
