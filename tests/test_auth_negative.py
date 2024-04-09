from lib.base_case import BaseCase
from lib.assertions import Assertions
from lib.my_requests import MyRequests


class TestAuthNegative(BaseCase):
    def test_auth_user_empty_fields(self):
        data = {
            "username": "",
            "password": ""
        }
        response = MyRequests.post("/auth/login/", data=data)
        expected_value = {
            'username': ['Это поле не может быть пустым.'],
            'password': ['Это поле не может быть пустым.']
        }
        Assertions.assert_json_has_keys_with_partial_values(response, expected_value)
        Assertions.assert_json_has_not_key(response, "access_token")
        Assertions.assert_code_status(response, 400)

    def test_auth_user_without_fields(self):
        response = MyRequests.post("/auth/login/")
        expected_value = {
            'username': ['Обязательное поле.'],
            'password': ['Обязательное поле.']
        }
        Assertions.assert_json_has_keys_with_partial_values(response, expected_value)
        Assertions.assert_json_has_not_key(response, "access_token")
        Assertions.assert_code_status(response, 400)

    def test_auth_user_empty_fields_username(self):
        data = {
            "username": "",
            "password": "123456йЙ"
        }
        response = MyRequests.post("/auth/login/", data=data)
        expected_value = {
            'username': ['Это поле не может быть пустым.']
        }
        Assertions.assert_json_has_keys_with_partial_values(response, expected_value)
        Assertions.assert_json_has_not_key(response, "access_token")
        Assertions.assert_code_status(response, 400)

    def test_auth_user_empty_fields_password(self):
        data = {
            "username": "79999997755",
            "password": ""
        }
        response = MyRequests.post("/auth/login/", data=data)
        expected_value = {
            'password': ['Это поле не может быть пустым.']
        }
        Assertions.assert_json_has_keys_with_partial_values(response, expected_value)
        Assertions.assert_json_has_not_key(response, "access_token")
        Assertions.assert_code_status(response, 400)

    def test_auth_user_not_valid_data(self):
        data = {
            "username": "79793957655",
            "password": "123321Qq"
        }
        response = MyRequests.post("/auth/login/", data=data)
        expected_value = {
            'non_field_errors': ['Невозможно войти с предоставленными учетными данными.']
        }
        Assertions.assert_json_has_keys_with_partial_values(response, expected_value)
        Assertions.assert_json_has_not_key(response, "access_token")
        Assertions.assert_code_status(response, 400)
