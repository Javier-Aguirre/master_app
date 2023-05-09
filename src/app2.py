# Import packages
from src.components.layout import create_layout
from dash_bootstrap_components.themes import BOOTSTRAP
from dash import Dash, html, dcc
import pandas as pd
import plotly.express as px
from dash.dependencies import Input, Output

# Incorporate data
data_path = "./Data/"
df = pd.read_csv(data_path+"processed_data.csv")

# Initialize the app
def main() -> None:
    app = Dash(external_stylesheets=[BOOTSTRAP])
    app.title = "Medal dashboard"
    app.layout = create_layout(app)
    app.run()


if __name__ == "__main__":
    main()

# App layout
# Callbacks
# Callback for updating the options of the city dropdown based on the selected country
@app.callback(
    Output('city-dropdown', 'options'),
    Input('countries-dropdown', 'value')
)
def update_city_dropdown_options(selected_country):
    cities = df.loc[df['country_name'] == selected_country, 'city'].unique()
    return [{'label': city, 'value': city} for city in cities]

# Callback for updating the value of the city dropdown when the options change
@app.callback(
    Output('city-dropdown', 'value'),
    Input('city-dropdown', 'options')
)
def update_city_dropdown_value(options):
    return options[0]['value']

# Callback for updating the options of the university dropdown based on the selected city
@app.callback(
    Output('university-dropdown', 'options'),
    Input('city-dropdown', 'value')
)
def update_university_dropdown_options(selected_city):
    universities = df.loc[df['city'] == selected_city, 'university_name'].unique()
    return [{'label': university, 'value': university} for university in universities]

# Callback for updating the value of the university dropdown when the options change
@app.callback(
    Output('university-dropdown', 'value'),
    Input('university-dropdown', 'options')
)
def update_university_dropdown_value(options):
    return options[0]['value']

# Callback for updating the program type options based on the selected university
@app.callback(
    Output('program-type-dropdown', 'options'),
    Input('university-dropdown', 'value')
)
def update_program_type_dropdown_options(selected_university):
    program_types = df.loc[df['university_name'] == selected_university, 'program_type'].unique()
    return [{'label': program_type, 'value': program_type} for program_type in program_types]

# Callback for updating the program type value when the options change
@app.callback(
    Output('program-type-dropdown', 'value'),
    Input('program-type-dropdown', 'options')
)
def update_program_type_dropdown_value(options):
    return options[0]['value']

# Callback for updating the data table based on the selected filters
@app.callback(
    Output('datatable', 'data'),
    Input('countries-dropdown', 'value'),
    Input('city-dropdown', 'value'),
    Input('university-dropdown', 'value'),
    Input('program-type-dropdown', 'value')
)
def update_datatable(selected_country, selected_city, selected_university, selected_program_type):
    filtered_df = df.loc[
        (df['country_name'] == selected_country) &
        (df['city'] == selected_city) &
        (df['university_name'] == selected_university) &
        (df['program_type'] == selected_program_type)
    ]
    return filtered_df.to_dict('records')

@app.callback(
    Output('university-rank-range', 'value'),
    Input('university-rank-min', 'value'),
    Input('university-rank-max', 'value')
)
def update_university_rank_range(min_rank, max_rank):
    return [min_rank, max_rank]




# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)