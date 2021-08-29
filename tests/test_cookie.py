import requests

class TestCookie:
    def test_check_cookie(self):
        url = "https://playground.learnqa.ru/api/homework_cookie"
        response = requests.get("https://playground.learnqa.ru/api/homework_cookie")
        print(response.cookies)
        assert response.status_code == 200, "Wrong response status"
        assert "HomeWork" in response.cookies, "There is now homework cookie in the response"
        assert response.cookies.get("HomeWork") == "hw_value", "The homework has wrong value"

