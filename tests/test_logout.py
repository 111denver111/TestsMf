from lib.base_case import BaseCase
from lib.assertions import Assertions
from lib.my_requests import MyRequests


class TestLogout(BaseCase):
    def test_logout(self):
        response = MyRequests.post("/auth/logout/", headers={"X-Authorization": f"Bearer {BaseCase.get_token_activity(self)}"})
        Assertions.assert_code_status(response, 200)
        expected_value = {
            'result': True
        }
        Assertions.assert_json_has_keys_with_partial_values(response, expected_value)
