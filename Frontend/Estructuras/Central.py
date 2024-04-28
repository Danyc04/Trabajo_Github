from dash import html, dcc
import dash_bootstrap_components as dbc
import pandas as pd

from Backend.backend import cotizacion

ciudades_lista = cotizacion['Destino'].tolist()

global central_arriba, central_abajo

central_arriba = dbc.Container([
    html.H5(dbc.Row([
        dbc.Col(dcc.Dropdown(
            ['Bogota'], value='origen'), md=2, style={'border': f'1px solid darkmagenta', 'color':'darkmagenta'}),
            dbc.Col(dcc.Dropdown(cotizacion['Destino'].unique(), value= 'Destino', id='destino_consultado'),
            md=2, style={'border': f'1px solid darkmagenta', 'color':'darkmagenta'}),
        dbc.Col(dcc.RadioItems(['Temp alta', 'Temp baja']), md=4, style={'border': f'1px solid darkmagenta', 'color':'darkmagenta'}),
        dbc.Col(dcc.Input(id='cantidad_personas', type='number', value = "Personas"),
            md=2, style={'border': f'1px solid darkmagenta', 'color':'darkmagenta'}),
        dbc.Col(dcc.Input(id='cantidad_dias', type='number', value = "Días"),
            md=2, style={'border': f'1px solid darkmagenta', 'color':'darkmagenta'}),
        ])),
        ])


central_abajo = dbc.Container([
    html.H2(dbc.Row([
        dbc.Col(dcc.Checklist(["  Buscar  "],style={'textAlign': 'center'}), md=12, style={'border': f'1px solid darkmagenta', 'color':'darkmagenta'}),
       ])),
    ])