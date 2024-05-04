from dash import html
import dash_bootstrap_components as dbc
import base64

global oferta_der

with open('bd/imagen 2.png', 'rb') as img_file:
    encoded_img = base64.b64encode(img_file.read()).decode('ascii')

oferta_der = html.Div([
    html.H3("Aprovecha esta increíble oferta", style={'color':'indigo', 'textAlign': 'center'}),
    html.Img(src=f'data:image/png;base64,{encoded_img}',
             style={'width': '70%', 'height': 'auto', 'display': 'block', 'margin': 'auto'}),
    html.P("Dale click para mayor información", style={'textAlign': 'center'})
])
