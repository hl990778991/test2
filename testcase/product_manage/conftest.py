import pytest


def read_yaml():
    return ['aa','bb','cc']

@pytest.fixture(scope="function",autouse=False,params=read_yaml(),ids=['A','B','C'],name="pm")
def  product_manage(request):
    print("商品管理前")
    yield request.param
    print("商品管理后")

