import dash
import dash_bootstrap_components as dbc
import configparser
from flask_login import UserMixin, LoginManager
import os
from src.create_database import *
from dash import html, dcc
from dash.dependencies import Input, Output, State
from flask_login import current_user
from src.create_database import *
import login, advisor_page

config = configparser.ConfigParser()

app = dash.Dash(__name__,server=flask_app, external_stylesheets=[dbc.themes.SLATE],suppress_callback_exceptions=True)

server = app.server

server.config.update(
    SECRET_KEY=os.urandom(12),
    SQLALCHEMY_TRACK_MODIFICATIONS=False
)


class MyUsers(UserMixin, Users):
    pass
login_manager = LoginManager()
login_manager.init_app(flask_app)
login_manager.login_view = '/'


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


@login_manager.user_loader
def load_user(user_id):
    with flask_app.app_context():
        return db.session.get(MyUsers, int(user_id))

@app.callback(Output('url', 'pathname'),
              [
                  Input('login-state','data'),
              ])
def render_page_content(login_state):
    ctx = dash.callback_context
    if ctx.triggered:
        trigg_id = ctx.triggered[0]['prop_id'].split('.')[0]
        if trigg_id == 'login-state' and login_state == 'success':
            return '/posicao'
        if trigg_id == 'login-state' and login_state == 'error':
            return '/'



@app.callback(Output('page-content', 'children'), [Input('url', 'pathname'), State('login-state','data')])
def render_content(pathname, login_state):
    if pathname == '/':
        return login.render_layout(login_state)
    else:
        if current_user.is_authenticated and current_user.username != 'Ariel':
         return advisor_page.render_layout()




if __name__ == "__main__":
    app.run_server(debug=True)