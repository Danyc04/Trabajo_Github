import dash
from dash import html 
import dash_bootstrap_components as dbc  

layout = dbc.Container( [
    dbc.Row([
        dbc.Col('navegador', md=12,style={'background-color': 'orange'}),
        dbc.Col('central', md=12,style={'background-color': 'white'}),
        dbc.Col('inferior izq', md=6,style={'background-color': 'blue'}),
        dbc.Col('inferior der', md=6,style={'background-color': 'red'})
    ])
])


