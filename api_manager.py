#!/usr/bin/env python
#-*-coding:utf-8-*-

import json
from api.application import ApplicationApi
from api.department import DepartmentApi
from api.user import UserApi

class WechatApiManager(object):
    '''根据传入的微信配置，统一管理各类型api，可自定义加入方法'''
    def __init__(self, wechat_configure):
        self.config = wechat_configure
        self.app_api = ApplicationApi(self.config['corp_id'], self.config['app_secret'])
        self.user_api = UserApi(self.config['corp_id'], self.config['contact_sync_secret'])
        self.department_api = DepartmentApi(self.config['corp_id'], self.config['contact_sync_secret'])


    def get_wechat_display_info(self):
        '''综合查询结果参数，返回给前端展示'''
        app_info = self.app_api.get_detail(appid=self.config['app_id'])
        user_info = self.user_api.detail_list(department_id=self.config['department_id'])
        department_list = self.department_api.get(id=self.config['department_id'])
        # application
        ret_info = {}
        ret_info['application'] = {}
        ret_info['application']['name'] = app_info['name']
        ret_info['application']['agentid'] = app_info['agentid']
        ret_info['application']['description'] = app_info['description']
        ret_info['application']['square_logo_url'] = app_info['square_logo_url']
        # department
        ret_info['department'] = {}
        for department in department_list['department']:
            if department['id'] == self.config['department_id']:
                ret_info['department']['id'] = department['id']
                ret_info['department']['name'] = department['name']
                ret_info['department']['app_visible'] = False
                if department['id'] in app_info['allow_partys']['partyid']:
                    ret_info['department']['app_visible'] = True
                break
        # users
        ret_info['users'] = []
        for user in user_info['userlist']:
            user_info = {}
            user_info['name'] = user['name']
            user_info['email'] = user['email']
            user_info['userid'] = user['userid']
            user_info['mobile'] = user['mobile']
            user_info['gender'] = user['gender']
            user_info['position'] = user['position']
            user_info['department'] = user['department']
            user_info['app_visible'] = False
            # 用户本人，或者其所在部门是否可见应用
            same_partys = [party for party in user['department'] if party in app_info['allow_partys']['partyid']]
            if {'userid': user['userid']} in app_info['allow_userinfos']['user']:
                user_info['app_visible'] = True
            elif len(same_partys) > 0:
                user_info['app_visible'] = True
            ret_info['users'].append(user_info)
        return json.dumps(ret_info)


if __name__ == '__main__':
    ret_info = {'application': {'agentid': '',
                                'name': '',
                                'square_logo_url': '',
                                'description': ''},
                'department':{'id': 2, 
                            'name': 'test',
                            'app_visible': False # 是否可见应用
                            },
                'users': [{'name': u"陈希",
                          'email': '',
                          'userid': 'ChenXi',
                          'mobile': '',
                          'gender': '0',
                          'department': [1, 2],
                          'position': u'后台工程师',
                          'app_visible': True # 是否可见应用
                         },]
                }
