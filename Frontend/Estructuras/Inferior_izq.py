from dash import html
import dash_bootstrap_components as dbc
import base64

global oferta_izq

# with open('bd\imagen 1.jpg', 'rb') as img_file:
    # encoded_img = base64.b64encode(img_file.read()).decode('ascii')

oferta_izq = html.Div([
    html.H3("Aprovecha esta increíble oferta", style={'color':'indigo', 'textAlign': 'center'}),
    # html.Img(src='https://akm-img-a-in.tosshub.com/indiatoday/images/story/202206/kkconcertkol.jpg?VersionId=X69XgQi6xidSzzk93srjDt2DrVFJxghU;base64,{encoded_img}',
             # style={'width': '70%', 'height': 'auto', 'display': 'block', 'margin': 'auto'}),
    html.P("Dale click para mayor información", style={'textAlign': 'center'})
])
