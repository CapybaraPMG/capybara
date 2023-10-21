from pathlib import Path

# get the resources folder in the tests folder
resources = Path(__file__).parent / "resources"

def test_health_check(client):
    response = client.get("/health")
    assert response.status_code == 200