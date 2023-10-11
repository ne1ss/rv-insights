from dash import html, dcc
from dash.dependencies import Input, Output, State
from flask_login import current_user
from src.app import *
import login, advisor_page

login_manager = LoginManager()
login_manager.init_app(app)
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
    with app.app_context():
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
    app.run_server(port=8051, debug=True)

