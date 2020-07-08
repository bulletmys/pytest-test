import random

import pytest


@pytest.fixture(params=["strong", "medium"])
def pwd_gen_complexity(request):
    return request.param


@pytest.fixture(params=["ru_RU", ""])
def pwd_gen(client, pwd_gen_complexity, request):
    def _method(count):
        args = {"locale": request.param, "count": count, "complexity": pwd_gen_complexity}

        return client.get("utils/password/generate", params=args)

    return _method


class TestUser:
    pwd_count = 10

    def test_get_user_forbidden(self, client):
        response = client.get("user")
        data = response.json()
        assert data.get("status") == 403, "Wrong Status"

    @pytest.mark.parametrize("expected_status", [200, 403])
    def test_get_user_with_pwd(self, client, pwd_gen, expected_status):
        passwords = pwd_gen(self.pwd_count).json().get("body")
        pwd_num = random.randrange(1, self.pwd_count, 1)
        response = client.get("user", params={"test": passwords[pwd_num].get("password")})
        data = response.json()
        assert data.get("status") == expected_status, "Wrong Status"
