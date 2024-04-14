import dash
from dash import html 
import dash_bootstrap_components as dbc  


layout = dbc.Container( [
    dbc.Row([
        dbc.Col("Navegador", md=12,style={'background-color': 'orange'}),
        dbc.Col("Central", md=12,style={'background-color': 'white'}),
        dbc.Col("Izquierda", md=6,style={'background-color': 'blue'}),
        dbc.Col("Derecha", md=6,style={'background-color': 'red'})
    ])
])


