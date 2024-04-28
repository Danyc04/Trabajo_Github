from dash import html, dcc
import dash_bootstrap_components as dbc
import pandas as pd

from Backend.backend import cotizacion

central_arriba = dbc.Container([
    dbc.Row([
        dbc.Col(
            dcc.Dropdown(['Bogota'], value='Origen'),
            md=2,
            style={'border': f'1px solid darkmagenta', 'color':'darkmagenta'}
        ),
        
        dbc.Col(
            dcc.Dropdown(
                options= [{'label': dest, 'value': dest} for dest in cotizacion['Destino'].unique()],
                value= 'Destino',
                id='destino_consultado'
                ),
            md=2,
            style={'border': f'1px solid darkmagenta', 'color':'darkmagenta'}
        ),
            
        dbc.Col(dcc.RadioItems(
            options=[
                {'label': ' Temporada alta', 'value': 'Temporada alta'},
                {'label': ' Temporada baja', 'value': 'Temporada baja'}],
                id='temporada'),
                md=4,
                style={'border': f'1px solid darkmagenta', 'color':'darkmagenta'},
                ),
        
        dbc.Col(dcc.Input(id='cantidad_personas',
                          type='number', value = "Personas"),
                          md=2, style={'border': f'1px solid darkmagenta', 'color':'darkmagenta'}),
        
        dbc.Col(dcc.Input(id='cantidad_dias', type='number', value = "Días"),
                md=2, style={'border': f'1px solid darkmagenta', 'color':'darkmagenta'}),
    ])
        ])


central_abajo = dbc.Container([
    html.Div(dbc.Row([
        dbc.Col(dbc.Button(["  Buscar  "],
                           id='buscar',
                           style={'textAlign': 'center',
                                  'backgroundColor': 'darkmagenta',
                                  'border': f'1px solid darkmagenta',
                                  'color':'lavenderblush'}),
                                  md={'size': 6, 'offset': 3}, className='text-center'),
                                  ])),
    dbc.Row([
        dbc.Col(
            
        )
    ])
    ])