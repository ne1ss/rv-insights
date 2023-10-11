# =========  Callbacks  =========== #
from dash import dash_table
from dash import dcc
from dash import html
import pandas as pd
import plotly.express as px
from dash.dash_table import FormatTemplate
from src.app import *
from dash.dependencies import Input, Output

df_custodia = pd.read_excel('assets/custódiaf5.xlsx')
df_setores = pd.read_excel('assets/Setores.xlsx')

setores = []
for ativo in df_custodia['ATIVO'].to_list():
    if ativo in df_setores['Ativo'].to_list():
        setores.append(df_setores[df_setores['Ativo']==ativo].iloc[0,1])
    else:
        setores.append('-')


df_custodia.insert(2, 'SETOR', setores)
df_custodia['CONTA'] = df_custodia['CONTA'].astype(str)

fig = px.bar(df_custodia.sort_values(by=['NOTIONAL']).tail(5), x='ATIVO', y='NOTIONAL')
fig2 = px.bar(df_custodia.sort_values(by=['NOTIONAL']).tail(5), x='SETOR', y='NOTIONAL')
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

sum_notional = df_custodia[df_custodia['SETOR']!='-']['NOTIONAL'].sum()
sum_notional_livre = df_custodia[df_custodia['SETOR']!='-']['NOTIONAL LIVRE'].sum()
count_cpf = len(df_custodia[df_custodia['SETOR']!='-']['CONTA'].unique())


# =========  Layout  =========== #


def col_format(i,x):
    col_list = []
    for i in x.columns:
        monetary_cols = ['PM', 'SPOT','NOTIONAL', 'NOTIONAL LIVRE']
        perc_cols = ['%', 'PERF% MÉDIA','% BLOCK']
        if i in monetary_cols:
            col_list.append({'name': i, 'id': i, 'type': 'numeric', 'format': FormatTemplate.money(2), 'deletable': False, 'selectable': False, 'editable': False})
        elif i in perc_cols:
            col_list.append({'name': i, 'id': i, 'type': 'numeric','format': FormatTemplate.percentage(2), 'deletable': False, 'selectable': False, 'editable': False})
        else:
            col_list.append({'name': i, 'id': i, 'deletable': False, 'selectable': False, 'editable': False})
    return col_list

cols = col_format(df_custodia.columns, df_custodia)


abas = ['Custódia','Dinâmica']

dados_pivot = [df_custodia.columns.to_list()]

for index, row in df_custodia.iterrows():
    dados_pivot.append(row.to_list())

def create_tab_content_position(aba):
    if aba == 'Custódia':
        return  [
            dbc.Row([
                dash_table.DataTable(
                            id='datatable-interactivity',
                            columns=cols,
                            data=df_custodia.round(2).to_dict('records'),
                            filter_action = 'native',
                            sort_action = 'native',
                            filter_options={"placeholder_text": "..."},
                            style_table={'overflowX':'scroll'},
                            editable=False,
                            style_data_conditional=(
                                [
                                    {
                                        'if': {
                                            'filter_query': '{%}<0',
                                            'column_id': '%'
                                        },
                                        'color': '#db0211',
                                        'fontWeight': 'bold',

                                    },
                                    {
                                        'if': {
                                            'filter_query': '{%}>0',
                                            'column_id':'%'
                                        },
                                        'color': '#247d04',
                                        'fontWeight': 'bold'
                                    },
                                    {
                                        'if': {'column_id': 'SQUAD'},
                                        'whiteSpace': 'nowrap',
                                        'overflow': 'hidden',
                                        'width':'100px'
                                    },


                                ]

                            ),
                            style_header={
                                    'backgroundColor': 'rgb(20, 20, 20)',
                                    'color': 'orange',
                                    'textAlign': 'center'
                            },
                            style_data={
                                    'backgroundColor': 'white',
                                    'color': 'black',


                            },
                            style_as_list_view=True,
                            style_cell={'border': '1px solid black','fontFamily': 'Arial, sans-serif', 'textAlign':'center','width':'auto', 'overflow':'hidden','padding':'5px','fontSize':'12px'},
                            style_filter = {
                            'backgroundColor': '#d3d3d3',
                            'color': 'black',
                            'fontWeight': 'bold',
                            'textAlign': 'left'},
                            css=[{
                                'selector': '.select-page input',
                                'rule': 'display: none;'  # Ajuste o tamanho da caixa e da fonte
                            }, {
                                'selector': '.previous-page, .next-page, .first-page, .last-page',
                                'rule': 'font-size: 10px;'  # Ajuste o tamanho da fonte dos botões de página
                            }]

                )
            ], style={'margin-top':'10px'})
    ]
    else:
        return [
            dbc.Row([
                html.Div([
                    html.H6('Selecionar índice', className='text-warning'),
                    dcc.Dropdown(['AAI RV', 'VERTICAL', 'SQUAD','ALOCAÇÃO', 'ATIVO','CONTA'], id='input-dinamica-position', style={'width':'150px'})
                ], style={'margin-left':'10px','margin-top':'10px'})
            ]),
            dbc.Row([
                dbc.Col(
                id='datatable-dinâmica', style={'margin-top':'10px'}
                )
            ])
        ]


tabs_position = [dbc.Tab(create_tab_content_position(aba), label=aba, label_style={'color':'#e68a19'}) for aba in abas]

def render_layout():
    layout = html.Div([
            html.H3('Posições', className="text-primary"),
            dbc.Tabs(tabs_position)
    ], style={'margin-left':'10px'})
    return layout


@app.callback(
    Output('datatable-dinâmica', 'children'),
    Input('input-dinamica-position', 'value')
)
def dinamica_render_layout(input):
    if input is None:
        return None
    else:
        if input not in ['CONTA', 'ATIVO']:

            df_custodia_limpo = df_custodia[df_custodia['SETOR'] != '-']
            pm_mean_dict = {}

            for ativo in df_custodia_limpo['ATIVO'].unique():
                df_ativo = df_custodia_limpo[df_custodia_limpo['ATIVO'] == ativo]
                pm_mean_dict.update({ativo: round(df_ativo['PM'].dropna().mean(), 2)})
                df_custodia_limpo.loc[df_custodia_limpo['ATIVO'] == ativo, 'PM'] = \
                df_custodia_limpo[df_custodia_limpo['ATIVO'] == ativo]['PM'].fillna(value=pm_mean_dict[ativo]).replace(0, pm_mean_dict[ativo])

            df_custodia_limpo.loc['%'] = (df_custodia_limpo['PM'] - df_custodia_limpo['SPOT']) / df_custodia_limpo['PM']
            df_custodia_limpo = df_custodia_limpo.iloc[:-1]
            df_custodia_limpo.loc['%'] = (df_custodia_limpo['PM'] - df_custodia_limpo['SPOT']) / df_custodia_limpo['PM']

            df_investido = df_custodia_limpo['PM'] * df_custodia_limpo['QTD ']
            df_spot = df_custodia_limpo['SPOT'] * df_custodia_limpo['QTD ']
            df_custodia_limpo.insert(4, '$ INVESTIDO', df_investido)
            df_custodia_limpo.insert(6, '$ SPOT', df_spot)

            df_input = df_custodia.groupby(input).sum()[['NOTIONAL', 'NOTIONAL LIVRE']].reset_index()
            df_input.rename({'ATIVO':'COUNT Nº ATIVOS'})
            count_list_cpf = []
            count_list_ativos = []
            mean_perf_list = []

            for x in df_input[input].to_list():
                count_list_cpf.append(df_custodia[df_custodia[input] == x]['CONTA'].unique().size)
                count_list_ativos.append(df_custodia[df_custodia[input] == x]['ATIVO'].unique().size)
                df = df_custodia_limpo.loc[df_custodia_limpo[input] == x, ['$ INVESTIDO', '$ SPOT', 'CONTA']].groupby('CONTA').sum().reset_index()
                df['%'] = (df['$ INVESTIDO'] - df['$ SPOT']) / df['$ SPOT']
                mean_perf_list.append(df['%'].dropna().mean())

            df_input['% BLOCK'] = (df_input['NOTIONAL'] - df_input['NOTIONAL LIVRE']) / df_input['NOTIONAL']
            df_input.insert(4, 'COUNT CPF', count_list_cpf)
            df_input.insert(5, 'COUNT Nº ATIVOS', count_list_ativos)
            df_input.insert(6, 'PERF% MÉDIA', mean_perf_list)

            print(df_input.columns)
        return  [
                dash_table.DataTable(
                    id='datatable-interactivity-dinamica',
                    columns=col_format(df_input.columns,df_input),
                    data=df_input.round(2).to_dict('records'),
                    filter_action = 'native',
                    sort_action = 'native',
                    filter_options={"placeholder_text": "..."},
                    style_table={'overflowX':'auto', 'width':'100%'},
                    editable=False,
                    style_data_conditional=(
                        [
                            {
                                'if': {
                                    'filter_query': '{%}<0',
                                    'column_id': 'PERF% MÉDIA'
                                },
                                'color': '#db0211',
                                'fontWeight': 'bold',

                            },
                            {
                                'if': {
                                    'filter_query': '{%}>0',
                                    'column_id':'PERF% MÉDIA'
                                },
                                'color': '#247d04',
                                'fontWeight': 'bold'
                            },
                            {
                                'if': {'column_id':input},
                                'fontWeight': 'bold'
                            },


                        ]

                    ),
                    style_header={
                            'backgroundColor': 'rgb(20, 20, 20)',
                            'color': 'orange',
                            'textAlign': 'center'
                    },
                    style_data={
                            'backgroundColor': 'white',
                            'color': 'black',


                    },
                    style_as_list_view=True,
                    style_cell={'border': '1px solid black','fontFamily': 'Arial, sans-serif', 'textAlign':'center','width':'auto', 'overflow':'hidden','padding':'5px','fontSize':'12px', 'whiteSpace':'normal'},
                    style_filter = {
                    'backgroundColor': '#d3d3d3',
                    'color': 'black',
                    'fontWeight': 'bold',
                    'textAlign': 'left'},
                    css=[{
                        'selector': '.select-page input',
                        'rule': 'display: none;'  # Ajuste o tamanho da caixa e da fonte
                    }, {
                        'selector': '.previous-page, .next-page, .first-page, .last-page',
                        'rule': 'font-size: 10px;'  # Ajuste o tamanho da fonte dos botões de página
                    }]
                )
            ]











