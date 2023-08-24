import json
import pytest
from flask import Flask
from order.order_controller import order_app


@pytest.fixture
def client():
    app = Flask(__name__)
    app.register_blueprint(order_app)
    app.config["TESTING"] = True
    client = app.test_client()
    yield client


def test_valid_order(client):
    """Test with valid order"""
    response = client.post('/orders?components=["A", "D", "F", "I", "K"]')
    data = json.loads(response.data)
    assert response.status_code == 201
    assert "order_id" in data
    assert "total" in data
    assert "parts" in data


def test_invalid_order_duplicate_category(client):
    """Test with invalid order have duplicate category"""
    response = client.post('/orders?components=["A", "D", "F", "I", "I"]')
    data = json.loads(response.data)
    assert response.status_code == 400
    assert "error" in data


def test_invalid_order_missing_category(client):
    """Test with invalid order have less order components"""
    response = client.post('/orders?components=["A", "D", "F", "I"]')
    data = json.loads(response.data)
    assert response.status_code == 400
    assert "error" in data


def test_invalid_order_missing_part(client):
    """Test with invalid order have less order components"""
    response = client.post('/orders?components= ["X", "Y", "Z"]')
    data = json.loads(response.data)
    assert response.status_code == 400
    assert "error" in data


def test_invalid_order_invalid_characters(client):
    """Test with invalid order have more order components"""
    response = client.post('/orders?components= ["A", "D", "F", "I", "K", "X"]')
    data = json.loads(response.data)
    assert response.status_code == 400
    assert "error" in data
