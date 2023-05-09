from . import ids
from dash import Dash, dcc, html
import dash_table
import pandas as pd
from dash.dependencies import Input, Output


# def render(app: Dash, db):


#     my_cursor = db.cursor()
#     my_cursor.execute("SELECT program_name, universities.university_name, country, city, world_rank FROM universities JOIN master_degrees ON universities.id = master_degrees.university_id ORDER BY world_rank")
#     columns = my_cursor.fetchall()

    

#     df =  pd.DataFrame(columns, columns=['Program', 'University', 'Country', 'City', 'Rank'])
#     @app.callback(
#         Output(ids.TABLE,"children"),
#         [Input(ids.COUNTRY,"value"),
#          Input(ids.CITY,"value"),
#          Input(ids.CHECKLIST,"value")],
#     )
#     def get_table(country,city,check):
#         if (country and ("country" in check)):
#             df_filtered = df[df.Country==country]
#             if (city and ("City" in check)):
#                 df_filtered = df_filtered[df_filtered.City==city]
#         else:
#             df_filtered = df.copy()

#         df_filtered = df_filtered.head(5)
#         result = dash_table.DataTable(
#             id=ids.TABLE,
#             columns=[{"name": i, "id": i} for i in df_filtered.columns],
#             data=df_filtered.to_dict('records')
#         )
#         print(result)
#         return html.Div(result)
    

#     return html.Div([html.Label('Best programs:'),
#                      html.Table(id = ids.TABLE)])


def render(app: Dash, db):
    my_cursor = db.cursor()
    my_cursor.execute("SELECT program_name, universities.university_name, country, city, world_rank, tuition, quality_of_education, alumni_employment, publications, influence, citations, broad_impact, patents  FROM universities JOIN master_degrees ON universities.id = master_degrees.university_id ORDER BY world_rank")
    columns = my_cursor.fetchall()

    df = pd.DataFrame(columns, columns=['Program', 'University', 'Country', 'City', 'Rank', 'Tuition',"Education", "Employment", "Publications", "Influence", "Citations", "Impact", "Patents"])

    @app.callback(
        Output(ids.TABLE, "data"),
        [Input(ids.COUNTRY, "value"),
         Input(ids.CITY, "value"),
         Input(ids.CHECKLIST, "value"),
         Input(ids.PROGRAM,"value"),
         Input(ids.SLIDER, "value"),
         Input(ids.ORDER,"value")]
    )
    def update_table(country, city, check, program, tuition, col):
        df_filtered = df.copy()

        if "country" in check and country:
            df_filtered = df_filtered[df_filtered.Country == country]

        if "City" in check and city:
            df_filtered = df_filtered[df_filtered.City == city]
        
        if "Program" in check and program:
            df_filtered = df_filtered[df_filtered.Program.apply(lambda x: x in program)]

        df_filtered = df_filtered[df_filtered.Tuition.apply(lambda x: (x<tuition[1] and x >tuition[0]))]
        df_filtered = df_filtered.sort_values(by=[col]).head(20)

        return df_filtered.to_dict('records')

    return html.Div([
        html.Div(className="table-filter-order", children = [
        html.Div([html.Label('Filter by:'),
        dcc.Checklist(
            id=ids.CHECKLIST,
            options=[{'label': 'Country', 'value': 'country'},
                     {'label': 'City', 'value': 'City'},
                     {'label': 'Program', 'value': 'Program'}],
            value=[],
            )]),
        html.Div([html.Label('Order by:'),
        dcc.RadioItems(
            id=ids.ORDER,
            options=[{'label': col, 'value': col} for col in df.columns[-9:]],
            value="Rank",
            inline=True
            )
        ])
        ]),
        dash_table.DataTable(
            id=ids.TABLE,
            columns=[{"name": i, "id": i} for i in df.columns],
            data=[],
        )
    ])