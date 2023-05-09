from . import ids
from dash import Dash, dcc, html
import dash_table
import pandas as pd


def render(app: Dash, db,table):

    my_cursor = db.cursor()
    my_cursor.execute(f"DESCRIBE {table}")
    columns = my_cursor.fetchall()


    df = pd.DataFrame(columns, columns=['Field', 'Type', 'Null', 'Key', 'Default', 'Extra'])
    df['Type'] = df['Type'].astype(str).apply(lambda x: x[2:-1])
    # create Dash DataTable
    result = dash_table.DataTable(
        id=f'{table}-schema',
        columns=[{"name": i, "id": i} for i in df.columns],
        data=df.to_dict('records')
    )

    return html.Div([html.Label(f'{table.capitalize()} schema:'),
                     result])