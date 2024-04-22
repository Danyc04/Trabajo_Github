from dash import html
import dash_bootstrap_components as dbc

global oferta_der

oferta_der = dbc.Container([
    html.Div([
    html.H3("SUPER OFERTA!!!! APROVEHA"),
    html.Img(src='bd\imagen 2.png', style={'width': '50%', 'height': 'auto'}),
])
])