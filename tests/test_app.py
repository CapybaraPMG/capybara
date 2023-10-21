import json


def test_health_check(app, client):
    response = client.get("/health")
    assert response.status_code == 200
    expected = {"status": "Ok!", "message": "API is up and running"}
    assert expected == json.loads(response.get_data(as_text=True))
