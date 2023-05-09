from . import ids
from dash import Dash, dcc, html
from dash.dependencies import Input, Output


def render(app: Dash,db):

    my_cursor = db.cursor()
    my_cursor.execute("SELECT DISTINCT country FROM universities")
    results = my_cursor.fetchall()
    
    countries = [result[0] for result in results]
    
    my_cursor.close()

    return html.Div([
                html.Label("Country:"),
                dcc.Dropdown(
                id=ids.COUNTRY,
                options=[{'label': country, 'value': country} for country in countries],
                value = "None"
                )
            ])
                

