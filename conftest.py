import pytest


@pytest.fixture(scope="function",autouse=False,ids=['A','B','C'],name="login")
def  login_ecshop(request):
    print("登录前")
    yield "登录成功"
    print("登录后")
