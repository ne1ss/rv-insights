from dash import html
from dash.dependencies import Input, Output, State
from src.app import *
from werkzeug.security import check_password_hash
from flask_login import login_user
from dash.exceptions import PreventUpdate


card_style = {
    'width': '300px',
    'min-height': '25px',
    'padding-top': '25px',
    'padding-right': '25px',
    'padding-left': '25px',
    'margin-left': '12vh',
    'margin-bottom': '25vh'
}


def render_layout(message):
    message = 'Login ou senha incorretos' if message == 'error' else message
    login = dbc.Card([
        html.Legend('RV Insight', className='text-warning'),
        dbc.Input(id='user_login', placeholder='Username', type='text'),
        dbc.Input(id='pwd_login', placeholder='Password', type='password', style={'margin-top': '5px'}),
        dbc.Button('Login', id='login_button', style={'margin-top': '10px','margin-bottom':'10px'}, color='Warning',
                   className="btn btn-outline-warning"),
        html.Span(message, style={'text-allign': 'center'})

    ], style=card_style)

    layout = dbc.Container(
        dbc.Row(
            dbc.Col(login, width=4, className="mx-auto"),
            className="align-items-center vh-100"
        ),
        fluid=True,
    )

    return layout


@app.callback(
    Output('login-state', 'data'),
    Input('login_button', 'n_clicks'),
    [
        State('user_login', 'value'),
        State('pwd_login', 'value')
    ]
)
def successful(n_clicks, username, password):
    if n_clicks is None:
        raise PreventUpdate
    user = MyUsers.query.filter_by(username=username).first()
    if user and password is not None:
        if check_password_hash(user.password, password):
            login_user(user)
            return 'success'

        else:

            return 'error'
    else:
        return 'error'

