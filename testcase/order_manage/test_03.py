import pytest
import requests

from common.common_util import CommonUtil
from common.request_util import RequestUtil
from common.yaml_util import read_yaml


class TestThreeDay(CommonUtil):

    access_token=""

    @pytest.mark.parametrize('canshu',read_yaml('D:\\test\\testcase\order_manage\get_token.yaml'))
    def test_token(self,canshu):
        print("03获取统一的token")
        url=canshu['request']['url']
        data=canshu['request']['data']
        validate=canshu['validate']
        name=canshu['name']
        method=canshu['request']['method']

        res=RequestUtil.send_request(self,method,url,data)
        result=res.json()
        print(result)
        TestThreeDay.access_token=result['errcode']
        print(TestThreeDay.access_token)

    @pytest.mark.parametrize('canshu', read_yaml('D:\\test\\testcase\order_manage\edit_flag.yaml'))
    def test_edit_flag(self,canshu):
        print("03编辑标签接口")
        url = canshu['request']['url']+str(TestThreeDay.access_token)
        print(url)
        data = canshu['request']['data']
        print(data)
        validate = canshu['validate']
        name = canshu['name']
        method = canshu['request']['method']
        res=RequestUtil.send_request(self,method,url,data)
        result=res.json()
        print(result)