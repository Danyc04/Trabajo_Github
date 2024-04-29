from dash import html, dcc
import dash_bootstrap_components as dbc

global var_navegador

var_navegador = dbc.Container([
    html.H5(dbc.Row([
        dbc.Col("Cotiza tus paquetes de vuelos y hotel 4 estrellas",
                md=3, style={'border': f'2px solid indigo', 'color':'indigo'}),
        dbc.Col('Log In', md=5,
                style={'background-color': 'darkorchid',
                       'color':'lavenderblush', 'border': f'2px solid indigo'}),
        dbc.Col('COP', md=4, style={'background-color': 'darkorchid',
                                    'color': 'lavenderblush',  'border': f'2px solid indigo'}),
    ]))
])