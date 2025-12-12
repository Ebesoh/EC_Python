from unittest.mock import patch
import Services
def test_email():
    with patch("Services.EmailService") as MockEmail:
        instance = MockEmail.return_value
        instance.send.return_value = True

        service = Services.EmailService()
        result = service.send("user@example.com", "Hi")

    assert result is True
    instance.send.assert_called_once()
