from lib.base_case import BaseCase
from lib.assertions import Assertions
from lib.my_requests import MyRequests


class TestLogoutNegative(BaseCase):
    def test_logout_without_token(self):
        response = MyRequests.post("/auth/logout/")
        Assertions.assert_code_status(response, 401)
        expected_value = {
            'detail': 'Учетные данные не были предоставлены.'
        }
        Assertions.assert_json_has_keys_with_partial_values(response, expected_value)

