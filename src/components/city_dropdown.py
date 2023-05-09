from . import ids
from dash import Dash, dcc, html
from dash.dependencies import Input, Output


def render(app: Dash,db):


    @app.callback(
        Output(ids.CITY, 'options'),
        Input(ids.COUNTRY, 'value')
    )
    def update_city_dropdown_options(selected_country):
        my_cursor = db.cursor()
        my_cursor.execute("SELECT DISTINCT city FROM universities JOIN master_degrees ON universities.id = master_degrees.university_id  WHERE country = '{0}'".format(selected_country))
        results = my_cursor.fetchall()

        cities = [result[0] for result in results]
        my_cursor.close()
        return cities
    return html.Div([html.Label('City:'),
            dcc.Dropdown(
                id=ids.CITY,
                options=[{'label': "None", 'value': "None"}],
                value = "None"
                )
            ])
    