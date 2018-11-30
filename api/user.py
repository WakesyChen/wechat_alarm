#-*- coding:utf-8 -*-
import sys
import os
import traceback
sys.path.append(os.path.abspath('../'))
from conf import CORP_ID, APP_SECRET, CONTACT_SYNC_SECRET
from base_api import CORP_API_TYPE, BaseApi

class UserApi(BaseApi):
    def simple_list(self, department_id=''):
        '''获取部门成员'''
        '''返回格式：
            {u'userlist': [
                {u'department': [1], u'userid': u'ChenXi', u'name': u'\u9648\u5e0c'}, 
                {u'department': [1], u'userid': u'XinXin', u'name': u'\u6b23\u946b'}], 
            u'errcode': 0,
            u'errmsg': u'ok'}
        '''
        try:
            if department_id:
                args = {'department_id': department_id, "fetch_child": 0} # fetch_child：1/0,是否递归查询子部门下的用户
            else:
                args = None
            response = self.http_request(CORP_API_TYPE['USER_SIMPLE_LIST'], args=args)
            print response
            return response
        except Exception as error:
            print traceback.format_exc()
    

    def detail_list(self, department_id=''):
        '''获取部门成员详情'''
        '''返回格式：已省略部分
            {"errcode": 0,
            "errmsg": "ok",
            "userlist": [{
                "userid": "ChenXi",
                "name": "陈希",
                "department": [1],
                "mobile": "17620349405",
                "gender": "1",
                "email": "",
                "status": 1,
                "enable": 1,
                "order": [0]]
            }
        '''
        try:
            args = {'department_id': department_id} if department_id else None
            response = self.http_request(CORP_API_TYPE['USER_LIST'], args=args)
            print response
            return response
        except Exception as error:
            print traceback.format_exc()

    def create(self): 
        '''创建用户'''
        '''返回格式：
        {"errcode": 0,
        "errmsg": "created"}
        '''
        try:
            # args = {'userid': 'DongLei',
            #         'name': u'董雷',
            #         'department': 2,
            #         'mobile': '13171523666'
            #         }
            args = {'userid': 'YangShiJie',
                    'name': u'杨仕杰',
                    'department': 2,
                    'mobile': '13928421103'
                    }
            response = self.http_request(CORP_API_TYPE['USER_CREATE'], args=args)
            print response 
        except Exception as error:
            print repr(error)

    def update(self):
        '''修改用户'''
        '''返回格式：
        {u'errcode': 0,
         u'errmsg': u'updated'}
        '''
        try:
            args = {'userid': 'DongLei',
                    'email': 'DongLei@qq.com',
                    }
            response = self.http_request(CORP_API_TYPE['USER_UPDATE'], args=args)
            print response 
        except Exception as error:
            print repr(error)

    def get(self):
        '''获取用户详情'''
        '''返回格式：已省略部分
        {u'status': 1, 
        u'name': u'\u9648\u5e0c', 
        u'mobile': u'17620349405', 
        u'gender': u'1', 
        u'userid': u'ChenXi', 
        u'order': [0],  
        u'enable': 1, 
        u'department': [1], 
        u'email': u'', 
        u'errcode': 0, 
        u'errmsg': u'ok'}
        '''
        try:
            args = {'userid': 'DongLei'}
            response = self.http_request(CORP_API_TYPE['USER_GET'], args=args)
            print response 
        except Exception as error:
            print repr(error)

    def delete(self):
        '''删除用户'''
        '''返回格式：
        {u'errcode': 0,
         u'errmsg': u'deleted'}
        '''
        try:
            args = {'userid': 'DongLei'}
            response = self.http_request(CORP_API_TYPE['USER_DELETE'], args=args)
            print response 
        except Exception as error:
            print repr(error)

    def batch_delete(self):
        '''批量删除用户'''
        '''返回格式：
        {u'errcode': 0,
         u'errmsg': u'deleted'}
        '''
        try:
            args = {'useridllist': ['DongLei', 'LiuYiYang']}
            response = self.http_request(CORP_API_TYPE['USER_BATCH_DELETE'], args=args)
            print response 
        except Exception as error:
            print repr(error)


if __name__ == '__main__':
    user_api = UserApi(CORP_ID, CONTACT_SYNC_SECRET)
    user_api.detail_list()
    user_api.create()
    user_api.update()
    user_api.get()
    user_api.delete()
    user_api.batch_delete()
    user_api.simple_list()



