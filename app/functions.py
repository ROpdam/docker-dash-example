import numpy as np
from sklearn import linear_model #import LinearRegression
import plotly.graph_objects as go

_data_size = np.random.randint(100,600)

def plot_regression(std=10):
    _x_og = np.arange(0,_data_size)
    x = _x_og.reshape((-1, 1))
    y = _x_og * np.random.normal(size=_data_size, loc=10, scale=std)

    model = linear_model.LinearRegression().fit(x, y)
    r_sq = model.score(x, y)
    preds = model.predict(x)

    layout  = go.Layout(title="What if you change standard deviation?", height=700)
    fig = go.Figure(layout=layout)

    fig.add_trace(go.Scatter(x=_x_og, y=y, mode='markers', name=f'x * rand_norm(mean=10, std=x*{std})'))
    fig.add_trace(go.Line(x=_x_og, y=preds, name='linear regression'))

    return fig