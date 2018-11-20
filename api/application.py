#-*- coding:utf-8 -*-
import os
import traceback
from base_api import CORP_API_TYPE, BaseApi
import sys
sys.path.append(os.path.abspath('../'))
from conf import CORP_ID, APP_SECRET, APP_ID

class ApplicationApi(BaseApi):

    def get_detail(self, appid):
        '''获取应用详情'''
        '''返回格式：
            {"errcode": 0,
            "errmsg": "ok",
            "agentid": 1000002,
            "name": "SandStone微信告警",
            "square_logo_url":  "http://p.qlogo.cn/bizmail/aqWdTaicxPk61oDwq70zjbiaDDVWsg1QUXZZj9e8bZJSbAKZfyibYtj5w/0",
            "description": "用于接收来自MOS管理系统产生的告警消息",
            "allow_userinfos": {
                "user": [
                        {"userid": "zhangshan"},
                        {"userid": "lisi"}
                ]
                },
            "allow_partys": {
                "partyid": [1]
                },
            "allow_tags": {
                "tagid": []
                },
            "close": 0,
            "redirect_domain": "open.work.weixin.qq.com",
            "report_location_flag": 0,
            "isreportenter": 0,
            "home_url": "https://open.work.weixin.qq.com"
            }
        '''
        try:
            args = {'agentid': appid}
            response = self.http_request(CORP_API_TYPE['APPLICATION_GET'], args=args)
            print response
        except Exception as error:
            print repr(error)

if __name__ == '__main__':
   app_api = ApplicationApi(CORP_ID, APP_SECRET)
   app_api.get_detail(APP_ID)