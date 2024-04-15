from dash import html
import dash_bootstrap_components as dbc

global var_navegador

var_navegador = dbc.Container([
    dbc.Row([
        dbc.Col("Logo", md=3, style={'border': f'2px solid indigo', 'color':'indigo'}),
        dbc.Col('Desplegable, ?, y Login', md=9, style={'background-color': 'darkorchid', 'color':'lavenderblush'})
    ])
])