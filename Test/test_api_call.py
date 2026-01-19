from unittest.mock import patch,Mock
import api_call
import requests
import pytest

# Test case 1: Successful API Response
def test_fetch_data_success():

       # Create a fake response object#
       # Arrange
       fake_response = Mock()
       expected_data = {"key": "value"}
       fake_response.json.return_value = expected_data

       #Patch requests.get so it returns the fake response#
       #Act
       with patch("api_call.requests.get", return_value = fake_response) as mock_get:
        result = api_call.fetch_data()

       # Assert
       mock_get.assert_called_once_with("https://api.example.com/data") # Check that requests.get was called once with the correct URL
       assert result == {"key": "value"} # Check that the function returns the expected JSON

