from dash import html 
import dash_bootstrap_components as dbc  

from .Estructuras.Navegador import var_navegador
from .Estructuras.Inferior_izq import oferta_izq
from .Estructuras.Inferior_der import oferta_der
from .Estructuras.Central import central_arriba
from .Estructuras.Central import central_abajo

layout = dbc.Container([
    dbc.Row([
        dbc.Col(var_navegador, md=12),
        dbc.Col(central_arriba, md=12,style={'background-color': 'lavenderblush'}),
        dbc.Col(central_abajo, md=12,style={'background-color': 'lavenderblush'}),
        dbc.Col(oferta_izq, md=6,style={'background-color': 'thistle'}),
        dbc.Col(oferta_der, md=6,style={'background-color': 'plum'})
    ])
])