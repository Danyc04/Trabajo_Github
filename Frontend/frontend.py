import dash
from dash import html 
import dash_bootstrap_components as dbc  

from Estructuras.Central import Central
from Estructuras.Navegador import Navegador
from Estructuras.Inferior_der import Derecha
from Estructuras.Inferior_izq import Izquierda

layout = dbc.Container( [
    dbc.Row([
        dbc.Col(Navegador, md=12,style={'background-color': 'orange'}),
        dbc.Col(Central, md=12,style={'background-color': 'white'}),
        dbc.Col(Izquierda, md=6,style={'background-color': 'blue'}),
        dbc.Col(Derecha, md=6,style={'background-color': 'red'})
    ])
])


