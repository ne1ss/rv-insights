from dash.dependencies import Input, Output
from dash import html
import trades, sidebar_admin, posições_admin, Insights_admin, riscoRadar_admin
from dash import dcc
from src.app import *

def render_layout():

    layout = html.Div([
        dcc.Location(id='url-logado'),
        dbc.Row([
        dbc.Col(
                        [
                            sidebar_admin.render_layout()
                        ],
                        md=2
                    ),
            dbc.Col(
                        [
                            posições_admin.render_layout()
                        ],
                        id='advisor-content',md=10
                    )
            ])
        ])
    return layout

@app.callback(Output('advisor-content', 'children'), [Input('url', 'pathname')])
def render_advisor_content(pathname):
    if pathname == '/trades':
        return trades.render_layout()
    elif pathname == '/posicao':
        return posições_admin.render_layout()
    elif pathname == '/insights':
        return Insights_admin.render_layout_insights()
    elif pathname == '/riscoRadar':
        return riscoRadar_admin.render_layout_riscoRadar()



