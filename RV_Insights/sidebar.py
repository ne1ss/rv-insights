
from dash import html
from dash.dependencies import Input, Output, State
from src.app import *

label = ['RRRP3', 'VALE3', 'PETR4', 'BBDC4']

ativos = [dbc.DropdownMenuItem(ativo) for ativo in label]

# === layout === #
def render_layout():
    layout = dbc.Col([
        dbc.Row([
            html.H1('RV Insight', className='text-warning'),
            html.Hr(),
            dbc.Button('Posições', href='/posicao', className="btn btn-outline-warning", color='Warning'),
            dbc.Button('Trades', href = '/trades', className="btn btn-outline-warning", color='Warning', style={'margin-top':'1px'}),

        ]),
    html.Div(style={'height':'64vh'}),

    dbc.Row([
                    dbc.Button('Mensagem', className="btn btn-outline-success", color='Warning', size='sm', id='open-modal-mensagem')
        ], align='baseline', justify='end'),

    #===Modal===#

    dbc.Modal([
            dbc.ModalHeader(dbc.ModalTitle('Mensagem', style={'color':'#e68a19'})),
            dbc.ModalBody([
                dbc.Row([
                    dbc.Col([
                        dbc.DropdownMenu(
                        label="Ativo",
                        children=ativos

                    )
                    ]),
                    dbc.Col([
                        dbc.Input(
                            placeholder="Parâmetros...", size="md", className="mb-3", style={'width':'45vh', 'margin-top':'4px'}, id='input-text'
                        )
                    ]),
                ]),

                dbc.Row([
                    dbc.Card(
                        dbc.CardBody(
                            [
                                html.H6("BBDC4", className="card-title"),
                                html.P(
                                    'Conforme a Research do BTG Pactual, continuamos otimistas com a nossa projeção de EBTIDA de ~R$ 15,5 bilhões para o ano, que está acima do consenso de mercado, e esperamos ver o consenso atualizando os números nos próximos meses. Esta é uma das teses mais baratas em nossa cobertura de Mineração & Siderurgia, negociando a 3,3x EV/EBTIDA 23. A recomendação é de COMPRA.',
                                    className="card-text",
                                ),
                                html.H6("ESTRUTURA", className="card-title"),
                                html.P(
                                    className="card-text",
                                    id='card-text-estrutura'
                                )

                            ]
                        ),
                    )


                ])




        ])
    ],id='modal-gerar-mensagem')], id='sidebar_completa', style={'border':'#171616','border-radius': '5px'})
    return layout

@dash_app.callback(
    Output('modal-gerar-mensagem', 'is_open'),
    Input('open-modal-mensagem', 'n_clicks'),
    State('modal-gerar-mensagem', 'is_open')
)
def toggle_modal(n1, is_open):
    if n1:
        return not is_open



@dash_app.callback(
    Output("card-text-estrutura", "children"),
    Input("input-text", "value"),
)
def update_card_content(input_value):
    return input_value



