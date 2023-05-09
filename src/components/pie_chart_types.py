from . import ids
from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

def render(app: Dash, db):

    @app.callback(
        Output(ids.TYPE_CHART,"figure"),
        Input(ids.COUNTRY,"value")
    )
    def update_pie_chart(country):

        # my_cursor = db.cursor()
        # if country == None:
        #     query = ("SELECT program_type, COUNT(id) AS n_type "
        #         "FROM master_degrees "
        #         "GROUP BY program_type "
        #         "HAVING n_type > 100 "
        #         "ORDER BY n_type DESC")
        #     my_cursor.execute(query)
        # else:
        #     query = ("SELECT program_type, COUNT(master_degrees.id) AS n_type "
        #              "FROM master_degrees JOIN universities ON universities.id = master_degrees.university_id "
        #              "WHERE country = %s "
        #              "GROUP BY program_type "
        #              "ORDER BY n_type DESC")

        
            # my_cursor.execute(query,(country,))
        print(country)
        print(type(country))
        my_cursor = db.cursor()
        query = ("select program_type, count(master_degrees.id) as n_type from master_degrees join universities on universities.id = master_degrees.university_id group by program_type order by n_type desc")
        my_cursor.execute(query)
        sleep(1)
        results = my_cursor.fetchall()

        my_cursor.close()

        df = pd.DataFrame(results, columns=['program_type', 'n_type'])

        fig = px.pie(df, values='n_type', names='program_type', title='Master Degrees by Program Type')
        return fig
    
    return html.Div(html.Label('Pie chart:'),
                    id=ids.TYPE_CHART)