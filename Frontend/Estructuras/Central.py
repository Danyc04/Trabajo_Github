from dash import html, dcc
import dash_bootstrap_components as dbc

global central_arriba, central_abajo
central_arriba = dbc.Container([
    html.H5(dbc.Row([
        dbc.Col(dcc.Dropdown(
            ['origen','Bogota'], value='origen'), md=2, style={'border': f'1px solid darkmagenta', 'color':'darkmagenta'}),
            dbc.Col(dcc.Dropdown(
            ['Destino','Cartagena','Medellin','Barranquilla','Cali','Bucaramanga','Santa Marta'],
            value= 'Destino'),
            md=2, style={'border': f'1px solid darkmagenta', 'color':'darkmagenta'}),
        dbc.Col(dcc.RadioItems(['Temp alta', 'Temp baja']), md=4, style={'border': f'1px solid darkmagenta', 'color':'darkmagenta'}),
        dbc.Col(dcc.Dropdown(
            ['Personas','1','2','3','4','5'],
            value = "Personas"),
            md=2, style={'border': f'1px solid darkmagenta', 'color':'darkmagenta'}),
        dbc.Col(dcc.Dropdown(
            ['Dias','1','2','3','4','5'],
            value = "Dias"),
            md=2, style={'border': f'1px solid darkmagenta', 'color':'darkmagenta'}),
        ])),
        ])


central_abajo = dbc.Container([
    html.H2(dbc.Row([
        dbc.Col(dcc.Checklist(["  Buscar  "],style={'textAlign': 'center'}), md=12, style={'border': f'1px solid darkmagenta', 'color':'darkmagenta'}),
       ])),
    ])