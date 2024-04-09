import json

import requests
import pytest
from lib.base_case import BaseCase
from lib.assertions import Assertions
from lib.my_requests import MyRequests


class TestAuth(BaseCase):
    def test_auth_user_activity(self):
        data = {
            "username": "79999997755",
            "password": "263898"
        }
        response = MyRequests.post("/auth/login/", data=data)
        expected_value = ['access_token', 'refresh_token', 'token_type', 'access_token_expires',
                          'refresh_token_expires']
        Assertions.assert_json_has_keys(response, expected_value)
        Assertions.assert_code_status(response, 200)

    def test_auth_user_superuser(self):
        data = {
            "username": "garpix@garpix.com",
            "password": "garpix911_demo"
        }
        response = MyRequests.post("/auth/login/", data=data)
        expected_value = ['access_token', 'refresh_token', 'token_type', 'access_token_expires',
                          'refresh_token_expires']
        Assertions.assert_json_has_keys(response, expected_value)
        Assertions.assert_code_status(response, 200)

    def test_auth_user_staff(self):
        data = {
            "username": "79999996655",
            "password": "123456йЙ"
        }
        response = MyRequests.post("/auth/login/", data=data)
        expected_value = ['access_token', 'refresh_token', 'token_type', 'access_token_expires',
                          'refresh_token_expires']
        Assertions.assert_json_has_keys(response, expected_value)
        Assertions.assert_code_status(response, 200)

    def test_auth_user_viewer(self):
        data = {
            "username": "79999995555",
            "password": "123456йЙ"
        }
        response = MyRequests.post("/auth/login/", data=data)
        expected_value = ['access_token', 'refresh_token', 'token_type', 'access_token_expires',
                          'refresh_token_expires']
        Assertions.assert_json_has_keys(response, expected_value)
        Assertions.assert_code_status(response, 200)
