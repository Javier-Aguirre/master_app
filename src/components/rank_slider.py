from . import ids
from dash import Dash, dcc, html
from dash.dependencies import Input, Output


def render(app: Dash,db):

    my_cursor = db.cursor()
    my_cursor.execute("SELECT min(tuition) as min_t, max(tuition) as max_t FROM master_degrees JOIN universities ON universities.id = master_degrees.university_id")
    results = my_cursor.fetchall()[0]
    ranks = list(range(int(results[0]),int(results[1]),10000))+[int(results[1])]
    return html.Div([
        html.Label('Tuition:'),
        dcc.RangeSlider(
            id=ids.SLIDER,
            marks={str(rank): str(rank) for rank in ranks},
            min = min(ranks),
            max = max(ranks),
            value=[int(0.2*results[1]), int(0.8*results[1])],
        )
    ])

