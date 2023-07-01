import pytest


def read_yaml():
    return ['aa','bb','cc']


@pytest.fixture(scope="function", autouse=False, params=read_yaml(), ids=['A', 'B', 'C'], name="um")
def user_manage(request):
    print("商品管理1前")
    yield request.param
    print("商品管理1后")