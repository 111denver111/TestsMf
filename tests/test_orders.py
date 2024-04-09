from lib.base_case import BaseCase
from lib.assertions import Assertions
from lib.my_requests import MyRequests
import datetime


class TestOrders(BaseCase):
    def test_logout_without_token(self):
        # Берем текущую дату и время, и приравниваем к большему
        now = datetime.datetime.now()
        if now.minute != 0 or now.second != 0:
            now += datetime.timedelta(hours=1)
            now = now.replace(minute=0, second=0)
        formatted_time = now.strftime("%Y-%m-%dT%H:%M:%S.000Z")
        data = {
            "orders": [
                {
                    "customer": {
                        "id": 88196
                    },
                    "tariff": {
                        "id": 12,
                        "title": "Первый полёт",
                        "is_child": "false"
                    },
                    "participants": [
                        {
                            "id": 68281
                        }
                    ],
                    "price": "2001.00",
                    "count_party": 1,
                    "comment": "",
                    "is_pay_here": "true",
                    "is_automatic_stock": "true",
                    "is_arrived": "false",
                    "is_children": "false",
                    "promo_code": "null",
                    "tariff_rate": 68,
                    "start_at": formatted_time
                }
            ]
        }
        response = MyRequests.post("/order/orders/",
                                   headers={"X-Authorization": f"Bearer {BaseCase.get_token_staff(self)}"},
                                   data=data)
        Assertions.assert_code_status(response, 201)



