from lib.base_case import BaseCase
from lib.assertions import Assertions
from lib.my_requests import MyRequests


class TestOrders(BaseCase):
    def test_logout_without_token(self):
        response = MyRequests.get("/user/88196", headers={"X-Authorization": f"Bearer {BaseCase.get_token_staff(self)}"})
        Assertions.assert_code_status(response, 200)
        expected_value = {
            'id': 88196,
            'username': '79999997755',
            'first_name': 'Активный',
            'last_name': 'Автотесты',
            'email': '',
            'phone': '79999997755',
            'type_user': 0
        }
        Assertions.assert_json_has_keys_with_partial_values(response, expected_value)
        Assertions.assert_code_status(response, 200)
