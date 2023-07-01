import pytest

from common.common_util import CommonUtil
from common.request_util import RequestUtil
from common.yaml_util import read_yaml
from testcase.order_manage.test_03 import TestThreeDay


class TestFourDay(CommonUtil):

    @pytest.mark.parametrize('canshu', read_yaml('D:\\test\\testcase\order_manage\get_token.yaml'))
    def test_token(self, canshu):
        print("04获取统一的token")
        url = canshu['request']['url']
        data = canshu['request']['data']
        validate = canshu['validate']
        name = canshu['name']
        method = canshu['request']['method']
        print(method)
        print(url)

        res = RequestUtil.send_request(self,method, url,data)
        result = res.json()
        print(result)
