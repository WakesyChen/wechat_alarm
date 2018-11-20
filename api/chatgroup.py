#-*- coding:utf-8 -*-
import sys
import os
import traceback
from base_api import ApiException, BaseApi, CORP_API_TYPE

sys.path.append(os.path.abspath('../'))
from conf import CORP_ID, APP_SECRET

'''群聊，只对企业微信app内可见，直接用微信查看不到'''

class ChatGroupApi(BaseApi):

    def create(self, name):
        '''创建群组'''
        '''返回格式{u'errcode': 0,
            u'errmsg': u'ok',
            u'chatid': u'CHATID'}'''
        try:
            args = {'name': name,
                    'owner': 'Chenxi',
                    'userlist': ['Chenxi', 'YangShiJie'],
                    'chatid': 'CHATID'
                    }
            response = self.http_request(CORP_API_TYPE['CHATGROUP_CREATE'], args=args)
            print response 
        except Exception as error:
            print repr(error)


    def update(self):
        '''更新群组信息'''
        '''返回格式：{u'errcode': 0, u'errmsg': u'ok'}'''
        try:
            args = {'chatid': 'CHATID',
                    'name': u'老猫的大猫窝',
                    'owner': 'Chenxi',
                    'add_user_list': [],
                    'del_user_list': []
                    }
            response = self.http_request(CORP_API_TYPE['CHATGROUP_UPDATE'], args=args)
            print response 
        except Exception as error:
            print repr(error) 

    def get(self):
        '''获取群组信息'''
        '''返回格式：{u'chat_info': {u'owner': u'ChenXi', 
                           u'userlist': [u'ChenXi', u'YangShiJie'],
                           u'name': u'\u8001\u732b\u7684\u732b\u7a9d', 
                           u'chatid': u'CHATID'}, 
            u'errcode': 0,
            u'errmsg': u'ok'}'''
        try:
            args = {'chatid': 'CHATID'}
            response = self.http_request(CORP_API_TYPE['CHATGROUP_GET'], args=args)
            print response 
        except Exception as error:
            print repr(error) 

    def send_text_msg(self, content):
        '''发送文本消息到群组'''
        '''返回格式：{u'errcode': 0, u'errmsg': u'ok'}'''
        try:
            args = {'chatid': 'CHATID',
                    'msgtype': 'text',
                    'text':{'content': content},
                    'safe': 0
                    }
            response = self.http_request(CORP_API_TYPE['CHATGROUP_SEND'], args=args)
            print response 
        except Exception as error:
            print repr(error)

if __name__ == '__main__':
    chatgroup_api = ChatGroupApi(CORP_ID, APP_SECRET)
    chatgroup_api.create(u'老猫的猫窝')
    chatgroup_api.get()
    chatgroup_api.update()
    content = u'童鞋你好，恭喜你收到了来自杉岩微信告警!'
    # chatgroup_api.send_text_msg(content)