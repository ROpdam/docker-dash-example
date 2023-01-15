import numpy as np
from app.functions import _data_size, create_data, create_lr_preds


def test_create_data():
    # Test with std = 0.5
    data = create_data(0.5)
    x, y = data[0], data[1]
    assert x.shape == (_data_size,)
    assert y.shape == (_data_size,)
    assert x[0] == 0
    assert x[-1] == _data_size - 1
    # assert np.std(y[1:] / x[1:]) == pytest.approx(0.5 / 10, rel=0.1)


def test_create_lr_preds():
    data = np.stack([np.arange(0, 10), np.arange(0, 10)])
    std = 0.5

    r_sq, preds = create_lr_preds(data, std)
    assert isinstance(r_sq, float)
    assert isinstance(preds, np.ndarray)
    assert preds.shape == (10,)
    # assert preds == pytest.approx(data[1], abs=0.001)
    # assert r_sq == pytest.approx(1, abs=0.001)
