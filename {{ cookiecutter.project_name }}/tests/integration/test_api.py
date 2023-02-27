import time

import pytest
import requests

# pylint: disable=redefined-outer-name,unused-argument

URL = "http://localhost:3005"


def _wait_for_api_ready(timeout):
    start = time.time()

    while (time.time() - start) < timeout:
        time.sleep(1)

        try:
            resp = requests.get(URL + "/readyz", timeout=5)
            if resp.status_code == 200:
                return True
        except requests.ConnectionError:
            pass

    return False


@pytest.fixture(scope="module")
def session():
    if _wait_for_api_ready(10):
        yield
    else:
        raise TimeoutError(f"API hosted on '{URL}' is not ready")


def test_healthz(session):
    resp = requests.get(URL + "/healthz", timeout=5)
    assert resp.status_code == 200


def test_livez(session):
    resp = requests.get(URL + "/livez", timeout=5)
    assert resp.status_code == 200


def test_readyz(session):
    resp = requests.get(URL + "/readyz", timeout=5)
    assert resp.status_code == 200


def test_metrics(session):
    resp = requests.get(URL + "/metrics", timeout=5)
    assert resp.status_code == 200


def test_classify(session):
    input_data = {
        "features": [
            {
                "sepal_length": 5.1,
                "sepal_width": 3.5,
                "petal_length": 1.4,
                "petal_width": 0.2,
            },
            {
                "sepal_length": 7.0,
                "sepal_width": 3.2,
                "petal_length": 4.7,
                "petal_width": 1.4,
            },
        ]
    }

    resp = requests.post(URL + "/classify", json=input_data, timeout=5)
    assert resp.status_code == 200

    output = resp.json()
    assert len(input_data["features"]) == len(output["predictions"])
