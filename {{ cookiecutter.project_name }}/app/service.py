from typing import List

import bentoml
import pandas as pd
from bentoml.io import JSON
from mlem.api import load
from pydantic import BaseModel  # pylint: disable=no-name-in-module

SERVICE_NAME = "iris-classifier-test"
CLASS_NAMES = ["setosa", "versicolor", "virginica"]


class ModelRunnable(bentoml.Runnable):
    SUPPORTED_RESOURCES = ("cpu",)
    SUPPORTS_CPU_MULTI_THREADING = True

    def __init__(self, model_path: str):
        self._model = load(model_path)

    @bentoml.Runnable.method(
        batchable=True,
        batch_dim=0,
        input_spec=None,
        output_spec=None,
    )
    def predict(self, input_data):
        return self._model.predict(input_data)


runner = bentoml.Runner(
    ModelRunnable,
    name="runner_1",
    runnable_init_params={"model_path": "models/rf"},
)

svc = bentoml.Service(SERVICE_NAME, runners=[runner])


class Features(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float


class BatchInputData(BaseModel):
    features: List[Features]


class Output(BaseModel):
    features: Features
    prediction: str


class BatchOutputData(BaseModel):
    predictions: List[Output]


def monitor(features, predictions):

    with bentoml.monitor(SERVICE_NAME + "#predictions") as mon:
        mon.log_batch(
            features.sepal_length,
            name="sepal_length",
            role="feature",
            data_type="numerical",
        )
        mon.log_batch(
            features.sepal_width,
            name="sepal_width",
            role="feature",
            data_type="numerical",
        )
        mon.log_batch(
            features.petal_length,
            name="petal_length",
            role="feature",
            data_type="numerical",
        )
        mon.log_batch(
            features.petal_width,
            name="petal_width",
            role="feature",
            data_type="numerical",
        )

        mon.log_batch(
            predictions,
            name="prediction",
            role="prediction",
            data_type="categorical",
        )


@svc.api(
    input=JSON(pydantic_model=BatchInputData),
    output=JSON(pydantic_model=BatchOutputData),
)
def classify(features: BatchInputData) -> dict:
    input_df = pd.DataFrame.from_records(features.dict()["features"])
    input_df_prep = input_df.rename(
        {
            "sepal_length": "sepal length (cm)",
            "sepal_width": "sepal width (cm)",
            "petal_length": "petal length (cm)",
            "petal_width": "petal width (cm)",
        },
        axis=1,
    )

    preds_idx = runner.predict.run(input_df_prep)  # pylint: disable=no-name-in-module
    preds = [
        {"features": features.features[i], "prediction": CLASS_NAMES[pred_idx]} for i, pred_idx in enumerate(preds_idx)
    ]

    monitor(input_df, preds_idx)
    return {"predictions": preds}
