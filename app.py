import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import pandas as pd
import numpy as np
import plotly.graph_objs as go

import time

df = pd.read_csv('testdata.csv')

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([

    dcc.Graph(id='testhistogramm'),
    html.Button(
        "render histogram",
        id="btn_render",
        type="submit",
        style={"width": "200px", "height": "100px"},
        className="row one-third column",
    ),
    
])


@app.callback(
    Output('testhistogramm', 'figure'),
    [Input('btn_render', 'n_clicks')])
def update_figure(n_clicks):
    start = time.time()
    if n_clicks is not None:

        timediff = [0.1] * df.shape[0]
        x = df["label1"]

        data = [
            go.Histogram(
                    histfunc="sum",
                    y=timediff,
                    x=x,
                    name="time(s)",
                    xbins=dict(start=min(x), end=max(x), size=100),
                    marker=dict(color="#ffa500"),
            ),
        ]



        end = time.time()
        elapsed = end - start

        figure3 = {
            "data": data,
            "layout": go.Layout(
                title="test histogramm ------ elapsed time: {}".format(elapsed),
                xaxis=dict(title="label1"),
                yaxis=dict(title="time"),
            ),
        }
        
        return figure3
    else:
        return {
            "data": [],
            "layout": go.Layout(
                title="test histogramm ",
                xaxis=dict(title="label1"),
                yaxis=dict(title="time"),
            ),
        }


if __name__ == '__main__':
    app.run_server(debug=True)