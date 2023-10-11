from dash import html
import dash_bootstrap_components as dbc

# =========  Layout  =========== #
labels = ['RRRP3', 'VALE3', 'PETR4', 'BBDC4']


def create_tab_content(label):
    return dbc.Container([
        dbc.Card(
        dbc.CardBody([
        html.P(f'{label}', className="card-text")
        ]),className="mt-3")]
    ,className="mt-4")

tabs = [dbc.Tab(create_tab_content(label), label=label,label_style={'color':'#e68a19'}) for label in labels]


def render_layout():
    layout = dbc.Col([
        dbc.Row([
            html.H3('Trades', className="text-primary"),
            html.Div(id='tabela-despesas'),
            dbc.Tabs(tabs),
           ])
    ])
    return layout
# =========  Callbacks  =========== #
