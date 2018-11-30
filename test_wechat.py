#!/usr/bin/env python
# -*- coding:utf-8-*-
# @Author Wakesy

from api.department import DepartmentApi
from api.user import UserApi
from api.message import MessageApi
from api.chatgroup import ChatGroupApi
from api.base_api import CORP_API_TYPE
from conf import CORP_ID, CONTACT_SYNC_SECRET, APP_SECRET, TOKEN_TYPES

def department_test():
    contact_sync_token = TOKEN_TYPES['contact_sync_token']
    department_api = DepartmentApi(CORP_ID, CONTACT_SYNC_SECRET, contact_sync_token)
    # department_api.create()
    # department_api.get()
    # department_api.update()
    # department_api.delete()
    department_api.get()


def user_test():
    contact_sync_token = TOKEN_TYPES['contact_sync_token']
    user_api = UserApi(CORP_ID, CONTACT_SYNC_SECRET, contact_sync_token)
    # user_api.detail_list()
    # user_api.create()
    # user_api.update()
    # user_api.get()
    # user_api.delete()
    # user_api.batch_delete()
    user_api.simple_list()

def message_test():
    app_token = TOKEN_TYPES['app_token']
    message_api = MessageApi(CORP_ID, APP_SECRET, app_token)
    print message_api.get_access_token()
    # message_api.send_message('ChenXi')
    # message_api.corp_wechat_invite()

def chatgroup_test():
    chatgroup_api = ChatGroupApi(CORP_ID, APP_SECRET)
    chatgroup_api.create(u'老猫的猫窝')
    chatgroup_api.get()
    chatgroup_api.update()
    content = u'童鞋你好，恭喜你收到了来自杉岩微信告警!'
    chatgroup_api.send_text_msg(content)


if __name__ == '__main__':
    # department_test()
    # user_test()
    message_test()
