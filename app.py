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
from Backend.backend import consultarCotizacion
app = dash.Dash(__name__,external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = layout
server = app.server
@app.callback(
    Output('costo', 'children'),
    Input('buscar', 'n_clicks'),
    Input('destino_consultado', 'value'),
    Input('temporada', 'value'),
    Input('cantidad_personas','value'),
    Input('cantidad_dias', 'value')
)

def entrada_datos(n_clicks, destino_consultado, temporada, cantidad_personas, cantidad_dias):
    if n_clicks is None:
        raise PreventUpdate
    else:
        if destino_consultado is None:
            return html.Div('Seleccione su ciudad de destino', style={'fontSize': '20px'})
        else:
            if temporada is None:
                return html.Div('Seleccione la temporada a viajar', style={'fontSize': '20px'})  
            else:
                if cantidad_personas is None:
                    return html.Div('Ingrese la cantidad de pasajeros', style={'fontSize': '20px'})
                else:
                    if cantidad_dias is None:
                        return html.Div('Ingrese la cantidad de días a cotizar', style={'fontSize': '20px'})
                    
    return consultarCotizacion(destino_consultado, temporada, cantidad_personas, cantidad_dias)


if __name__ =='__main__':
    app.run_server(debug=True)
