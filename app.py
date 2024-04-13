""" Diseño codigo para app"""
"Buenas tardes"
'''
Integrantes:
Daniela Cerquera
Daniel Baquero
Johan Peñaloza
'''
import dash
from dash import html 
import dash_bootstrap_components as dbc  

#from fronted.fronted import layout

app = dash.Dash(__name__,external_stylesheets=[dbc.themes.BOOTSTRAP])

#app.layout = layout

if __name__ =='__main__':
    app.run_server(debug=True)
