from . import ids
from dash import Dash, dcc, html
from dash.dependencies import Input, Output


def render(app: Dash,db):


    my_cursor = db.cursor()
    my_cursor.execute("SELECT DISTINCT program_name FROM master_degrees JOIN universities ON universities.id = master_degrees.university_id")
    results = my_cursor.fetchall()

    programs = [result[0] for result in results]
    my_cursor.close()
    return html.Div([html.Label('Program:'),
            dcc.Dropdown(
                id=ids.PROGRAM,
                options=[{'label': program, 'value': program} for program in programs],
                value = "None",
                searchable=True,
                multi=True
                )
            ])