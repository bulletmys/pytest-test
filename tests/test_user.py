import random


class TestUser:
    locale = "ru_RU"
    complexity = "strong"
    pwd_count = 10

    def test_get_user_forbidden(self, client):
        response = client.get("user")
        data = response.json()
        assert data.get("status") == 403, "Wrong Status"

    def test_get_user_with_pwd(self, client, pwd_gen):
        passwords = pwd_gen(self.locale, self.pwd_count, self.complexity).json().get("body")
        pwd_num = random.randrange(1, self.pwd_count, 1)
        response = client.get("user", {"test": passwords[pwd_num].get("password")})
        data = response.json()
        assert data.get("status") == 403, "Wrong Status"
