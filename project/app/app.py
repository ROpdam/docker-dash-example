import dash

import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import flask

from functions import plot_regression

server = flask.Flask(__name__)
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP], server=server)
server = app.server

app.layout = html.Div(
    [
        html.Div(
            "Regression fit example",
            style={
                "fontSize": 28,
                "marginLeft": "40px",
                "marginBottom": "50px",
                "font-weight": "bold",
                "marginTop": "20px",
            },
        ),
        html.Div(
            [
                dcc.Graph(id="regression_plot"),
                html.P(
                    "Standard Deviation", style={"color": "black", "marginLeft": "20px"}
                ),
                dcc.Slider(
                    id="std_slider",
                    min=0,
                    max=40,
                    step=0.5,
                    value=10,
                    marks={i: str(i) for i in range(0, 40, 5)},
                ),
            ],
            style={"background-color": "white", "color": "white"},
        ),
    ]
)


@app.callback(
    Output(component_id="regression_plot", component_property="figure"),
    [Input(component_id="std_slider", component_property="value")],
)
def update_regression_plot(std):
    return plot_regression(std)


if __name__ == "__main__":
    # app.run_server(debug=True)

    # To run with guvicorn go to /app and run 'guvicorn -b 0.0.0.0:8050 app:server'
    app.run_server(host="0.0.0.0", port=8050, debug=True)
