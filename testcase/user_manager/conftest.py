import pytest


def read_yaml():
    return ['aa','bb','cc']


@pytest.fixture(scope="function", autouse=False, params=read_yaml(), ids=['A', 'B', 'C'], name="um")
def user_manage(request):
    print("用户管理前")
    yield request.param
    print("用户管理后")