from . import ids
from dash import Dash, dcc, html
from dash.dependencies import Input, Output


def render(app:Dash):


    return html.Div([
            html.H4('Filter by:'),
            dcc.Checklist(
                id=ids.CHECKLIST,
                options=[{'label': 'Country', 'value': 'country'},
                         {'label': 'City', 'value': 'City'}],
                value=[],
            )])