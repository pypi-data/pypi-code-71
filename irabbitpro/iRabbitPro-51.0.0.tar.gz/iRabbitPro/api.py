import hashlib

import jsonpath
import time
import re
import json
import httpx


def get_signature(raw_data, session_key):
    signature = hashlib.sha1((json.dumps(raw_data) + session_key).encode('utf-8')).hexdigest()
    return signature


class WxApi(object):
    # 授权类型
    ORDER_TYPE_AUTH_CODE = 1
    ORDER_TYPE_INFO = 2
    ORDER_TYPE_MOBILE = 3

    CREATE_ORDER_API = 'http://vip.miniclub.vip:7771/createTaskApi'
    GET_RESULT_API = 'http://vip.miniclub.vip:7771/public/getresult'
    API_APPID = '60056'

    GET_RESULT_DELAY = 3

    raw_data=''
    auth_code = ''
    nickName = ''
    signature = ''
    encryptedData = ''
    iv = ''
    avatarUrl = ''
    encryptedDataPhone = ''
    ivPhone = ''
    mobile = ''
    gender = 1
    language = ''
    city = ''
    province = ''
    country = ''
    orderid = ''
    

    def __init__(self, token, wx_appid):
        self.wx_appid = wx_appid
        self.token = token
        # 用户信息

    def create_order(self, order_type):
        """
        创建授权订单
        :param order_type: 授权方式
        :param orderid: 订单号,代入即回扫
        :return:返回订单号
        """
        data = {
            'appId': self.API_APPID,
            'qrCode': f'appID={self.wx_appid}@type={order_type}',
            'token': self.token,
            'orderId': self.orderid,
        }
        resp = httpx.post(self.CREATE_ORDER_API, data=data)
        print(resp.text)
        while '回扫过快' in resp.text:
            time.sleep(self.GET_RESULT_DELAY)
            resp = httpx.post(self.CREATE_ORDER_API, data=data)
            print(resp.text)
        authOrderId = resp.json()['data']['authOrderId']
        print(f'创建订单==>TYPE:{order_type}|订单号:{authOrderId}')
        self.orderid = authOrderId
        return self.orderid

    def get_result(self, orderid=None):
        try:
            try_time = 0
            if orderid is not None:
                self.orderid = orderid
            print(f'订单号{self.orderid}==>获取结果中')
            data = {
                'token': self.token,
                'orderId': self.orderid
            }
            resp = httpx.post(self.GET_RESULT_API, data=data)
            print(f'结果{resp.text}')
            while resp.json()['data'] is None or '回扫中' in resp.text and try_time < 5:
                time.sleep(self.GET_RESULT_DELAY)
                resp = httpx.post(self.GET_RESULT_API, data=data)
                try_time += 1
            data_str = str(resp.json()['data']).split(',@')[0]
            data_json = json.loads(data_str)
            return data_json
        except Exception as e:
            print(e)

    def wx_auth_info(self, orderid=None):
        """
        信息授权
        :param orderid: 留空即回扫
        :return:
        """
        print('<==信息授权==>')
        self.create_order(self.ORDER_TYPE_INFO)
        if orderid is not None:
            self.orderid = orderid
        time.sleep(self.GET_RESULT_DELAY)
        resp_user_json = self.get_result(orderid)
        print(resp_user_json)
        wx_user_json = json.loads(resp_user_json['data'])
        self.raw_data = resp_user_json['data']
        self.nickName = str(jsonpath.jsonpath(wx_user_json, '$..nickName')[0]).replace(' ', '')
        self.gender = jsonpath.jsonpath(wx_user_json, '$..gender')[0]
        self.language = jsonpath.jsonpath(wx_user_json, '$..language')[0]
        self.city = jsonpath.jsonpath(wx_user_json, '$..city')[0]
        self.province = jsonpath.jsonpath(wx_user_json, '$..province')[0]
        self.country = jsonpath.jsonpath(wx_user_json, '$..country')[0]
        self.signature = jsonpath.jsonpath(resp_user_json, '$..signature')[0]
        self.encryptedData = jsonpath.jsonpath(resp_user_json, '$..encryptedData')[0]
        self.iv = jsonpath.jsonpath(resp_user_json, '$..iv')[0]
        self.avatarUrl = jsonpath.jsonpath(wx_user_json, '$..avatarUrl')[0]

    def wx_auth_code(self, orderid=None):
        """
        授权auth_code
        :param orderid: 留空即回扫
        """
        print('<==auth_code授权==>')
        self.create_order(self.ORDER_TYPE_AUTH_CODE)
        if orderid is not None:
            self.orderid = orderid
        time.sleep(self.GET_RESULT_DELAY)
        resp_user_json = self.get_result(orderid)
        print(resp_user_json)
        self.auth_code = jsonpath.jsonpath(resp_user_json, '$..auth_code')[0]

    def wx_auth_mobile(self, orderid=None):
        """
        授权手机信息
        :param orderid: 留空即回扫
        """
        print('<==手机授权==>')
        self.create_order(self.ORDER_TYPE_MOBILE)
        if orderid is not None:
            self.orderid = orderid
        time.sleep(self.GET_RESULT_DELAY)
        resp_user_json = self.get_result(orderid)
        print(resp_user_json)
        self.mobile = jsonpath.jsonpath(resp_user_json, '$..mobile')[0]
        self.encryptedDataPhone = jsonpath.jsonpath(resp_user_json, '$..encryptedData')[0]
        self.ivPhone = jsonpath.jsonpath(resp_user_json, '$..iv')[0]


if __name__ == '__main__':
    token = 'Kg4nhPq6q1aDULseSSWng0pv8iRerF'
    appid = 'wx77af438b3505c00e'
    api = WxApi(token, appid)
    api.wx_auth_code()
    # api.wx_auth_info()
    print(api.auth_code, api.nickName, api.avatarUrl, api.mobile, api.encryptedData, api.encryptedDataPhone, api.iv, api.ivPhone, api.signature)
    time.sleep(3)
    api.wx_auth_info()
    print(api.auth_code, api.nickName, api.avatarUrl, api.mobile, api.encryptedData, api.encryptedDataPhone, api.iv, api.ivPhone, api.signature)
    time.sleep(3)
    api.wx_auth_mobile()
    print(api.auth_code, api.nickName, api.avatarUrl, api.mobile, api.encryptedData, api.encryptedDataPhone, api.iv, api.ivPhone, api.signature)
