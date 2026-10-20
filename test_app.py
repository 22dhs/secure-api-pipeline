import pytest

from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_health_endpoint(client):
    response = client.get("/health")

    assert response.status_code == 200
    assert response.get_json() == {"status": "ok"}


def test_add_two_numbers(client):
    response = client.post(
        "/add",
        json={"a": 2, "b": 3},
    )

    assert response.status_code == 200
    assert response.get_json() == {"result": 5}


def test_add_rejects_strings(client):
    response = client.post(
        "/add",
        json={"a": "two", "b": 3},
    )

    assert response.status_code == 400


def test_add_rejects_boolean(client):
    response = client.post(
        "/add",
        json={"a": True, "b": 3},
    )

    assert response.status_code == 400


def test_add_rejects_non_object_json(client):
    response = client.post("/add", json=[2, 3])

    assert response.status_code == 400
