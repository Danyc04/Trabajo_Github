from dash import html, dcc
import dash_bootstrap_components as dbc

global var_navegador

var_navegador = dbc.Container([
    html.H5(dbc.Row([
        dbc.Col("Cotiza Ya", md=3, style={'border': f'2px solid indigo', 'color':'indigo'}),
        dbc.Col('Iniciar Sesion', md=5, style={'background-color': 'darkorchid', 'color':'lavenderblush'}),
        dbc.Col(dcc.Dropdown(['USD', 'COP', 'EUR'],
                             value= 'USD',
                             style={'background-color': 'darkorchid', 'color': 'black'}),
                             md=4),
    ]))
])