""" Diseño codigo para app"""
"Buenas tardes"
'''
Integrantes:
Daniela Cerquera
Daniel Baquero
Johan Peñaloza
'''
import dash
import dash_bootstrap_components as dbc

app = dash.Dash(__name__,external_stylesheets=[dbc.themes.BOOTSTRAP])

<<<<<<< Updated upstream
from Frontend.frontend import layout

app.layout = layout
=======

variable_1_cen = dbc.Container([
    html.H1("Texto 1 cen")
])
#app.layout = layout
>>>>>>> Stashed changes

if __name__ =='__main__':
    app.run_server(debug=True)
