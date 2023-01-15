import json
from typing import Union

import numpy as np
import plotly.graph_objects as go
from sklearn import linear_model

_data_size = 1000


def create_data(std: float) -> np.array:
    """Create x based on std and ceate a related y

    Args:
        std (float): standard deviation

    Returns:
        np.array: x and y stacked
    """
    x = np.arange(0, _data_size)
    noise = np.random.normal(size=_data_size, loc=1, scale=std / 10)
    y = x * (1 + noise)
    data = np.stack([x, y])

    return data


def create_lr_preds(data: np.array, std: float) -> Union[float, np.array]:
    """
    Creates random data based on input std and fits a linear
    regression model through this data

    Args:
        std (float): standard deviation for random data
        x (np.array): randomly generated std

    Returns:
        r_sq: R squared of the linear regression model
        preds: np.array with the predicitons
    """
    x = data[0, :].reshape(-1, 1)
    y = data[1, :]

    model = linear_model.LinearRegression().fit(x, y)
    r_sq = model.score(x, y)
    preds = model.predict(x)

    return r_sq, preds


def create_figure(**kwds) -> go.Figure:
    """Create a go.Figure plot using input data x and
    predicitons preds

    Args:
        x (np.array): input data
        preds (np.array): predictions

    Returns:
        go.Figure: plot showing input
        data (dots) and predictions (line)
    """
    layout = go.Layout(
        title=f"Regression fit example with R squared: {round(kwds['r_sq'], 3)}",
        height=700,
    )
    fig = go.Figure(layout=layout)

    fig.add_trace(
        go.Scatter(
            x=kwds["x"],
            y=kwds["y"],
            mode="markers",
            name=f"x * (1 + rand_norm(mean=1, std={kwds['std']}/10))",
        )
    )
    fig.add_trace(
        go.Scatter(x=kwds["x"], y=kwds["preds"], mode="lines", name="linear regression")
    )

    return fig


def style_figure(fig: go.Figure) -> go.Figure:
    """Style the figure according to the fig_layout.json

    Args:
        fig (go.Figure): Figure

    Returns:
        go.Figure: styled figure
    """
    f = open("assets/fig_layout.json")
    fig_layout = json.load(f)

    fig.update_layout(fig_layout)

    return fig


def plot_regression(std: float = 10) -> go.Figure:
    """Create a regression plot from random input data
    that varies with the standard deviation input

    Args:
        std (float, optional): standard deviation. Defaults to 10.

    Returns:
        go.Figure: go.Figure: plot showing input
        data (dots) and predictions (line)
    """
    data = create_data(std)
    r_sq, preds = create_lr_preds(data, std)

    fig = create_figure(std=std, r_sq=r_sq, x=data[0, :], y=data[1, :], preds=preds)
    fig = style_figure(fig)

    return fig
