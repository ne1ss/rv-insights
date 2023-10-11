from dash import dash_table
from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
import locale

df = pd.read_excel('assets/dados_datatable_insights.xlsx')
df['CONTA'] = df['CONTA'].astype(str)
fig = px.bar(df[df['Operação'] != 'SEM'], x='ATIVO', y='NOTIONAL')
fig2 = px.bar(df[df['Operação'] != 'SEM'].sort_values(by=['NOTIONAL']).tail(5), x='CONTA', y='NOTIONAL')
fig.update_layout(
    xaxis_title='',
    yaxis_title='',
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='rgba(0,0,0,0)',
    font=dict(color='white'),
    margin=dict(l=1,t=1,b=1,r=1)

)

fig.update_traces(marker_color='orange')
fig2.update_layout(
    xaxis_title='',
    yaxis_title='',
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='rgba(0,0,0,0)',
    font=dict(color='white'),
    margin=dict(l=1,t=1,b=1,r=1)

)
fig2.update_traces(marker_color='orange')

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
sum_notional = locale.currency(df[df['Operação'] != 'SEM']['NOTIONAL'].sum(), grouping=True, symbol=None)
sum_fee = locale.currency(df[df['Operação'] != 'SEM']['FEE '].sum(), grouping=True, symbol=None)
count_cpf = len(df[df['Operação'] != 'SEM']['CONTA'].unique())

df[' %'] = df[' %']*100


df['PM'] = 'R$' + ' ' + df['PM'].apply(lambda x: locale.currency(x, grouping=True, symbol=None))
df['SPOT'] ='R$' + ' ' + df['SPOT'].apply(lambda x: locale.currency(x, grouping=True, symbol=None))
df['NOTIONAL'] = 'R$' + ' ' + df['NOTIONAL'].apply(lambda x: locale.currency(x, grouping=True, symbol=None))
df['FEE '] = 'R$' + ' ' + df['FEE '].apply(lambda x: locale.currency(x, grouping=True, symbol=None))


# =========  Layout  =========== #

def render_layout():
    layout = dbc.Col([
        dbc.Row([
            html.H3('Posições', className="text-primary"),

            html.Div(
                dash_table.DataTable(
                            id='datatable-interactivity',
                            columns=[
                                {"name": i, "id": i, "deletable": False, "selectable": False, "editable": False} for i in df.columns
                            ],
                            data=df[df['Operação'] != 'SEM'].round(2).to_dict('records'),
                            filter_action = 'native',
                            filter_options={"placeholder_text": "..."},
                            editable=False,
                            page_size=4,
                            style_data_conditional=(
                                [
                                    {
                                        'if': {
                                            'filter_query': '{ %}<0',
                                            'column_id': ' %'
                                        },
                                        'color': '#db0211',
                                        'fontWeight': 'bold'

                                    },
                                    {
                                        'if': {
                                            'filter_query': '{ %}>0',
                                            'column_id':' %'
                                        },
                                        'color': '#247d04',
                                        'fontWeight': 'bold'
                                    }

                                ]

                            ),
                            style_header={
                                    'backgroundColor': 'rgb(20, 20, 20)',
                                    'color': 'orange',
                                    'textAlign': 'center'
                            },
                            style_data={
                                    'backgroundColor': 'rgba(0, 0, 0,0)',
                                    'color': '#e68a19',


                            },
                            style_as_list_view=True,
                            style_cell={'whiteSpace': 'normal','border': '1px solid black','padding': '8px','fontFamily': 'Arial, sans-serif', 'textAlign':'center'},
                            style_filter = {
                            'backgroundColor': 'grey',
                            'color': 'white'},
                            css=[{
                                'selector': '.select-page input',
                                'rule': 'display: none;'  # Ajuste o tamanho da caixa e da fonte
                            }, {
                                'selector': '.previous-page, .next-page, .first-page, .last-page',
                                'rule': 'font-size: 10px;'  # Ajuste o tamanho da fonte dos botões de página
                            }]

                )
            )
        ], style={'height':'55vh'}),
        dbc.Row([
            dbc.Col([


                dcc.Graph(
                    id='bar-graph-posições',
                    figure=fig,
                    style={'height': '45vh','border': 'rgba(0,0,0,0)', 'border-radius': '5px'},
                    config= {'displaylogo': False, 'displayModeBar': False}
                )
            ], md=5),
            dbc.Col([

                dcc.Graph(
                    id='bar-graph-posições2',
                    figure=fig2,
                    style={'height': '45vh', 'border': 'rgba(0,0,0,0)', 'border-radius': '5px'},
                    config= {'displaylogo': False,'displayModeBar': False}
                )

            ], md=5),
            dbc.Col([
                dbc.ListGroup(
                    [
                        dbc.ListGroupItem('Notional', style={'color': '#e68a19'}),
                        dbc.ListGroupItem('R$ '+sum_notional),
                        dbc.ListGroupItem('Fee', style={'color': '#e68a19'}),
                        dbc.ListGroupItem('R$ '+sum_fee),
                        dbc.ListGroupItem('CPFs', style={'color': '#e68a19'}),
                        dbc.ListGroupItem(str(count_cpf))
                    ],
                    flush=True,
                ),

            ], md=2)
        ])
    ])
    return layout
# =========  Callbacks  =========== #
# Tabela
