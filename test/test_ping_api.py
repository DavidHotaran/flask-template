from app import app # can't do this bc app.py is not a module so cannot import
import pytest


@pytest.fixture()
def client(app):
    return app.test_client()

def test_ping_returns_200(client):
    response = client.get('/api/ping')
    assert response.status_code == 200