import json

import requests
from requests import Response


class BaseCase:
    # Получение куки и проверка наличия ключа
    def get_cookie(self, response: Response, cookie_name):
        assert cookie_name in response.cookies, f"Cannot find cookie with name {cookie_name} in the last response"
        return response.cookies[cookie_name]

    # Получение заголовка и проверка наличия ключа
    def get_header(self, response: Response, headers_name):
        assert headers_name in response.headers, f"Cannot find header with name {headers_name} in the last response"
        return response.headers[headers_name]

    # Получение значения ключа и проверка наличия
    def get_json_value(self, response: Response, name):
        try:
            response_as_dict = response.json()
        except json.decoder.JSONDecodeError:
            assert False, f"Response is not in JSON format. Response text is '{response.text}'"

        assert name in response_as_dict, f"Cannot find {name} in the last response"

        return response_as_dict[name]

    # Получение токена суперюзера
    def get_token_superuser(self):
        payload = {
            "username": "garpix@garpix.com",
            "password": "garpix911_demo"
        }
        response = requests.post("https://mf-prod-copy.infra.garpix.com/api/auth/login/", json=payload)
        token = self.get_json_value(response, "access_token")
        return token

    # Получение токена активного пользователя
    def get_token_activity(self):
        payload = {
            "username": "79999997755",
            "password": "263898"
        }
        response = requests.post("https://mf-prod-copy.infra.garpix.com/api/auth/login/", json=payload)
        token = self.get_json_value(response, "access_token")
        return token

    # Получение токена персонала
    def get_token_staff(self):
        payload = {
            "username": "79999996655",
            "password": "123456йЙ"
        }
        response = requests.post("https://mf-prod-copy.infra.garpix.com/api/auth/login/", json=payload)
        token = self.get_json_value(response, "access_token")
        return token

    # Получение токена просмоторрщика
    def get_token_viewer(self):
        payload = {
            "username": "79999995555",
            "password": "123456йЙ"
        }
        response = requests.post("https://mf-prod-copy.infra.garpix.com/api/auth/login/", json=payload)
        token = self.get_json_value(response, "access_token")
        return token