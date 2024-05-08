from dash import html, dcc
import dash_bootstrap_components as dbc

from Backend.backend import cotizacion

central_arriba = dbc.Container([
    dbc.Row([
        dbc.Col([
            html.Label("Ingrese Origen: "),
            dcc.Dropdown(['Bogota'], value='Origen',
                         placeholder="Desde")],
                         md=2, style={'border': f'1px solid darkmagenta', 'color':'darkmagenta'}
        ),
        
        dbc.Col([
            html.Label("Ingrese Destino: "),
            dcc.Dropdown(
                options= [{'label': dest, 'value': dest} for dest in cotizacion['Destino'].unique()],
                value= 'Destino',
                id='destino_consultado',
                placeholder="Destino"
                )],
            md=2,
            style={'border': f'1px solid darkmagenta', 'color':'darkmagenta'}
        ),
            
        dbc.Col(dcc.RadioItems(
            options=[
                {'label': ' Temporada alta', 'value': 'TemporadaAlta'},
                {'label': ' Temporada baja', 'value': 'TemporadaBaja'}],
                id='temporada'),
                md=4,
                style={'border': f'1px solid darkmagenta', 'color':'darkmagenta'},
                ),
        
        dbc.Col([
            html.Label("Ingrese cantidad de personas: "),
            dcc.Input(id='cantidad_personas',
                          type='number', value = "Personas", placeholder="No. Personas")],
                          md=2, style={'border': f'1px solid darkmagenta', 'color':'darkmagenta'},
    ),
        
        dbc.Col([
            html.Label("Ingrese cantidad de días: "),
            dcc.Input(id='cantidad_dias', type='number', value = "Días", placeholder="No. Días")],
                md=2, style={'border': f'1px solid darkmagenta', 'color':'darkmagenta'}),
    ])
        ])

central_abajo = dbc.Container([
    html.Div(
        dbc.Row([
            dbc.Col(dbc.Button(["  Buscar  "],
                           id='buscar',
                           style={'textAlign': 'center',
                                  'backgroundColor': 'darkmagenta',
                                  'border': f'1px solid darkmagenta',
                                  'color':'lavenderblush'}),
                                  md={'size': 6, 'offset': 3}, className='text-center'),
                                  ])),
    html.Div(
        dbc.Row([
            dbc.Col(html.H3('El valor de la cotización es de: ', style={'color':'darkmagenta', 'offset': 1.5}), md=6),
            dbc.Col(html.H2(id = 'valor_formateado',
                            style={'color':'darkmagenta'}),md=6)
                            ]))
            ])