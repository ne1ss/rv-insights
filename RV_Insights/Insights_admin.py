from dash import html
from src.app import *

abas_insight = ['P.E.','SWING']
def create_tab_content_position(aba):
    if aba == 'P.E.':
        return [
            dbc.Row([

            ], style={'margin-top':'10px'})
        ]
    else:
        return [
            dbc.Row([

            ], style={'margin-top': '10px'})
        ]
tabs_insights = [dbc.Tab(create_tab_content_position(aba), label=aba, label_style={'color':'#e68a19'}) for aba in abas_insight]

def render_layout_insights():
    layout = html.Div([
            html.H3('Insights', className="text-primary"),
            dbc.Tabs(tabs_insights)
    ], style={'margin-left':'10px'})
    return layout