from dash import html, dcc
import dash_bootstrap_components as dbc

global central_arriba, central_abajo
central_arriba = dbc.Container([
    dbc.Row([
        dbc.Col("Origen", md=2, style={'border': f'1px solid darkmagenta', 'color':'darkmagenta'}),
        dbc.Col("Destino", md=2, style={'border': f'1px solid darkmagenta', 'color':'darkmagenta'}),
        dbc.Col("Fecha ida (y regreso)", md=4, style={'border': f'1px solid darkmagenta', 'color':'darkmagenta'}),
        dbc.Col("Cantidad personas", md=2, style={'border': f'1px solid darkmagenta', 'color':'darkmagenta'}),
        dbc.Col("Buscar", md=2, style={'border': f'1px solid darkmagenta', 'color':'darkmagenta'})
        ]),
    dbc.Row([
        dbc.Col(dcc.Checklist(["Botón ida y regreso"]), md=12)
        ])
    ])

central_abajo = dbc.Container([
    dbc.Row([
        dbc.Col(dcc.Checklist(["  Hotel"]), md=3, style={'border': f'1px solid darkmagenta', 'color':'darkmagenta'}),
        dbc.Col(dcc.Checklist(["  Vuelos"]), md=3, style={'border': f'1px solid darkmagenta', 'color':'darkmagenta'}),
        dbc.Col(dcc.Checklist(["  Carro"]), md=3, style={'border': f'1px solid darkmagenta', 'color':'darkmagenta'}),
        dbc.Col(dcc.Checklist(["  Taxis aeropuerto"]), md=3, style={'border': f'1px solid darkmagenta', 'color':'darkmagenta'}),
        ]),
    dbc.Row([
        dbc.Col("Seleccione los servicios a reservar", md=12),
        ])
    ])