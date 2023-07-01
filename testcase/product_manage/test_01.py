import pytest

from common.common_util import CommonUtil



class TestOneDay(CommonUtil):
   # age=9
    def test_001(self):
        print("第1个用例")

    #@pytest.mark.skipif(age<10,reason="小于10跳过")
    def test_002(self,login,pm):
        print("第2个用例")
        print("参数化"+login+pm)

  #  @pytest.mark.skip(reason="无理由跳过")
    def test_003(self):
        print("第3个用例")


