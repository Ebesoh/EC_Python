from unittest.mock import patch,Mock
import api_call

def test_fetch_data():
    fake_response = Mock()
    fake_response.json.return_value = {"status": "ok"}

    with patch("api_call.requests.get", return_value = fake_response):
        result = api_call.fetch_data()

    assert result == {"status":"oki"}
