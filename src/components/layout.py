from dash import Dash, dcc, html

from . import city_dropdown, country_dropdown, rank_slider, pie_chart_types, schema_table, show_table
from . import checklist, program_dropdown, map, info

def create_layout(app: Dash,db):

    return html.Div([
        dcc.Tabs([
            dcc.Tab(label='Database description', children=[
                # html.Div(
                #     className="chart-container",
                #     children=[
                #         pie_chart_types.render(app,db)
                #     ]
                # ),
                html.Div(
                    className="table-container",
                    children=[
                        schema_table.render(app,db,"universities"),
                        schema_table.render(app,db,"master_degrees")
                    ]
                ),
                info.render(app,db)
            ]),
            dcc.Tab(label='Filters', children=[
                html.H4('Select filters:'),
                html.Div(
                    className="dropdown-container",
                    children=[
                        country_dropdown.render(app,db),
                        city_dropdown.render(app,db),
                        program_dropdown.render(app,db)
                    ],
                    style={'margin-bottom': '20px'}
                ),
                html.Div(
                    className="slider-container",
                    children=[
                    rank_slider.render(app,db),
                        # checklist.render(app)
                    ]
                ),
                html.Div(
                    className="table-container-show",
                    children=[
                        show_table.render(app,db),
                    ]
                ),
                dcc.Store(id="store"), html.Div(id="trigger")
            ]),
            dcc.Tab(label='Map', children=[
                map.render(app,db)
            ]),
        ])
    ])
