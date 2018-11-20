#!/usr/bin/env python
#-*-coding:utf-8-*-

import sys
import os
import traceback
from base_api import ApiException, BaseApi, CORP_API_TYPE
sys.path.append(os.path.abspath('../'))
from conf import CORP_ID, CONTACT_SYNC_SECRET

class DepartmentApi(BaseApi):

    def simple_list(self):
        '''部门列表'''
        '''返回格式：
            {u'department': [
            {u'order': 100000000, 
            u'parentid': 0, 
            u'id': 1, 
            u'name': u'SandStone'}],
            u'errcode': 0, 
            u'errmsg': u'ok'}
        '''
        try:
            response = self.http_request(CORP_API_TYPE['DEPARTMENT_LIST'])
            print response
        except ApiException as error:
            print repr(error)

    def create(self, department_name):
        '''创建部门'''
        '''返回格式： 
            {u'id': 2,
            u'errcode': 0, 
            u'errmsg': u'created'}
        '''
        args = {'name': department_name,
                'parentid': 1,  # 父部门id
                # 'order': 2,     # order越大越靠前
                # 'id': 4         # 部门id，不填自动生成
                }        
        try:
            response = self.http_request(CORP_API_TYPE['DEPARTMENT_CREATE'], args=args)
            print response
        except ApiException as error:
            print repr(error)

    def update(self):
        '''修改部门'''
        '''返回格式： 
            {u'id': 2,
            u'errcode': 0, 
            u'errmsg': u'updated'}
        '''
        args = {'id': 2,
                'name': 'mos_test',
                'parentid': 1,  # 父部门id
                'order': 3,     # order越大越靠前
                }               # 部门id
        try:
            response = self.http_request(CORP_API_TYPE['DEPARTMENT_UPDATE'], args=args)
            print response
        except ApiException as error:
            print repr(error)

    def delete(self):
        '''修改部门'''
        '''返回格式： 
            {u'id': 2,
            u'errcode': 0, 
            u'errmsg': u'deleted'}
        '''
        args = {'id': 4}          # 部门id, 不能删除根部门；不能删除含有子部门、成员的部门
        try:
            response = self.http_request(CORP_API_TYPE['DEPARTMENT_DELETE'], args=args)
            print response
        except ApiException as error:
            print repr(error)


if __name__ == '__main__':
    department_api = DepartmentApi(CORP_ID, CONTACT_SYNC_SECRET)
    # department_api.create('test')
    # department_api.simple_list()
    # department_api.update()
    # department_api.delete()
    
    department_api.simple_list()

