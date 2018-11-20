#-*- coding:utf-8 -*-
import sys
import os
import traceback
from base_api import ApiException, BaseApi, CORP_API_TYPE

sys.path.append(os.path.abspath('../'))
from conf import CORP_ID, APP_SECRET, APP_ID

class MessageApi(BaseApi):

    def send_message(self, userid='ChenXi', msgtype='text'):
        '''发送文本消息'''
        '''返回格式:
            {u'invaliduser': u'', 
            u'errcode': 0, 
            u'errmsg': u'ok'}
        '''
        try:
            args = {'touser': userid,
                    # 'toparty': '1|2',   # 部门id
                    'msgtype': msgtype, 
                    'agentid': APP_ID,
                    'text': {'content': u'hello %s童鞋，恭喜你接收到了来自杉岩数据的告警！' % userid},
                    'safe': 0
                    }
            response = self.http_request(CORP_API_TYPE['MESSAGE_SEND'], args=args)
            print response
        except ApiException as error:
            print repr(error)

    def corp_wechat_invite(self):
        '''邀请加入企业微信，邮件或者短信, 试过好像不起作用'''
        '''返回格式
            {
            "errcode" : 0,
            "errmsg" : "ok",
            "invaliduser" : ["UserID1", "UserID2"],
            "invalidparty" : [PartyID1, PartyID2],
            "invalidtag": [TagID1, TagID2]
            }
        '''
        try:
            args = {'user': ['ChenXi'],
                    'party': [],
                    'tag': [],
                    }
            response = self.http_request(CORP_API_TYPE['CORP_WECHAT_INVITE'], args=args)
            print response 
        except Exception as error:
            print repr(error)

if __name__ == '__main__':
    message_api = MessageApi(CORP_ID, APP_SECRET)
    # message_api.send_message()
    message_api.corp_wechat_invite()