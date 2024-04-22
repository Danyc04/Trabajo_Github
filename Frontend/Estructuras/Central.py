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
        dbc.Col("Buscar", md=2, style={'border': f'1px solid darkmagenta', 'color':'darkmagenta'})
        ])),
    dbc.Row([
        dbc.Col(dcc.Checklist(["Botón ida y regreso"]), md=12)
        ])
    ])

central_abajo = dbc.Container([
    dbc.Row([
        dbc.Col(dcc.Checklist(["  Hotel"]), md=6, style={'border': f'1px solid darkmagenta', 'color':'darkmagenta'}),
        dbc.Col(dcc.Checklist(["  Vuelos"]), md=6, style={'border': f'1px solid darkmagenta', 'color':'darkmagenta'}),
       ]),
    dbc.Row([
        dbc.Col("Seleccione los servicios a reservar", md=12),
        ])
    ])