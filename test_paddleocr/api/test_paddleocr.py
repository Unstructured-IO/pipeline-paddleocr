from fastapi.testclient import TestClient


from prepline_paddleocr.api.app import app


def test_api_health_check():
    client = TestClient(app)
    response = client.get("/healthcheck")

    assert response.status_code == 200


def test_api_call():
    client = TestClient(app)
    with open("img/0.png", "rb") as f:
        response = client.post(
            "/paddleocr/v0.0.1/paddleocr", files={"files": ("filename", f, "image/jpeg")}
        )

    assert response.status_code == 200
