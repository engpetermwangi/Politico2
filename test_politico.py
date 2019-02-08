import pytest
from politico import app

app.config["TESTING"] = True
client = app.test_client()


def test_create_political_party_given_complete_data():
    data = {
        "id": 1,
        "name": "Jubilee",
        "hqAddress": "Jubilee Towers",
        "logoUrl": "www.logopics.com/Jubilee",
    }
    response = client.post("/parties", json=data)
    assert response.status_code == 201


def test_create_political_party_given_incomplete_data():
    data = None
    response = client.post("/parties", json=data)
    assert response.status_code == 400


def test_get_all_political_parties():
    response = client.get("/parties")
    assert response.status_code == 200


if __name__ == "__main__":
    pytest.main()
