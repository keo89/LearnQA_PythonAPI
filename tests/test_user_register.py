import pytest as pytest
from lib.my_requests import MyRequests
from lib.base_case import BaseCase
from lib.assertions import Assertions
import allure

class TestUserRegister(BaseCase):
    fields = [
        ("password"),
        ("username"),
        ("firstName"),
        ("lastName"),
        ("email")
    ]

    @allure.story('story_1')
    def create_user_successfully(self):
        data = self.prepare_registration_data()
        response = MyRequests.post("/user/", data=data)

        Assertions.assert_code_status(response, 200)
        Assertions.assert_json_has_key(response, "id")

    def test_create_user_with_existing_email(self):
        email = 'vinkotov@example.com'
        data = self.prepare_registration_data(email)
        response = MyRequests.post("/user/", data=data)
        Assertions.assert_code_status(response, 400)
        assert response.content.decode(
            "utf-8") == f"Users with email '{email}' already exists", f"Unexpected content {response.content}"

    def test_create_user_without_symbol(self):
        data = {
            'password': '123',
            'username': 'learnqa',
            'firstName': 'learnqa',
            'lastName': 'learnqa',
            'email': 'vinkotovexample.com'
        }
        response = MyRequests.post("/user/", data=data)
        Assertions.assert_code_status(response, 400)
        assert response.content.decode("utf-8") == f"Invalid email format", f"Unexpected content {response.content}"

    @pytest.mark.parametrize('field', fields)
    def test_user_without_field(self, field):
        data = self.prepare_registration_data()
        del data[field]
        response = MyRequests.post("/user/", data=data)

        Assertions.assert_code_status(response, 400)
        assert response.content.decode(
            "utf-8") == f"The following required params are missed: {field}", f"Unexpected content {response.content}"

    @allure.story('story_1')
    def test_create_user_with_one_symbol_username(self):
        data = {
            'password': '123',
            'username': 'l',
            'firstName': 'learnqa',
            'lastName': 'learnqa',
            'email': 'vinkotov@example.com'
        }

        response = MyRequests.post("/user/", data=data)

        Assertions.assert_code_status(response, 400)
        assert response.content.decode(
            "utf-8") == f"The value of 'username' field is too short", f"Unexpected content {response.content}"

    def test_create_user_with_too_long_username(self):
        data = {
            'password': '123',
            'username': 'fvtghyudcgpztsmcgfnjofkqtzqqmluaadubpzlveabrzmyqwbxjusvxdoigjfectonsqwndugnsylriuhskmkdyubbcbhectjeuajtvtpavvmfoibzmrmhlxgdgpoiuyoqsabltpurvaueayuoroimotbdmuclmjxmdabfcxoetfegbqinncqsfpqyxbzmldoijtlmcywxwgojungkmaccthlsqqnmsbqlmbvavvzobarjfhjzblxwekoqpqbeirenn',
            'firstName': 'learnqa',
            'lastName': 'learnqa',
            'email': 'vinkotov@example.com'
        }

        response = MyRequests.post("/user/", data=data)
        Assertions.assert_code_status(response, 400)
        assert response.content.decode(
            "utf-8") == f"The value of 'username' field is too long", f"Unexpected content {response.content}"
