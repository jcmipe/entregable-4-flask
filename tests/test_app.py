import importlib
import sys
from pathlib import Path

CODE_DIRECTORY = Path(__file__).resolve().parents[1] / "code"
sys.path.insert(0, str(CODE_DIRECTORY))

app_module = importlib.import_module("app")
app = app_module.app
GREETING_MESSAGE = app_module.GREETING_MESSAGE


def test_home_returns_expected_json_response() -> None:
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200
    assert response.is_json
    assert response.get_json() == {"message": GREETING_MESSAGE}
