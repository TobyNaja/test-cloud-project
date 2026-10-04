import pytest
from app.app import app


@pytest.fixture
def client():
    app.config.update({"TESTING": True})
    with app.test_client() as client:
        yield client


def test_hello_route(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Hello Prodpai Cloud Demo" in response.data


def test_health_route(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json() == {"status": "healthy"}


def test_invalid_route_404(client):
    response = client.get("/wrong-path")
    assert response.status_code == 404