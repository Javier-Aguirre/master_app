from . import ids
from dash import Dash, dcc, html
from dash.dependencies import Input, Output


def render(app: Dash,db):


    my_cursor = db.cursor()
    my_cursor.execute("SELECT count(DISTINCT program_name) FROM master_degrees")
    n_programs = my_cursor.fetchall()[0][0]

    my_cursor.execute("SELECT count(DISTINCT Country) FROM universities")
    n_countries = my_cursor.fetchall()[0][0]


    my_cursor.close()
    return html.Div([html.H5(f'Number of programs: {n_programs}'),
                     html.H5(f'Number of countries: {n_countries}')
            ])