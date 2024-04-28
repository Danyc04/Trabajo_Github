from dash import html
import dash_bootstrap_components as dbc
import base64

global oferta_der

with open('bd\imagen 2.png', 'rb') as img_file:
    encoded_img = base64.b64encode(img_file.read()).decode('ascii')

oferta_der = html.Div([
    html.H3("Aprovecha esta increíble oferta"),
    html.Img(src=f'data:image/png;base64,{encoded_img}', style={'width': '50%', 'height': 'auto'}),
    html.P("Dale click para mayor información")
])