import json
import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    return app.test_client()

def test_home_route(client):
    response = client.get('/')
    assert response.status_code == 200
    data = response.get_json()
    assert "message" in data
    assert "features" in data

def test_analyze_employee_data_empty(client):
    response = client.post('/analyze_employee_data', json={})
    assert response.status_code == 400
    assert "error" in response.get_json()

def test_analyze_employee_data_valid(client):
    sample_data = {
        "employee_data": [
            {"name": "Alice", "age": 30, "score": 80},
            {"name": "Bob", "age": 35, "score": 90}
        ]
    }
    response = client.post('/analyze_employee_data', data=json.dumps(sample_data), content_type='application/json')
    assert response.status_code == 200
    data = response.get_json()
    assert "analysis" in data
