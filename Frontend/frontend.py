from dash import html 
import dash_bootstrap_components as dbc  

from Estructuras.Inferior_izq import oferta_izq
from Estructuras.Navegador import var_navegador

layout = dbc.Container( [
    dbc.Row([
        dbc.Col(var_navegador, md=12,style={'background-color': 'aquamarine'}),
        dbc.Col("Central", md=12,style={'background-color': 'white'}),
        dbc.Col(oferta_izq, md=6,style={'background-color': 'blue'}),
        dbc.Col("oferta_der", md=6,style={'background-color': 'red'})
    ])
])