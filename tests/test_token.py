import requests


class TestCookie:
    def test_check_token(self):
        url = "https://playground.learnqa.ru/api/homework_cookie"
        response = requests.get("https://playground.learnqa.ru/api/homework_cookie")
        print(response.headers)
        assert response.status_code == 200, "Wrong response status"
        assert "Set-Cookie" in response.headers, "There is set cookie header in the response"
