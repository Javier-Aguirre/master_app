# Import packages
from dash import Dash, html, dash_table, dcc
import pandas as pd
import plotly.express as px
from dash.dependencies import Input, Output

# Incorporate data
data_path = "./Data/"
df = pd.read_csv(data_path+"processed_data.csv")

# Initialize the app
app = Dash(__name__)

# App layout


app.layout = html.Div([
    dcc.Tabs([
        dcc.Tab(label='Data selection', children=[
            html.H4('Country:'),
            dcc.Dropdown(
                df.country_name.unique(),
                'Belgium',
                id= 'countries-dropdown'
            ),
            html.H4('City:'),
            dcc.Dropdown(
                id= 'city-dropdown',
            )
            
        ]),
        dcc.Tab(label='Tab two',children= [
            html.Div([dcc.Graph(
                figure={
                    'data': [
                        {'x': [1, 2, 3], 'y': [1, 4, 1],
                            'type': 'bar', 'name': 'SF'},
                        {'x': [1, 2, 3], 'y': [1, 2, 3],
                        'type': 'bar', 'name': u'Montréal'},
                    ]
                }
            )]),
            html.Div([dcc.Graph(
                figure={
                    'data': [
                        {'x': [1, 2, 3], 'y': [2, 4, 3],
                            'type': 'bar', 'name': 'SF'},
                        {'x': [1, 2, 3], 'y': [5, 4, 3],
                        'type': 'bar', 'name': u'Montréal'},
                    ]
                }
            )
            ])            
        ]),
        dcc.Tab(label='Tab three', children=[
            dcc.Graph(
                figure={
                    'data': [
                        {'x': [1, 2, 3], 'y': [2, 4, 3],
                            'type': 'bar', 'name': 'SF'},
                        {'x': [1, 2, 3], 'y': [5, 4, 3],
                         'type': 'bar', 'name': u'Montréal'},
                    ]
                }
            )
        ]),
    ])
])

@app.callback(
    Output('city-dropdown', 'options'),
    Input('countries-dropdown', 'value'))
def set_cities_options(selected_country):
    return df.city[df['country_name'] ==selected_country].unique()

@app.callback(
    Output('city-dropdown', 'value'),
    Input('city-dropdown', 'options'))
def set_cities_value(available_options):
    return available_options[0]

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
