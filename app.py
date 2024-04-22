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
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate

from Frontend.frontend import layout
from Backend.backend import cotizacion_unica
app = dash.Dash(__name__,external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = layout

@app.callback(
    Output('precio', 'children'),
    Input('destino_consultado', 'value'),
    Input('cantidad_personas','value'),
    Input('cantidad_dias', 'value'),
    State('buscar', 'n_clicks')
)

def entrada_datos(destino_consultado, cantidad_personas, cantidad_dias, n_clicks):
    if n_clicks is None:
        raise PreventUpdate
    if destino_consultado is None:
        return 'Seleccione su ciudad de destino'
    if cantidad_personas is None:
        return 'Ingrese la cantidad de pasajeros'
    if cantidad_dias is None:
        return 'Ingrese la cantidad de días a cotizar'
    return cotizacion_unica(cantidad_personas, cantidad_dias)


if __name__ =='__main__':
    app.run_server(debug=True)
