import dash
import dash_bootstrap_components as dbc
import configparser
from flask_login import UserMixin, LoginManager
import os
from dash import html, dcc
from dash.dependencies import Input, Output, State
from flask_login import current_user
from src.create_database import *


config = configparser.ConfigParser()

app = dash.Dash(__name__,server=flask_app, external_stylesheets=[dbc.themes.SLATE],suppress_callback_exceptions=True)

server = app.server

server.config.update(
    SECRET_KEY=os.urandom(12),
    SQLALCHEMY_TRACK_MODIFICATIONS=False
)

# ==== layout ==== #


app.layout = dbc.Container(

    [
        dbc.Row(
            [
                dcc.Store(id='login-state', data=''),
                dcc.Location(id='url'),
                html.Div([
                ], id='page-content')

            ])

    ],
    fluid=True
)

class MyUsers(UserMixin, Users):
    pass

