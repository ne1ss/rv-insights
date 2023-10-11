from dash import html


def render_layout_riscoRadar():
    layout = html.Div([
            html.H3('Risco Radar', className="text-primary"),
    ], style={'margin-left':'10px'})
    return layout