import pytest


@pytest.fixture
def client():
    from app import app

    app.config.update(TESTING=True)
    with app.test_client() as test_client:
        yield test_client


def test_home_page(client):
    response = client.get("/")

    assert response.status_code == 200
    assert b"Annual income" in response.data
    assert b"Filing status" in response.data


def test_calculate_form(client):
    response = client.post(
        "/calculate", data={"income": "50000", "status": "single"}
    )

    assert response.status_code == 200
    assert b"Estimated tax: $6,307.50" in response.data


def test_health(client):
    response = client.get("/health")

    assert response.status_code == 200
    assert response.get_json() == {"status": "ok"}


def test_calculate_api(client):
    response = client.get("/api/calculate?income=50000&status=single")

    assert response.status_code == 200
    assert response.get_json() == {
        "income": 50000,
        "status": "single",
        "tax": 6307.5,
        "effective_rate": 6307.5 / 50000,
    }


def test_invalid_api_input_returns_400(client):
    response = client.get("/api/calculate?income=-1&status=single")

    assert response.status_code == 400
    assert "error" in response.get_json()


def test_invalid_form_input_returns_400(client):
    response = client.post(
        "/calculate", data={"income": "50000", "status": "unknown"}
    )

    assert response.status_code == 400
