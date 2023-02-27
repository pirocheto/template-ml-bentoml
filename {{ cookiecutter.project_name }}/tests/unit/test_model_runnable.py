from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.base import BaseEstimator

from app.service import ModelRunnable

# pylint: disable=redefined-outer-name,unused-argument

PROJECT_DIR = Path(__file__).parents[2] / "app"
MODEL_PATH = PROJECT_DIR / "models/rf"


def test_model_runnable_initialization():
    model_runnable = ModelRunnable(MODEL_PATH)
    assert isinstance(model_runnable._model, BaseEstimator)  # pylint: disable=protected-access


def test_model_runnable_predict():
    model_runnable = ModelRunnable(MODEL_PATH)
    input_data = pd.DataFrame(
        [
            {
                "sepal length (cm)": 5.1,
                "sepal width (cm)": 3.5,
                "petal length (cm)": 1.4,
                "petal width (cm)": 0.2,
            },
            {
                "sepal length (cm)": 7.0,
                "sepal width (cm)": 3.2,
                "petal length (cm)": 4.7,
                "petal width (cm)": 1.4,
            },
        ]
    )

    predictions = model_runnable.predict(input_data)
    assert isinstance(predictions, np.ndarray)
    assert len(predictions) == len(input_data)
