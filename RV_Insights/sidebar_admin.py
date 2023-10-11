
from dash import html
from dash.dependencies import Input, Output, State
from dash import dcc
from src.app import *
import pandas as pd
from datetime import datetime
from dash.exceptions import PreventUpdate

                                # ======== DADOS ======== #

custom_option_style = {'margin-bottom': '2px'}
run_excel_file = pd.ExcelFile('assets/run190923.xlsx')
PE_list = run_excel_file.sheet_names
PE_outros = [
    'Compra de Put Spread',
    'Compra de Put',
    'Compra de Call'
]

for x in PE_outros:
    PE_list.append(x)

stock_df = pd.read_excel('assets/2023 09 18 Stock-Guide.xlsm', sheet_name='Stock Guide', header=None)
headers_stock_df = pd.read_excel('assets/headers_stock.xlsx')
stock_limpo = stock_df.dropna()
stock_limpo.columns = list(headers_stock_df)

params = ['Parâmetros', 'Import']
insights = ['P.E.', 'SWING']

PE_dict = {
    'Smart Coupon': [
    dbc.Row([
        dbc.Col([
            html.Div([
            html.H6('CUSTO', className='text-warning'),
            dcc.Input(id='input1', type='number', min=0, step=0.1, style={'width': '80px'})
        ]),
            html.Div([
                html.H6('C PUT', className='text-warning'),
                dcc.Input(id='input2', type='number', min=0, step=0.1, style={'width': '80px'})
            ], style={'margin-top': '5px'}),
            html.Div([
                html.H6('C CALL KO', className='text-warning'),
                dcc.Input(id='input3', type='number', min=0, step=0.1, style={'width': '80px'})
            ], style={'margin-top': '5px'}),
            html.Div([
                html.H6('V CALL KI', className='text-warning'),
                dcc.Input(id='input4', type='number', min=0, step=0.1, style={'width': '80px'}),
            ], style={'margin-top': '5px'}),
            html.Div([
                html.H6('UP KI | KO', className='text-warning'),
                dcc.Input(id='input5', type='number', min=0, step=0.1, style={'width': '80px'})
            ], style={'margin-top': '5px'}),
            html.Div([
                html.H6('FIXING', className='text-warning'),
                dcc.DatePickerSingle(id='datepicker', placeholder='Data...', style={'width': '80px'})
            ], style={'margin-top': '5px'})
        ], md=10),
        dbc.Col([
            html.H5(id='output1'),
            html.H5(id='output2', style={'margin-top': '37px', 'textAlign':'left'}),
            html.H5(id='output3', style={'margin-top': '37px'}),
            html.H5(id='output3', style={'margin-top': '37px'}),
            html.H5(id='output4', style={'margin-top': '37px'}),
            html.H5(id='output5', style={'margin-top': '37px'}),
            html.H5(id='datepicker-output', style={'margin-top': '37px'}),
        ],md=2, style={'margin-top': '30px', 'justify-content': 'flex-end'}),
        dbc.Row([
            html.Div([
                html.H6('PITCH', className='text-warning'),
                dcc.Textarea(value='', id='textarea-rebal-modal-swing', style={'width': '100%', 'height': '100px'})
            ], style={'margin-top': '15px'}),
            html.Div([
                html.H6('GIRO SETORIAL', className='text-warning'),
                dcc.RadioItems(['Sim', 'Não'], inline=True, labelStyle={'margin-right': '10px', 'margin-left': '2px'})
            ], style={'margin-top': '5px'})
        ]),
        html.Div([dbc.Button('CADASTRAR INSIGHT', className="btn btn-outline-warning", color='Warning', size='sm',
                             id='cadastrar-insight-pe-button', style={'margin-top': '7px'})
        ], style={'justify-content': 'flex-end', 'display': 'flex'})
    ])
],
    'Financiamento com Ativo': [
        dbc.Row([
            dbc.Col([
                html.Div([
                html.H6('PRÊMIO', className='text-warning'),
                dcc.Input(id='input1', type='number', min=0, step=0.1, style={'width': '80px'})
            ]),
                html.Div([
                    html.H6('V CALL', className='text-warning'),
                    dcc.Input(id='input2', type='number', min=0, step=0.1, style={'width': '80px'})
                ], style={'margin-top': '5px'}),
                html.Div([
                    html.H6('PRAZO', className='text-warning'),
                    dcc.DatePickerSingle(id='datepicker', placeholder='Data...', style={'width': '80px'})
                ], style={'margin-top': '5px'})
            ], md=10),
            dbc.Col([
                html.H5(id='output1'),
                html.H5(id='output2', style={'margin-top': '37px'}),
                html.H5(id='datepicker-output', style={'margin-top': '37px'})
            ], style={'margin-top': '30px'}, md=2),
            dbc.Row([
                html.Div([
                    html.H6('PITCH', className='text-warning'),
                    dcc.Textarea(value='', id='textarea-rebal-modal-swing', style={'width': '100%', 'height': '100px'})
                ], style={'margin-top': '15px'}),
                html.Div([
                    html.H6('GIRO SETORIAL', className='text-warning'),
                    dcc.RadioItems(['Sim', 'Não'], inline=True,
                                   labelStyle={'margin-right': '10px', 'margin-left': '2px'})
                ], style={'margin-top': '5px'})
            ]),
            html.Div([dbc.Button('CADASTRAR INSIGHT', className="btn btn-outline-warning", color='Warning', size='sm',
                                 id='cadastrar-insight-pe-button', style={'margin-top': '7px'})
            ], style={'justify-content': 'flex-end', 'display': 'flex'})
        ])

    ],
    'Aceleradora KO com Ativo': [
        dbc.Row([
            dbc.Col([
                html.Div([
                html.H6('CUSTO', className='text-warning'),
                dcc.Input(id='input1', type='number', min=0, step=0.1, style={'width': '80px'})
            ]),
                html.Div([
                    html.H6('C CALL KO', className='text-warning'),
                    dcc.Input(id='input2', type='number', min=0, step=0.1, style={'width': '80px'})
                ], style={'margin-top': '5px'}),
                html.Div([
                    html.H6('UP KO | V CALL', className='text-warning'),
                    dcc.Input(id='input3', type='number', min=0, step=0.1, style={'width': '80px'})
                ], style={'margin-top': '5px'}),
                html.Div([
                    html.H6('FIXING', className='text-warning'),
                    dcc.DatePickerSingle(id='datepicker', placeholder='Data...', style={'width': '80px'})
                ], style={'margin-top': '5px'})
            ], md=10),
            dbc.Col([
                html.H5(id='output1'),
                html.H5(id='output2', style={'margin-top': '37px'}),
                html.H5(id='output3', style={'margin-top': '37px'}),
                html.H5(id='datepicker-output', style={'margin-top': '37px'})
            ], style={'margin-top': '30px'}, md=2),
            dbc.Row([
                html.Div([
                    html.H6('PITCH', className='text-warning'),
                    dcc.Textarea(value='', id='textarea-rebal-modal-swing', style={'width': '100%', 'height': '100px'})
                ], style={'margin-top': '15px'}),
                html.Div([
                    html.H6('GIRO SETORIAL', className='text-warning'),
                    dcc.RadioItems(['Sim', 'Não'], inline=True,
                                   labelStyle={'margin-right': '10px', 'margin-left': '2px'})
                ], style={'margin-top': '5px'})
            ]),
            html.Div(
                [dbc.Button('CADASTRAR INSIGHT', className="btn btn-outline-warning", color='Warning', size='sm', id='cadastrar-insight-pe-button', style={'margin-top': '7px'})
            ],style={'justify-content': 'flex-end', 'display': 'flex'})
        ])

    ],
    'Twin Win Protected - TWIP': [
        dbc.Row([
            dbc.Col([
                html.Div([
                html.H6('CUSTO', className='text-warning'),
                dcc.Input(id='input1', type='number', min=0, step=0.1, style={'width': '80px'})
                ]),
                html.Div([
                    html.H6('C PUT', className='text-warning'),
                    dcc.Input(id='input2', type='number', min=0, step=0.1, style={'width': '80px'}),
                ], style={'margin-top': '5px'}),
                html.Div([
                    html.H6('C PUT', className='text-warning'),
                    dcc.Input(id='input3', type='number', min=0, step=0.1, style={'width': '80px'}),
                ], style={'margin-top': '5px'}),
                html.Div([
                    html.H6('DOWN KO', className='text-warning'),
                    dcc.Input(id='input4', type='number', min=0, step=0.1, style={'width': '80px'})
                ], style={'margin-top': '5px'}),
                html.Div([
                    html.H6('C CALL KO', className='text-warning'),
                    dcc.Input(id='input5', type='number', min=0, step=0.1, style={'width': '80px'})
                ], style={'margin-top': '5px'}),
                html.Div([
                    html.H6('V CALL KI', className='text-warning'),
                    dcc.Input(id='input6', type='number', min=0, step=0.1, style={'width': '80px'}),
                ], style={'margin-top': '5px'}),
                html.Div([
                    html.H6('UP KI | KO', className='text-warning'),
                    dcc.Input(id='input7', type='number', min=0, step=0.1, style={'width': '80px'})
                ], style={'margin-top': '5px'}),
                html.Div([
                    html.H6('FIXING', className='text-warning'),
                    dcc.DatePickerSingle(id='datepicker', placeholder='Data...', style={'width': '80px'})
                ], style={'margin-top': '5px'})
            ], md=10),
            dbc.Col([
                html.H5(id='output1'),
                html.H5(id='output2', style={'margin-top': '37px'}),
                html.H5(id='output3', style={'margin-top': '37px'}),
                html.H5(id='output4', style={'margin-top': '37px'}),
                html.H5(id='output5', style={'margin-top': '37px'}),
                html.H5(id='output6', style={'margin-top': '37px'}),
                html.H5(id='output7', style={'margin-top': '37px'}),
                html.H5(id='datepicker-output', style={'margin-top': '37px'})
            ], style={'margin-top': '30px'}, md=2),
            dbc.Row([
                html.Div([
                    html.H6('PITCH', className='text-warning'),
                    dcc.Textarea(value='', id='textarea-rebal-modal-swing', style={'width': '100%', 'height': '100px'})
                ], style={'margin-top': '15px'}),
                html.Div([
                    html.H6('GIRO SETORIAL', className='text-warning'),
                    dcc.RadioItems(['Sim', 'Não'], inline=True,
                                   labelStyle={'margin-right': '10px', 'margin-left': '2px'})
                ], style={'margin-top': '5px'})
            ]),
            html.Div([dbc.Button('CADASTRAR INSIGHT', className="btn btn-outline-warning", color='Warning', size='sm',id='cadastrar-insight-pe-button', style={'margin-top': '7px'})
            ], style={'justify-content': 'flex-end', 'display': 'flex'})
        ])
    ],
    'Fence com Ativo': [
        dbc.Row([
            dbc.Col([
                html.Div([
                html.H6('CUSTO', className='text-warning'),
                dcc.Input(id='input1', type='number', min=0, step=0.1, style={'width': '80px'})
                ], style={'margin-top': '5px'}),
                html.Div([
                    html.H6('V CALL', className='text-warning'),
                    dcc.Input(id='input2', type='number', min=0, step=0.1, style={'width': '80px'})
                ], style={'margin-top': '5px'}),
                html.Div([
                    html.H6('C PUT', className='text-warning'),
                    dcc.Input(id='input3', type='number', min=0, step=0.1, style={'width': '80px'})
                ], style={'margin-top': '5px'}),
                html.Div([
                    html.H6('V PUT', className='text-warning'),
                    dcc.Input(id='input4', type='number', min=0, step=0.1, style={'width': '80px'})
                ], style={'margin-top': '5px'}),
                html.Div([
                    html.H6('FIXING', className='text-warning'),
                    dcc.DatePickerSingle(id='datepicker', placeholder='Data...', style={'width': '80px'})
                ], style={'margin-top': '5px'})
            ], md=10),
            dbc.Col([
                html.H5(id='output1'),
                html.H5(id='output2', style={'margin-top': '37px'}),
                html.H5(id='output3', style={'margin-top': '37px'}),
                html.H5(id='output4', style={'margin-top': '37px'}),
                html.H5(id='datepicker-output', style={'margin-top': '37px'}),
            ], style={'margin-top': '30px'}, md=2),
            dbc.Row([
                html.Div([
                    html.H6('PITCH', className='text-warning'),
                    dcc.Textarea(value='', id='textarea-rebal-modal-swing', style={'width': '100%', 'height': '100px'})
                ], style={'margin-top': '15px'}),
                html.Div([
                    html.H6('GIRO SETORIAL', className='text-warning'),
                    dcc.RadioItems(['Sim', 'Não'], inline=True, labelStyle={'margin-right': '10px', 'margin-left': '2px'})
                ], style={'margin-top': '5px'})
            ]),
            html.Div([dbc.Button('CADASTRAR INSIGHT', className="btn btn-outline-warning", color='Warning', size='sm', id='cadastrar-insight-pe-button', style={'margin-top': '7px'})
            ], style={'justify-content': 'flex-end', 'display': 'flex'})
        ])
    ],
    'Cupom Alto Retorno - CAR': [
        dbc.Row([
            dbc.Col([
                html.Div([
                html.H6('CUPOM', className='text-warning'),
                dcc.Input(id='input1', type='number', min=0, step=0.1, style={'width': '80px'})
                ]),
                html.Div([
                    html.H6('DOWN KO', className='text-warning'),
                    dcc.Input(id='input2', type='number', min=0, step=0.1, style={'width': '80px'})
                ], style={'margin-top': '5px'}),
                html.Div([
                    html.H6('UP KO', className='text-warning'),
                    dcc.Input(id='input3', type='number', min=0, step=0.1, style={'width': '80px'})
                ], style={'margin-top': '5px'}),
                html.Div([
                    html.H6('FIXING', className='text-warning'),
                    dcc.DatePickerSingle(id='datepicker', placeholder='Data...', style={'width': '80px'})
                ], style={'margin-top': '5px'})
            ]),
            dbc.Col([
                html.H5(id='output1'),
                html.H5(id='output2', style={'margin-top': '37px'}),
                html.H5(id='output3', style={'margin-top': '37px'}),
                html.H5(id='datepicker-output', style={'margin-top': '37px'}),
            ], style={'margin-top': '30px'}),
            dbc.Row([
                html.Div([
                    html.H6('PITCH', className='text-warning'),
                    dcc.Textarea(value='', id='textarea-rebal-modal-swing', style={'width': '100%', 'height': '100px'})
                ], style={'margin-top': '15px'}),
                html.Div([
                    html.H6('GIRO SETORIAL', className='text-warning'),
                    dcc.RadioItems(['Sim', 'Não'], inline=True, labelStyle={'margin-right': '10px', 'margin-left': '2px'})
                ], style={'margin-top': '5px'})
            ]),
            html.Div([dbc.Button('CADASTRAR INSIGHT', className="btn btn-outline-warning", color='Warning', size='sm', id='cadastrar-insight-pe-button', style={'margin-top': '7px'})
            ], style={'justify-content': 'flex-end', 'display': 'flex'}),
        ])
    ],
    'Stock or Coupon': [
        dbc.Row([
            dbc.Col([
                html.Div([
                html.H6('CUPOM', className='text-warning'),
                dcc.Input(id='input1', type='number', min=0, step=0.1, style={'width': '80px'})
                ]),
                html.Div([
                    html.H6('DOWN KO', className='text-warning'),
                    dcc.Input(id='input2', type='number', min=0, step=0.1, style={'width': '80px'})
                ], style={'margin-top': '5px'}),
                html.Div([
                    html.H6('FIXING', className='text-warning'),
                    dcc.DatePickerSingle(id='datepicker', placeholder='Data...', style={'width': '80px'})
                ], style={'margin-top': '5px'})
            ], md=10),
            dbc.Col([
                html.H5(id='output1'),
                html.H5(id='output2', style={'margin-top': '37px'}),
                html.H5(id='datepicker-output', style={'margin-top': '37px'}),
            ], style={'margin-top': '30px'}, md=2),
            dbc.Row([
                html.Div([
                    html.H6('PITCH', className='text-warning'),
                    dcc.Textarea(value='', id='textarea-rebal-modal-swing', style={'width': '100%', 'height': '100px'})
                ], style={'margin-top': '15px'}),
                html.Div([
                    html.H6('GIRO SETORIAL', className='text-warning'),
                    dcc.RadioItems(['Sim', 'Não'], inline=True, labelStyle={'margin-right': '10px', 'margin-left': '2px'})
                ], style={'margin-top': '5px'})
            ]),
            html.Div([dbc.Button('CADASTRAR INSIGHT', className="btn btn-outline-warning", color='Warning', size='sm', id='cadastrar-insight-pe-button', style={'margin-top': '7px'})
            ], style={'justify-content': 'flex-end', 'display': 'flex'})
        ])
    ],
    'Smart Up': [
        dbc.Row([
            dbc.Col([
                html.Div([
                html.H6('CUSTO', className='text-warning'),
                dcc.Input(id='input1', type='number', min=0, step=0.1, style={'width': '80px'})
                ]),
                html.Div([
                    html.H6('V CALL KI', className='text-warning'),
                    dcc.Input(id='input2', type='number', min=0, step=0.1, style={'width': '80px'})
                ], style={'margin-top': '5px'}),
                html.Div([
                    html.H6('C PUT', className='text-warning'),
                    dcc.Input(id='input3', type='number', min=0, step=0.1, style={'width': '80px'})
                ], style={'margin-top': '5px'}),
                html.Div([
                    html.H6('UP KI', className='text-warning'),
                    dcc.Input(id='input4', type='number', min=0, step=0.1, style={'width': '80px'})
                ], style={'margin-top': '5px'}),
                html.Div([
                    html.H6('FIXING', className='text-warning'),
                    dcc.DatePickerSingle(id='datepicker', placeholder='Data...', style={'width': '80px'})
                ], style={'margin-top': '5px'})
            ]),
            dbc.Col([
                html.H5(id='output1'),
                html.H5(id='output2', style={'margin-top': '37px'}),
                html.H5(id='output3', style={'margin-top': '37px'}),
                html.H5(id='output4', style={'margin-top': '37px'}),
                html.H5(id='datepicker-output', style={'margin-top': '37px'})
            ], style={'margin-top': '30px'}),
            dbc.Row([
                html.Div([
                    html.H6('PITCH', className='text-warning'),
                    dcc.Textarea(value='', id='textarea-rebal-modal-swing', style={'width': '100%', 'height': '100px'})
                ], style={'margin-top': '15px'}),
                html.Div([
                    html.H6('GIRO SETORIAL', className='text-warning'),
                    dcc.RadioItems(['Sim', 'Não'], inline=True, labelStyle={'margin-right': '10px', 'margin-left': '2px'})
                ], style={'margin-top': '5px'}),
            html.Div([dbc.Button('CADASTRAR INSIGHT', className="btn btn-outline-warning", color='Warning', size='sm', id='cadastrar-insight-pe-button', style={'margin-top': '7px'})
            ], style={'justify-content': 'flex-end', 'display': 'flex'})
            ]),
        ])
    ],
    'R.A. (Retorno Alavancado)': [
        dbc.Row([
            dbc.Col([
                html.Div([
                html.H6('CUSTO', className='text-warning'),
                dcc.Input(id='input1', type='number', min=0, step=0.1, style={'width': '80px'})
                ]),
                html.Div([
                    html.H6('V CALL KI', className='text-warning'),
                    dcc.Input(id='input2', type='number', min=0, step=0.1, style={'width': '80px'})
                ], style={'margin-top': '5px'}),
                html.Div([
                    html.H6('C CALL KO', className='text-warning'),
                    dcc.Input(id='input3', type='number', min=0, step=0.1, style={'width': '80px'})
                ], style={'margin-top': '5px'}),
                html.Div([
                    html.H6('UP KI | KO', className='text-warning'),
                    dcc.Input(id='input4', type='number', min=0, step=0.1, style={'width': '80px'})
                ], style={'margin-top': '5px'}),
                html.Div([
                    html.H6('FIXING', className='text-warning'),
                    dcc.DatePickerSingle(id='datepicker', placeholder='Data...', style={'width': '80px'})
                ], style={'margin-top': '5px'}),
            ], md=10),
            dbc.Col([
                html.H5(id='output1'),
                html.H5(id='output2', style={'margin-top': '37px'}),
                html.H5(id='output3', style={'margin-top': '37px'}),
                html.H5(id='output4', style={'margin-top': '37px'}),
                html.H5(id='datepicker-output', style={'margin-top': '37px'})
            ], style={'margin-top': '30px'}, md=2),
            dbc.Row([
                html.Div([
                    html.H6('PITCH', className='text-warning'),
                    dcc.Textarea(value='', id='textarea-rebal-modal-swing', style={'width': '100%', 'height': '100px'})
                ], style={'margin-top': '15px'}),
                html.Div([
                    html.H6('GIRO SETORIAL', className='text-warning'),
                    dcc.RadioItems(['Sim', 'Não'], inline=True, labelStyle={'margin-right': '10px', 'margin-left': '2px'})
                ], style={'margin-top': '5px'})
            ]),
            html.Div([dbc.Button('CADASTRAR INSIGHT', className="btn btn-outline-warning", color='Warning', size='sm', id='cadastrar-insight-pe-button', style={'margin-top': '7px'})
            ], style={'justify-content': 'flex-end', 'display': 'flex'})
        ])
    ],
    'Fence KI com Ativo': [
        dbc.Row([
            dbc.Col([
                html.Div([
                html.H6('CUSTO', className='text-warning'),
                dcc.Input(id='input1', type='number', min=0, step=0.1, style={'width': '80px'})
                ]),
                html.Div([
                    html.H6('V CALL KI', className='text-warning'),
                    dcc.Input(id='input2', type='number', min=0, step=0.1, style={'width': '80px'})
                ], style={'margin-top': '5px'}),
                html.Div([
                    html.H6('C PUT', className='text-warning'),
                    dcc.Input(id='input3', type='number', min=0, step=0.1, style={'width': '80px'})
                ], style={'margin-top': '5px'}),
                html.Div([
                    html.H6('UP KI', className='text-warning'),
                    dcc.Input(id='input4', type='number', min=0, step=0.1, style={'width': '80px'})
                ], style={'margin-top': '5px'}),
                html.Div([
                    html.H6('V PUT', className='text-warning'),
                    dcc.Input(id='input5', type='number', min=0, step=0.1, style={'width': '80px'})
                ], style={'margin-top': '5px'}),
                html.Div([
                    html.H6('FIXING', className='text-warning'),
                    dcc.DatePickerSingle(id='datepicker', placeholder='Data...', style={'width': '80px'})
                ], style={'margin-top': '5px'})
            ], md=10),
            dbc.Col([
                html.H5(id='output1'),
                html.H5(id='output2', style={'margin-top': '37px'}),
                html.H5(id='output3', style={'margin-top': '37px'}),
                html.H5(id='output4', style={'margin-top': '37px'}),
                html.H5(id='output5', style={'margin-top': '37px'}),
                html.H5(id='datepicker-output', style={'margin-top': '37px'})
            ], style={'margin-top': '30px'}, md=2),
            dbc.Row([
                html.Div([
                    html.H6('PITCH', className='text-warning'),
                    dcc.Textarea(value='', id='textarea-rebal-modal-swing', style={'width': '100%', 'height': '100px'})
                ], style={'margin-top': '15px'}),
                html.Div([
                    html.H6('GIRO SETORIAL', className='text-warning'),
                    dcc.RadioItems(['Sim', 'Não'], inline=True, labelStyle={'margin-right': '10px', 'margin-left': '2px'})
                ], style={'margin-top': '5px'})
            ]),
            html.Div([dbc.Button('CADASTRAR INSIGHT', className="btn btn-outline-warning", color='Warning', size='sm', id='cadastrar-insight-pe-button', style={'margin-top': '7px'})
            ], style={'justify-content': 'flex-end', 'display': 'flex'})
        ])
],
    'Smart Hedge': [
        dbc.Row([
            dbc.Col([
                html.Div([
                html.H6('CUSTO', className='text-warning'),
                dcc.Input(id='input1', type='number', min=0, step=0.1, style={'width': '80px'})
                ]),
                html.Div([
                    html.H6('V CALL KI', className='text-warning'),
                    dcc.Input(id='input2', type='number', min=0, step=0.1, style={'width': '80px'})
                ], style={'margin-top': '5px'}),
                html.Div([
                    html.H6('C PUT', className='text-warning'),
                    dcc.Input(id='input3', type='number', min=0, step=0.1, style={'width': '80px'})
                ], style={'margin-top': '5px'}),
                html.Div([
                    html.H6('FIXING', className='text-warning'),
                    dcc.DatePickerSingle(id='datepicker', placeholder='Data...', style={'width': '80px'})
                ], style={'margin-top': '5px'})
            ]),
            dbc.Col([
                html.H5(id='output1', style={'margin-top': '37px'}),
                html.H5(id='output2', style={'margin-top': '37px'}),
                html.H5(id='output3', style={'margin-top': '37px'}),
                html.H5(id='datepicker-output', style={'margin-top': '37px'})
            ], style={'margin-top': '30px'}),
            dbc.Row([
                html.Div([
                    html.H6('PITCH', className='text-warning'),
                    dcc.Textarea(value='', id='textarea-rebal-modal-swing', style={'width': '100%', 'height': '100px'})
                ], style={'margin-top': '15px'}),
                html.Div([
                    html.H6('GIRO SETORIAL', className='text-warning'),
                    dcc.RadioItems(['Sim', 'Não'], inline=True,
                                   labelStyle={'margin-right': '10px', 'margin-left': '2px'})
                ], style={'margin-top': '5px'})
            ]),
            html.Div([dbc.Button('CADASTRAR INSIGHT', className="btn btn-outline-warning", color='Warning', size='sm', id='cadastrar-insight-pe-button', style={'margin-top': '7px'})
            ], style={'justify-content': 'flex-end', 'display': 'flex'}),
        ])
    ],
    'Resultado até Barreira Dinâmic': [
        dbc.Row([
            dbc.Col([
                html.Div([
                html.H6('CUPOM', className='text-warning'),
                dcc.Input(id='input1', type='number', min=0, step=0.1, style={'width': '80px'})
            ]),
                html.Div([
                    html.H6('C PUT KO', className='text-warning'),
                    dcc.Input(id='input2', type='number', min=0, step=0.1, style={'width': '80px'})
                ], style={'margin-top': '5px'}),
                html.Div([
                    html.H6('DOWN KO', className='text-warning'),
                    dcc.Input(id='input3', type='number', min=0, step=0.1, style={'width': '80px'})
                ], style={'margin-top': '5px'}),
                html.Div([
                    html.H6('C CALL KO', className='text-warning'),
                    dcc.Input(id='input4', type='number', min=0, step=0.1, style={'width': '80px'})
                ], style={'margin-top': '5px'}),
                html.Div([
                    html.H6('UP KO', className='text-warning'),
                    dcc.Input(id='input5', type='number', min=0, step=0.1, style={'width': '80px'})
                ], style={'margin-top': '5px'}),
                html.Div([
                    html.H6('FIXING', className='text-warning'),
                    dcc.Input(id='datepicker', type='number', min=0, step=0.1, style={'width': '80px'})
                ], style={'margin-top': '5px'})
            ]),
            dbc.Col([
                html.H5(id='output1', style={'margin-top': '37px'}),
                html.H5(id='output2', style={'margin-top': '37px'}),
                html.H5(id='output3', style={'margin-top': '37px'}),
                html.H5(id='output4', style={'margin-top': '37px'}),
                html.H5(id='output5', style={'margin-top': '37px'}),
                html.H5(id='datepicker-output', style={'margin-top': '37px'})
            ], style={'margin-top': '30px'}),
            dbc.Row([
                html.Div([
                    html.H6('PITCH', className='text-warning'),
                    dcc.Textarea(value='', id='textarea-rebal-modal-swing', style={'width': '100%', 'height': '100px'})
                ], style={'margin-top': '15px'}),
                html.Div([
                    html.H6('GIRO SETORIAL', className='text-warning'),
                    dcc.RadioItems(['Sim', 'Não'], inline=True,
                                   labelStyle={'margin-right': '10px', 'margin-left': '2px'})
                ], style={'margin-top': '5px'})
            ]),
            html.Div([dbc.Button('CADASTRAR INSIGHT', className="btn btn-outline-warning", color='Warning', size='sm', id='cadastrar-insight-pe-button', style={'margin-top': '7px'})
            ], style={'justify-content': 'flex-end', 'display': 'flex'})
        ])
],
    'Compra de Call Spread': [
        dbc.Row([
            dbc.Col([
                html.Div([
                html.H6('CUSTO', className='text-warning'),
                dcc.Input(id='input1', type='number', min=0, step=0.1, style={'width': '80px'})
                ]),
                html.Div([
                    html.H6('C CALL', className='text-warning'),
                    dcc.Input(id='input2', type='number', min=0, step=0.1, style={'width': '80px'})
                ], style={'margin-top': '5px'}),
                html.Div([
                    html.H6('V CALL', className='text-warning'),
                    dcc.Input(id='input3', type='number', min=0, step=0.1, style={'width': '80px'})
                ], style={'margin-top': '5px'}),
                html.Div([
                    html.H6('FIXING', className='text-warning'),
                    dcc.DatePickerSingle(id='datepicker', placeholder='Data...', style={'width': '80px'})
                ], style={'margin-top': '5px'})
            ]),
            dbc.Col([
                html.H5(id='output1', style={'margin-top': '37px'}),
                html.H5(id='output2', style={'margin-top': '37px'}),
                html.H5(id='output3', style={'margin-top': '37px'}),
                html.H5(id='datepicker-output', style={'margin-top': '37px'})
            ], style={'margin-top': '30px'}),
            dbc.Row([
                html.Div([
                    html.H6('PITCH', className='text-warning'),
                    dcc.Textarea(value='', id='textarea-rebal-modal-swing', style={'width': '100%', 'height': '100px'})
                ], style={'margin-top': '15px'}),
                html.Div([
                    html.H6('GIRO SETORIAL', className='text-warning'),
                    dcc.RadioItems(['Sim', 'Não'], inline=True, labelStyle={'margin-right': '10px', 'margin-left': '2px'})
                ], style={'margin-top': '5px'})
            ]),
            html.Div([dbc.Button('CADASTRAR INSIGHT', className="btn btn-outline-warning", color='Warning', size='sm', id='cadastrar-insight-pe-button', style={'margin-top': '7px'})
            ], style={'justify-content': 'flex-end', 'display': 'flex'})
        ])
    ],
    'TWIP Up': [
        dbc.Row([
            dbc.Col([
                html.Div([
                html.H6('CUSTO', className='text-warning'),
                dcc.Input(id='input1', type='number', min=0, step=0.1, style={'width': '80px'})
                ]),
                html.Div([
                    html.H6('V CALL KI', className='text-warning'),
                    dcc.Input(id='input2', type='number', min=0, step=0.1, style={'width': '80px'})
                ], style={'margin-top': '5px'}),
                html.Div([
                    html.H6('C PUT', className='text-warning'),
                    dcc.Input(id='input3', type='number', min=0, step=0.1, style={'width': '80px'})
                ], style={'margin-top': '5px'}),
                html.Div([
                    html.H6('C PUT KO', className='text-warning'),
                    dcc.Input(id='input4', type='number', min=0, step=0.1, style={'width': '80px'})
                ], style={'margin-top': '5px'}),
                html.Div([
                    html.H6('C CALL KO', className='text-warning'),
                    dcc.Input(id='input5', type='number', min=0, step=0.1, style={'width': '80px'})
                ], style={'margin-top': '5px'}),
                html.Div([
                    html.H6('DOWN KO', className='text-warning'),
                    dcc.Input(id='input6', type='number', min=0, step=0.1, style={'width': '80px'})
                ], style={'margin-top': '5px'}),
                html.Div([
                    html.H6('UP KI | KO', className='text-warning'),
                    dcc.Input(id='input7', type='number', min=0, step=0.1, style={'width': '80px'})
                ], style={'margin-top': '5px'}),
                html.Div([
                    html.H6('FIXING', className='text-warning'),
                    dcc.DatePickerSingle(id='datepicker', placeholder='Data...', style={'width': '80px'})
                ], style={'margin-top': '5px'})
            ], md=10),
            dbc.Col([
                html.H5(id='output1'),
                html.H5(id='output2', style={'margin-top': '37px'}),
                html.H5(id='output3', style={'margin-top': '37px'}),
                html.H5(id='output4', style={'margin-top': '37px'}),
                html.H5(id='output5', style={'margin-top': '37px'}),
                html.H5(id='output6', style={'margin-top': '37px'}),
                html.H5(id='output7', style={'margin-top': '37px'}),
                html.H5(id='datepicker-output', style={'margin-top': '37px'})
            ], style={'margin-top': '30px'}, md=2),
            dbc.Row([
                html.Div([
                    html.H6('PITCH', className='text-warning'),
                    dcc.Textarea(value='', id='textarea-rebal-modal-swing', style={'width': '100%', 'height': '100px'})
                ], style={'margin-top': '15px'}),
                html.Div([
                    html.H6('GIRO SETORIAL', className='text-warning'),
                    dcc.RadioItems(['Sim', 'Não'], inline=True, labelStyle={'margin-right': '10px', 'margin-left': '2px'})
                ], style={'margin-top': '5px'})
            ]),
            html.Div([dbc.Button('CADASTRAR INSIGHT', className="btn btn-outline-warning", color='Warning', size='sm', id='cadastrar-insight-pe-button', style={'margin-top': '7px'})
            ], style={'justify-content': 'flex-end', 'display': 'flex'})
        ])
    ],
    'Compra de Put Spread': [
        dbc.Row([
            dbc.Col([
                html.Div([
                    html.H6('CUSTO', className='text-warning'),
                    dcc.Input(id='input1', type='number', min=0, step=0.1, style={'width': '80px'})
                ]),
                html.Div([
                    html.H6('C PUT', className='text-warning'),
                    dcc.Input(id='input2', type='number', min=0, step=0.1, style={'width': '80px'})
                ], style={'margin-top': '5px'}),
                html.Div([
                    html.H6('V PUT', className='text-warning'),
                    dcc.Input(id='input3', type='number', min=0, step=0.1, style={'width': '80px'})
                ], style={'margin-top': '5px'}),
                html.Div([
                    html.H6('FIXING', className='text-warning'),
                    dcc.DatePickerSingle(id='datepicker', placeholder='Data...', style={'width': '80px'})
                ], style={'margin-top': '5px'}),
                html.Div([
                    html.H6('PITCH', className='text-warning'),
                    dcc.Textarea(value='', id='textarea-rebal-modal-swing', style={'width': '100%', 'height': '200px'})
                ], style={'margin-top': '15px'}),
                html.Div([
                    html.H6('GIRO SETORIAL', className='text-warning'),
                    dcc.RadioItems(['Sim', 'Não'], inline=True, labelStyle={'margin-right': '10px', 'margin-left': '2px'})
                ], style={'margin-top': '5px'})
            ]),
            dbc.Col([
                html.H5(id='output1'),
                html.H5(id='output2', style={'margin-top': '37px'}),
                html.H5(id='output3', style={'margin-top': '37px'}),
                html.H5(id='datepicker-output', style={'margin-top': '37px'})
            ], style={'margin-top': '30px'}),
            dbc.Row([
                html.Div([
                    html.H6('PITCH', className='text-warning'),
                    dcc.Textarea(value='', id='textarea-rebal-modal-swing', style={'width': '100%', 'height': '100px'})
                ], style={'margin-top': '15px'}),
                html.Div([
                    html.H6('GIRO SETORIAL', className='text-warning'),
                    dcc.RadioItems(['Sim', 'Não'], inline=True,labelStyle={'margin-right': '10px', 'margin-left': '2px'})
                ], style={'margin-top': '5px'}),
            ]),
            html.Div([dbc.Button('CADASTRAR INSIGHT', className="btn btn-outline-warning", color='Warning', size='sm', id='cadastrar-insight-pe-button', style={'margin-top': '7px'})], style={'justify-content': 'flex-end', 'display': 'flex'})
        ])
    ],
    'Compra de Put': [
        dbc.Row([
            dbc.Col([
                html.Div([
                    html.H6('CUSTO', className='text-warning'),
                    dcc.Input(id='input1', type='number', min=0, step=0.1, style={'width': '80px'})
                ]),
                html.Div([
                    html.H6('C PUT', className='text-warning'),
                    dcc.Input(id='input2', type='number', min=0, step=0.1, style={'width': '80px'})
                ], style={'margin-top': '5px'}),
                html.Div([
                    html.H6('FIXING', className='text-warning'),
                    dcc.DatePickerSingle(id='datepicker', placeholder='Data...', style={'width': '80px'})
                ], style={'margin-top': '5px'})
            ]),
            dbc.Col([
                html.H5(id='output1'),
                html.H5(id='output2', style={'margin-top': '37px'}),
                html.H5(id='datepicker-output', style={'margin-top': '37px'})
            ], style={'margin-top': '30px'}),
            dbc.Row([
                html.Div([
                    html.H6('PITCH', className='text-warning'),
                    dcc.Textarea(value='', id='textarea-rebal-modal-swing', style={'width': '100%', 'height': '100px'})
                ], style={'margin-top': '15px'}),
                html.Div([
                    html.H6('GIRO SETORIAL', className='text-warning'),
                    dcc.RadioItems(['Sim', 'Não'], inline=True, labelStyle={'margin-right': '10px', 'margin-left': '2px'})
                ], style={'margin-top': '5px'}),
            ]),
            html.Div([dbc.Button('CADASTRAR INSIGHT', className="btn btn-outline-warning", color='Warning', size='sm', id='cadastrar-insight-pe-button', style={'margin-top': '7px'})
            ], style={'justify-content': 'flex-end', 'display': 'flex'})
        ])
    ],
    'Compra de Call': [
        dbc.Row([
            dbc.Col([
                html.Div([
                    html.H6('CUSTO', className='text-warning'),
                    dcc.Input(id='input1', type='number', min=0, step=0.1, style={'width': '80px'})
                ]),
                html.Div([
                    html.H6('C CALL', className='text-warning'),
                    dcc.Input(id='input2', type='number', min=0, step=0.1, style={'width': '80px'})
                ], style={'margin-top': '5px'}),
                html.Div([
                    html.H6('FIXING', className='text-warning'),
                    dcc.DatePickerSingle(id='datepicker', placeholder='Data...', style={'width': '80px'})
                ], style={'margin-top': '5px'})
            ]),
            dbc.Col([
                html.H5(id='output1'),
                html.H5(id='output2', style={'margin-top': '37px'}),
                html.H5(id='datepicker-output', style={'margin-top': '37px'})
            ], style={'margin-top': '30px'}),
            dbc.Row([
                html.Div([
                    html.H6('PITCH', className='text-warning'),
                    dcc.Textarea(value='', id='textarea-rebal-modal-swing', style={'width': '100%', 'height': '100px'})
                ], style={'margin-top': '15px'}),
                html.Div([
                    html.H6('GIRO SETORIAL', className='text-warning'),
                    dcc.RadioItems(['Sim', 'Não'], inline=True, labelStyle={'margin-right': '10px', 'margin-left': '2px'})
                ], style={'margin-top': '5px'}),
            ]),
            html.Div([dbc.Button('CADASTRAR INSIGHT', className="btn btn-outline-warning", color='Warning', size='sm', id='cadastrar-insight-pe-button', style={'margin-top': '7px'})
            ], style={'justify-content': 'flex-end', 'display': 'flex'})
        ])
    ]
}
SWING_dict = {
    'Rebalanceamento': [
    dbc.Row([html.Div([
        dcc.Dropdown(stock_limpo['Ticker'], placeholder="Ativo", style={'width': '110px'}, id='input-text-ativo')
        ], style={'display': 'flex', 'margin-top':'3px'})]),
    html.Hr(),
    html.Div([
        html.H6('Research', className='text-warning'),
        dcc.RadioItems([' EQI', ' Quantzed', ' Monett', ' Outros'], inline=True, labelStyle={'margin-right': '20px'})
    ], style={'margin-top': '5px'}),
    html.Div([
        html.H6('GIRO SETORIAL', className='text-warning'),
        dcc.RadioItems([' Sim', ' Não'], inline=True, labelStyle={'margin-right': '10px'})
    ], style={'margin-top': '15px'}),
    html.Div([
        html.H6('SELECIONAR ATIVOS', className='text-warning'),
        dcc.Dropdown(stock_limpo['Ticker'],placeholder='Ativo', multi=True)
    ], style={'margin-top': '15px'}),
    html.Div([
        html.H6('PITCH', className='text-warning'),
        dcc.Textarea(value='', id='textarea-rebal-modal-swing', style={'width':'100%','height':'200px'})
    ], style={'margin-top': '15px'}),
    html.Div([
        dbc.Button('CADASTRAR INSIGHT', className="btn btn-outline-warning", color='Warning', size='sm',id='cadastrar-insight-swing-button', style={'margin-top': '7px'})
    ], style={'justify-content': 'flex-end', 'display': 'flex', 'margin-top': '20px'})
    ],
    'Long&Short': [
            dbc.Row([
                html.Div([
                    dcc.Dropdown(stock_limpo['Ticker'], placeholder="Long", style={'width': '110px'}, id='input-drop-ativo-long'),
                    html.H6('C', className='text-warning', style={'margin-left':'3px'})
                ], style={'display': 'flex', 'margin-top':'10px'}),
                html.Div([
                    dcc.Dropdown(stock_limpo['Ticker'], placeholder="Short", style={'width': '110px'}, id='input-drop-ativo-short'),
                    html.H6('V', className='text-warning', style={'margin-left':'3px'})
                ], style={'display': 'flex', 'margin-top':'3px'})]),
                html.Div([
                    dbc.Button('switch', id='switch-button', className="btn btn-outline-warning", color='Warning', size='sm', style={'margin-top': '5px'})
                ], style={'display': 'flex'}),
                html.Hr(),
                dbc.Container([
                    html.Div([
                            html.H6('Research', className='text-warning'),
                            dcc.RadioItems([' EQI',' Quantzed',' Monett',' Outros'], inline=True, labelStyle={'margin-right':'20px'})
                        ], style={'margin-top': '5px'}),
                    dbc.Row([
                        dbc.Col([
                        html.Div([
                            html.H6('ENTRADA', className='text-warning'),
                            dcc.Input(id='entrada-swing-input', type='number', min=0, step=0.01, style={'width':'80px'})
                        ], style={'margin-top': '5px'}),
                        html.Div([
                            html.H6('STOP', className='text-warning'),
                            dcc.Input(id='stop-swing-input', type='number', min=0, step=0.01, style={'width': '80px'})
                        ], style={'margin-top': '5px'}),
                        html.Div([
                            html.H6('ALVO', className='text-warning'),
                            dcc.Input(id='alvo-swing-input', type='number', min=0, step=0.01, style={'width': '80px'})
                        ], style={'margin-top': '5px'}),
                        ]),
                        dbc.Col([
                            html.H5(id='output-valor-entrada-swing'),
                            html.H5(id='output-valor-stop-swing', style={'margin-top':'36px'}),
                            html.H5(id='output-valor-alvo-swing', style={'margin-top':'36px'})
                        ], style={'margin-top':'36px'})
                    ])
                ], style={'margin-top':'20px'}),
        html.Div([dbc.Button('CADASTRAR INSIGHT', className="btn btn-outline-warning", color='Warning', size='sm', id='cadastrar-insight-swing-button', style={'margin-top': '7px'})
                  ], style={'justify-content': 'flex-end', 'display': 'flex', 'margin-top': '20px'})
    ],
    'Swing Trade': [
            dbc.Row([
                html.Div([
                    dcc.Dropdown(stock_limpo['Ticker'], placeholder="Ativo", style={'width': '110px'}, id='input-text-ativo')
                ], style={'display': 'flex', 'margin-top':'5px'})]),
            html.Hr(),
            dbc.Container([
                html.Div([
                    html.H6('Research', className='text-warning'),
                    dcc.RadioItems([' EQI', ' Quantzed', ' Monett', ' Outros'], inline=True, labelStyle={'margin-right': '20px'})
                ], style={'margin-top': '5px'}),
                html.Div([
                        html.H6('C | V', className='text-warning'),
                        dcc.RadioItems([' Compra', ' Venda'], inline=True, labelStyle={'margin-right': '10px'})
                    ], style={'margin-top': '5px'}),
                dbc.Row([
                    dbc.Col([
                    html.Div([
                        html.H6('ENTRADA', className='text-warning'),
                        dcc.Input(id='entrada-swing-input', type='number', min=0, step=0.01, style={'width':'80px'})
                    ], style={'margin-top': '5px'}),
                    html.Div([
                        html.H6('STOP', className='text-warning'),
                        dcc.Input(id='stop-swing-input', type='number', min=0, step=0.01, style={'width': '80px'})
                    ], style={'margin-top': '5px'}),
                    html.Div([
                        html.H6('ALVO', className='text-warning'),
                        dcc.Input(id='alvo-swing-input', type='number', min=0, step=0.01, style={'width': '80px'})
                    ], style={'margin-top': '5px'}),
                    ]),
                    dbc.Col([
                        html.H5(id='output-valor-entrada-swing'),
                        html.H5(id='output-valor-stop-swing', style={'margin-top':'36px'}),
                        html.H5(id='output-valor-alvo-swing', style={'margin-top':'36px'})
                    ], style={'margin-top':'36px'})
                ])
            ], style={'margin-top':'20px'}),
    html.Div([dbc.Button('CADASTRAR INSIGHT', className="btn btn-outline-warning", color='Warning', size='sm', id='cadastrar-insight-swing-button', style={'margin-top': '7px'})
    ], style={'justify-content': 'flex-end', 'display': 'flex','margin-top':'20px'})
    ]
}
PARAMS_dict = {
    'Parâmetros':[
        dbc.Container([
            html.H5('RISCO RADAR', className='text-warning', style={'margin-top':'10px', 'textAlign':'center'}),
            dbc.Row([
                dbc.Col([
                    html.Div([
                        html.H6('Exposição por ativo', className='text-secondary'),
                        dcc.Input(id='input1-params', type='number', min=0, step=0.01, style={'width': '80px'})
                    ]),
                    html.Div([
                        html.H6('Exposição por setor', className='text-secondary'),
                        dcc.Input(id='input2-params', type='number', min=0, step=0.01, style={'width': '80px'})
                    ], style={'margin-top':'10px'}),
                    html.Div([
                        html.H6('Volatilidade', className='text-secondary'),
                        dcc.Input(id='input3-params', type='number', min=0, step=0.01, style={'width': '80px'})
                    ], style={'margin-top':'10px'}),
                    html.Div([
                        html.H6('Drawdown', className='text-secondary'),
                        dcc.Input(id='input4-params', type='number', min=0, step=0.01, style={'width': '80px'})
                    ], style={'margin-top':'10px'})
                ]),
                dbc.Col([
                    html.Div([
                        html.H6(id='output1-params', style={'margin-top': '30px'} ),
                        html.H6(id='output2-params', style={'margin-top': '48px'}),
                        html.H6(id='output3-params', style={'margin-top': '48px'}),
                        html.H6(id='output4-params', style={'margin-top': '48px'})
                    ], style={'text-align':'right','margin-right':'20px'})
                ])
            ]),
            html.Hr(),
            html.H5('INSIGHTS', className='text-warning', style={'margin-top':'20px', 'textAlign':'center'}),
            dbc.Row([
                dbc.Col([
                    html.Div([
                        html.H6('Venda / PM', className='text-secondary'),
                        dcc.Input(id='input5-params', type='number', min=0, step=0.01, style={'width': '80px'})
                    ])
                ]),
                dbc.Col([
                    html.Div([
                        html.H6(id='output5-params', style={'margin-top': '30px'}),
                    ], style={'text-align':'right','margin-right':'20px'})
                ]),
                html.Div([dbc.Button('SALVAR PARÂMETROS', className="btn btn-outline-warning", color='Warning', size='sm', id='cadastrar-insight-swing-button', style={'margin-top': '7px'})
                ], style={'justify-content': 'center', 'display': 'flex', 'margin-top': '20px'})

            ])
        ])
    ],

    'Import':[
        dbc.Container([
            html.Div([
                html.H6('CUSTÓDIA', className='text-warning', style={'textAlign': 'center'}),
                dcc.Upload(
                    children=html.Div([
                        'import.xlsx'
                    ]),
                    style={
                        'width': '100%',
                        'height': '60px',
                        'lineHeight': '60px',
                        'borderWidth': '1px',
                        'borderStyle': 'dashed',
                        'borderRadius': '5px',
                        'textAlign': 'center',
                    },
                    multiple=True
                )
            ]),
            html.Div([
                html.H6('STOCK GUIDE', className='text-warning', style={'textAlign': 'center'}),
                dcc.Upload(
                    children=html.Div([
                        'import.xlsx'
                    ]),
                    style={
                        'width': '100%',
                        'height': '60px',
                        'lineHeight': '60px',
                        'borderWidth': '1px',
                        'borderStyle': 'dashed',
                        'borderRadius': '5px',
                        'textAlign': 'center',
                    },
                    multiple=True
                )
            ], style={'margin-top': '10px'}),
            html.Div([
                html.H6('RUN', className='text-warning', style={'textAlign': 'center'}),
                dcc.Upload(
                    children=html.Div([
                        'import.xlsx'
                    ]),
                    style={
                        'width': '100%',
                        'height': '60px',
                        'lineHeight': '60px',
                        'borderWidth': '1px',
                        'borderStyle': 'dashed',
                        'borderRadius': '5px',
                        'textAlign': 'center',
                    },
                    multiple=True
                )
            ], style={'margin-top': '10px'}),
            html.Div([
                html.H6('AUDITORIAS', className='text-warning', style={'textAlign': 'center'}),
                dcc.Upload(
                    children=html.Div([
                        'import.xlsx'
                    ]),
                    style={
                        'width': '100%',
                        'height': '60px',
                        'lineHeight': '60px',
                        'borderWidth': '1px',
                        'borderStyle': 'dashed',
                        'borderRadius': '5px',
                        'textAlign': 'center',
                    },
                    multiple=True
                )
            ], style={'margin-top': '10px'})
        ], style={'margin-top':'20px'}),
        html.Div([dbc.Button('SALVAR', className="btn btn-outline-warning", color='Warning', size='sm', id='cadastrar-insight-swing-button', style={'width':'200px'})
        ], style={'justify-content': 'center', 'display': 'flex', 'margin-top': '20px'})
    ]
}


                                # ========= CRIAR TABS ======== #


def create_tab_content_insights(insight):
    if insight == 'P.E.':
        return dbc.Container([
            dbc.Row([html.Div([
                dcc.Dropdown(stock_limpo['Ticker'], placeholder="Ativo", style={'width':'110px'}, id='input-text-ativo'),
            ], style={'display':'flex'})
            ]),
            dbc.Row([html.Div([
                dcc.Dropdown(PE_list, placeholder="Operação", style={'width':'250px'}, id='input-text-operação')
            ], style={'display':'flex'})

            ], style={'margin-top':'5px'}),
            html.Hr(),
            html.Div(id='content-input-pe',style={'margin-top':'15px'})
        ], style={'margin-top':'10px'})
    else:
        return dbc.Container([
            dbc.Row([html.Div([
                dcc.Dropdown(['Rebalanceamento','Long&Short','Swing Trade'], placeholder="Operação", style={'width': '200px'}, id='input-text-operação-swing')
            ], style={'display': 'flex'}),
            ]),
            html.Div(id='content-input-swing', style={'margin-top': '5px'})
        ], style={'margin-top':'10px'})


tabs_insights = [dbc.Tab(create_tab_content_insights(insight), label=insight, label_style={'color':'#e68a19'}) for insight in insights]

def create_tab_content_params(param):
    if param == 'Parâmetros':
        return PARAMS_dict['Parâmetros']
    else:
        return PARAMS_dict['Import']

tabs_params = [dbc.Tab(create_tab_content_params(param), label=param, label_style={'color':'#e68a19'}) for param in params]

def render_layout():
    layout = dbc.Col([
        dbc.Row([
            dbc.Row([
                html.H1('RV Insight', className='text-warning'),
                html.Hr(),
                dbc.Button('Insights', href='/insights', className="btn btn-outline-warning", color='Warning'),
                dbc.Button('Posições', href = '/posicao', className="btn btn-outline-warning", color='Warning', style={'margin-top':'2px'}),
                dbc.Button('Risco Radar', href='/riscoRadar', className="btn btn-outline-warning", color='Warning',style={'margin-top': '2px'})


            ]),
            html.Div(style={'height':'68vh'}),
            dbc.Row([
                    dbc.Button('Novo Insight', className="btn btn-outline-danger", color='Warning', size='sm', id='open-modal-insight'),
                    dbc.Button('Parâmetros', className="btn btn-outline-secondary", color='Warning', size='sm', id='open-modal-parametro',style={'margin-top': '2px'})
            ])
        ], id='sidebar_completa-admin', style={'border':'#171616','border-radius': '5px', 'color':'black'}),


                                    # ======== MODAL ======== #

        dbc.Modal([
                dbc.ModalHeader(dbc.ModalTitle(id='modal-title', style={'color':'#e68a19'})),
                dbc.ModalBody([
                    html.Div(
                        id='content-modal-admin'
                    )

            ])
        ],id='modal-admin')
    ], style={'position':'fixed'}, md=2)

    return layout


                                # ======== *CALLBACKS* ======== #

                                # ======== OPEN MODAL N CLICKS ======== #


@dash_app.callback(
    [Output('modal-admin', 'is_open'),
     Output('modal-title', 'children'),
     Output('content-modal-admin', 'children')],
     [Input('open-modal-parametro', 'n_clicks'),
     Input('open-modal-insight', 'n_clicks')],
     State('modal-admin', 'is_open')
)
def toggle_modal(n1,n2,is_open):

    ctx = dash.callback_context

    if not ctx.triggered:
        return False, None, ''
    button_id = ctx.triggered[0]['prop_id'].split('.')[0]

    if button_id == 'open-modal-insight':
        modal_title = 'Novo Insight'
        modal_content = dbc.Tabs(tabs_insights)
        return True, modal_title, modal_content

    elif button_id == 'open-modal-parametro':
        modal_title = 'Parâmetros'
        modal_content = dbc.Tabs(tabs_params)
        return True, modal_title, modal_content



                                # ======== LAYOUTS ======== #


@dash_app.callback(
    Output('content-input-pe', 'children'),
    Input('input-text-operação','value')
)
def render_input_pe_layout(value):
    if value is None:
        raise PreventUpdate
    else:
        return PE_dict[value]


@dash_app.callback(
    Output('content-input-swing', 'children'),
    Input('input-text-operação-swing','value')
)
def render_input_swing_layout(value):
    if value is None:
        raise PreventUpdate
    else:
        return SWING_dict[value]


                                # ======== SWING TRADE ======== #


@dash_app.callback(
    Output('output-valor-entrada-swing', 'children'),
    [Input('entrada-swing-input', 'value')]
)
def render_output_swingTrade_entrada(inputEntrada):

    if inputEntrada is None:
        return 'R$ - '
    else:
        return f'R${inputEntrada}'


@dash_app.callback(
    Output('output-valor-stop-swing','children'),
    [Input('stop-swing-input', 'value'),
     Input('entrada-swing-input', 'value')]
)
def render_output_swingTrade_stop(inputStop, inputEntrada):
    if inputEntrada is None:
        if inputStop is None:
            return 'R$ - '
        else:
            return f'R${inputStop}'
    else:
        percStop = round(((inputStop - inputEntrada) / inputEntrada) * 100, 1)
        if inputStop is None:
            return 'R$ - | %'
        else:
            return f'R${inputStop} | {percStop}%'


@dash_app.callback(
    Output('output-valor-alvo-swing', 'children'),
    [Input('alvo-swing-input', 'value'),
     Input('entrada-swing-input', 'value')]
)
def render_output_swingTrade_alvo(inputAlvo, inputEntrada):
    if inputEntrada is None:
        if inputAlvo is None:
            return 'R$ - '
        else:
            return f'R${inputAlvo}'
    else:
        percAlvo = round(((inputAlvo - inputEntrada) / inputEntrada) * 100, 1)
        if inputAlvo is None:
            return 'R$ - | %'
        else:
            return f'R${inputAlvo} | {percAlvo}%'


@dash_app.callback(
    [Output('input-drop-ativo-long','value'),
     Output('input-drop-ativo-short','value'),
     Output('switch-button','n_clicks')],
    [Input('input-drop-ativo-short','value'),
     Input('input-drop-ativo-long','value'),
     Input('switch-button','n_clicks')],
)
def switch_update(inputShort,inputLong,n_clicks):
    if n_clicks is None:
        raise PreventUpdate
    else:
        return inputShort, inputLong, None


                                # ======== P.E. ======== #


@dash_app.callback(
    Output('output1', 'children'),
    Input('input1','value')
)
def render_input_pe1(value):
    if value is None:
        return ' - %'
    return f'{value}%'


@dash_app.callback(
    Output('output2', 'children'),
    Input('input2','value')
)
def render_input_pe2(value):
    if value is None:
        return ' - %'
    return f'{value}%'


@dash_app.callback(
    Output('output3', 'children'),
    Input('input3','value')
)
def render_input_pe3(value):
    if value is None:
        return ' - %'
    return f'{value}%'


@dash_app.callback(
    Output('output4', 'children'),
    Input('input4','value')
)
def render_input_pe4(value):
    if value is None:
        return ' - %'
    return f'{value}%'


@dash_app.callback(
    Output('output5', 'children'),
    Input('input5','value')
)
def render_input_pe5(value):
    if value is None:
        return ' - %'
    return f'{value}%'


@dash_app.callback(
    Output('output6', 'children'),
    Input('input6','value')
)
def render_input_pe6(value):
    if value is None:
        return ' - %'
    return f'{value}%'

@dash_app.callback(
    Output('output7', 'children'),
    Input('input7','value')
)
def render_input_pe7(value):
    if value is None:
        return ' - %'
    return f'{value}%'


@dash_app.callback(
    Output('datepicker-output', 'children'),
    Input('datepicker','date')
)
def render_input_pe_date(value):
    if value is None:
        return '-'
    else:
        value = datetime.strptime(value, '%Y-%m-%d')
        today = datetime.today()
        days_difference = (value - today).days
        return f'{value.strftime("%Y-%m-%d")} ({days_difference} d.c.)'


                                # ======== PARAMS ======== #
@dash_app.callback(
    Output('output1-params', 'children'),
    [Input('input1-params', 'value')]
)
def render_input_params(value):
    if value is None:
        return 'Monitorar: > %'
    else:
        return f'Monitorar: > {value}%'

@dash_app.callback(
    Output('output2-params', 'children'),
    [Input('input2-params', 'value')]
)
def render_input_params(value):
    if value is None:
        return 'Monitorar: > %'
    else:
        return f'Monitorar: > {value}%'

@dash_app.callback(
    Output('output3-params', 'children'),
    [Input('input3-params', 'value')]
)
def render_input_params(value):
    if value is None:
        return 'Monitorar: > %'
    else:
        return f'Monitorar: > {value}%'

@dash_app.callback(
    Output('output4-params', 'children'),
    [Input('input4-params', 'value')]
)
def render_input_params(value):
    if value is None:
        return 'Monitorar: > %'
    else:
        return f'Monitorar: > {value}%'

@dash_app.callback(
    Output('output5-params', 'children'),
    [Input('input5-params', 'value')]
)
def render_input_params(value):
    if value is None:
        return 'Mínimo: %'
    else:
        return f'Mínimo: {value}%'