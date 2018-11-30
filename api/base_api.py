#!/usr/bin/env python
#-*-coding:utf-8-*-
# @Author wakesy

import requests
import json
BASE_URL = "https://qyapi.weixin.qq.com"
RETRY_TIMES = 3

CORP_API_TYPE = {
        # 获取token
        'GET_ACCESS_TOKEN'  : ['/cgi-bin/gettoken', 'GET'],
        # 用户管理，需要corpid + contact_secret生成的token才有读写权限
        'USER_CREATE' 	    : ['/cgi-bin/user/create?access_token=ACCESS_TOKEN', 'POST'],
        'USER_GET' 	        : ['/cgi-bin/user/get?access_token=ACCESS_TOKEN', 'GET'],
        'USER_UPDATE'       : ['/cgi-bin/user/update?access_token=ACCESS_TOKEN', 'POST'],
        'USER_DELETE' 	    : ['/cgi-bin/user/delete?access_token=ACCESS_TOKEN', 'GET'],
        'USER_BATCH_DELETE' : ['/cgi-bin/user/batchdelete?access_token=ACCESS_TOKEN', 'POST'],
        'USER_SIMPLE_LIST'  : ['/cgi-bin/user/simplelist?access_token=ACCESS_TOKEN', 'GET'],
        'USER_LIST' 	    : ['/cgi-bin/user/list?access_token=ACCESS_TOKEN', 'GET'],
        'USERID_TO_OPENID'  : ['/cgi-bin/user/convert_to_openid?access_token=ACCESS_TOKEN', 'POST'],
        'OPENID_TO_USERID'  : ['/cgi-bin/user/convert_to_userid?access_token=ACCESS_TOKEN', 'POST'],
        'USER_AUTH_SUCCESS' : ['/cgi-bin/user/authsucc?access_token=ACCESS_TOKEN', 'GET'],
        # 部门管理，需要corpid + contact_secret生成的token才有读写权限
        'DEPARTMENT_CREATE' : ['/cgi-bin/department/create?access_token=ACCESS_TOKEN', 'POST'],
        'DEPARTMENT_UPDATE' : ['/cgi-bin/department/update?access_token=ACCESS_TOKEN', 'POST'],
        'DEPARTMENT_DELETE' : ['/cgi-bin/department/delete?access_token=ACCESS_TOKEN', 'GET'],
        'DEPARTMENT_LIST'   : ['/cgi-bin/department/list?access_token=ACCESS_TOKEN', 'GET'],
        # 消息发送，需要corpid + app_secret生成的token
        'MESSAGE_SEND' 	    : ['/cgi-bin/message/send?access_token=ACCESS_TOKEN', 'POST'],
        'CORP_WECHAT_INVITE': ['/cgi-bin/batch/invite?access_token=ACCESS_TOKEN', 'POST'],
        # 企业微信app内群聊
        'CHATGROUP_CREATE'  : ['/cgi-bin/appchat/create?access_token=ACCESS_TOKEN', 'POST'],
        'CHATGROUP_UPDATE'  : ['/cgi-bin/appchat/update?access_token=ACCESS_TOKEN', 'POST'],
        'CHATGROUP_GET'     : ['/cgi-bin/appchat/get?access_token=ACCESS_TOKEN', 'GET'],
        'CHATGROUP_SEND'    : ['/cgi-bin/appchat/send?access_token=ACCESS_TOKEN', 'POST'],
        # 应用
        'APPLICATION_GET'   : ['/cgi-bin/agent/get?access_token=ACCESS_TOKEN', 'GET'],
        'APPLICATION_UPDATE': ['/cgi-bin/agent/set?access_token=ACCESS_TOKEN', 'POST']
}


class BaseApi(object):

    def __init__(self, corpid='', secret='', token_type='app_token'):
        self.corpid = corpid
        self.secret = secret
        self.token_type = token_type
        self.access_token = None

    def get_access_token(self):
        # todo: get token in db by token_type
        if not self.access_token:
            self.refresh_access_token()
        
        return self.access_token
  
    def refresh_access_token(self):
        args = {'corpid': self.corpid, 'corpsecret': self.secret}
        response = self.http_request(CORP_API_TYPE['GET_ACCESS_TOKEN'], args)
        self.access_token = response.get('access_token')
        # todo: update token in db by token_type

    def http_request(self, url_type, args=None):
        short_url = url_type[0]
        request_type = url_type[1]
        response = {}
        for count in range(RETRY_TIMES): # 重试3次
            if request_type == 'GET':
                url = self.__make_url(short_url)
                url = self.__append_args(url, args)
                response = self.__http_get(url)
            elif request_type == 'POST':
                url = self.__make_url(short_url)
                response = self.__http_post(url, args)
            else:
                raise ApiException('-1', 'unknown method type: %s' % request_type)
            if self.__is_token_expired(response.get('errcode')):
                self.refresh_access_token()
                continue
            else:
                break
        return self.__check_response(response)

    def __http_get(self, url):
        return requests.get(url).json()
            
    def __http_post(self, url, args):
        params = json.dumps(args, ensure_ascii=False).encode('utf-8')
        response = requests.post(url, data=params).json()
        return response

    def __check_response(self, response):
        if response.get('errcode') != 0:
            raise ApiException(response.get('errcode'), response.get('errmsg'))
        else:
            return response

    def __append_args(self, url, args):
        if args is None:
            return url
        for key, value in args.items():
            if '?' in url:
                url += '&' + key + '=' + str(value)
            else:
                url += '?' + key + '=' + str(value)
        return url

    def __make_url(self, short_url):
        if short_url.startswith('/'):
            return self.__append_token(BASE_URL + short_url)
        else:
            return self.__append_token(BASE_URL + '/' + short_url)

    def __is_token_expired(self, retcode):
        if retcode in [40014, 42001, 42007, 42009]:
            return True
        else:
            return False

    def __append_token(self, url):
        if 'ACCESS_TOKEN' in url:
            return url.replace('ACCESS_TOKEN', self.get_access_token())
        else: 
            return url


class ApiException(Exception):

    def __init__(self, error_code, error_msg):
        self.error_code = error_code
        self.error_msg = error_msg
    
    def __str__(self):
        return "<ApiException> error_code: {}, error_msg: {}".format(self.error_code, self.error_msg)

    def __repr__(self):
        return "<ApiException> error_code: {}, error_msg: {}".format(self.error_code, self.error_msg)


    