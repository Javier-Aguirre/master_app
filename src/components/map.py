from . import ids
from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px
import geocoder
import geopy
import numpy as np




def render(app:Dash,db):


    @app.callback(
        Output(ids.MAP,"figure"),
        Input(ids.TABLE,"data")
    )
    def update_map(table):

        

        df = pd.DataFrame(table)
        coords = []
        for univ in df.University.unique():
            retries = 0
            while retries < 3:
                try:
                    loc = geocoder.bing(univ,key="AocVxas8IGt1ISKVIEXk7yGW4PrbxeD3pw-YSWZK4M3L2hSPwQjiCyCfH_5pfjIp").json
                    coords.append([loc['lat'], loc['lng']])
                    break
                except geopy.exc.GeocoderTimedOut:
                    retries += 1
                    continue
                # except:
                #     coords.append([np.nan, np.nan])
                #     break
        coords = np.array(coords)
        fig = px.scatter_mapbox(lat = coords[:, 0],
                                 lon = coords[:, 1],
                                 text = df.University.unique(),
                                 zoom = 1,
                                 size=[5 for _ in coords],
                                 width = 1200,
                                 height= 900,
                                 title = "Map of best universities by filter")
        fig.update_layout(mapbox_style = "open-street-map")
        fig.update_layout(margin = {"r":10,"t":50,"l":10,"b":10})

        return fig

    
    return html.Div(dcc.Graph(id=ids.MAP))

          

