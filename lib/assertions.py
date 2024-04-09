from requests import Response
import json


class Assertions:
    # Проверка наличия ключа и реального и ожидаемого значения
    @staticmethod
    def assert_json_value_by_name(response: Response, name, expected_value, error_message):
        try:
            response_as_dict = response.json()
        except json.JSONDecodeError:
            assert False, f"Response is not in JSON format. Response text is '{response.text}'"

        assert name in response_as_dict, f"Cannot find {name} in the last response"
        assert response_as_dict[name] == expected_value, error_message

    # Проверка наличия ключа
    @staticmethod
    def assert_json_has_key(response: Response, name):
        try:
            response_as_dict = response.json()
        except json.JSONDecodeError:
            assert False, f"Response is not in JSON format. Response text is '{response.text}'"

        assert name in response_as_dict, f"Cannot find {name} in the last response"

    # Проверка наличия ключей
    @staticmethod
    def assert_json_has_keys(response: Response, names: list):
        try:
            response_as_dict = response.json()
        except json.JSONDecodeError:
            assert False, f"Response is not in JSON format. Response text is '{response.text}'"
        for name in names:
            assert name in response_as_dict, f"Cannot find {name} in the last response"

    # Проверка отсутствия ключа
    @staticmethod
    def assert_json_has_not_key(response: Response, name):
        try:
            response_as_dict = response.json()
        except json.JSONDecodeError:
            assert False, f"Response is not in JSON format. Response text is '{response.text}'"

        assert name not in response_as_dict, f"Should not find {name} in the last response"

    # Проверка кода
    @staticmethod
    def assert_code_status(response: Response, expected_status_code):
        assert response.status_code == expected_status_code, \
            f"Unexpected status code! Expected: {expected_status_code}. Actual: {response.status_code}"


    # Проверка наличия ключей и значений(гибкий) + принимает список
    @staticmethod
    def assert_json_has_keys_with_partial_values(response: Response, key_value_pairs: dict):
        try:
            response_as_dict = response.json()
        except json.JSONDecodeError:
            assert False, f"Response is not in JSON format. Response text is '{response.text}'"

        def recursive_check(dictionary, key_value_pairs):
            for key, value in key_value_pairs.items():
                if key not in dictionary:
                    assert False, f"Cannot find key '{key}' in the last response"
                if isinstance(value, dict):
                    recursive_check(dictionary[key], value)
                elif isinstance(value, list):
                    if not all(item in dictionary[key] for item in value):
                        assert False, f"Values for key '{key}' do not match. Expected: {value}. Actual: {dictionary[key]}"
                else:
                    assert dictionary[key] == value, f"Unexpected value for key '{key}'. Expected: {value}. Actual: {dictionary[key]}"

        recursive_check(response_as_dict, key_value_pairs)

