
# 企业微信使用说明
##  一、企业微信，后台管理
### 1. 注册企业微信
   * 登录[企业微信官网](https://work.weixin.qq.com/) ，可以使用个人身份进行注册企业微信。
   * 点击“我的企业”， 底部可以拿到企业的 <font color=red size=5>corp_id</font>

### 2. 管理通讯录：
   * 点击"通讯录"，可以创建部门，管理成员等。成员需要自行登录企业微信app, 绑定微信。
   * 点击“管理工具”-> "通讯录同步"， 设置允许通过api来管理通讯录
   * 此时可以拿到通讯录的秘钥 <font color=red size=5>contact_sync_secret</font>

### 3. 创建应用：
   * 登录管理后台，点击“应用和小程序”，创建应用。
   * 创建好应用后，需要设置可见范围，否则成员无法接收到消息。
   * 此时可以拿到该应用的 <font color=red size=5>agent_id， app_secret</font>

### 4.关注企业微信公众号
   * 点击“连接微信”-> “微工作台”，扫描底部的企业微信二维码，关注该企业微信。
   * 若是新加入的成员，则申请加入后，需要管理员在"管理工具"->"成员加入"中进行审核。

### 5. 测试应用发送消息
   * 点击“应用于小程序，选择要使用的应用;
   * 确保待接收消息的人或者部门，在应用的可见范围内;
   * 然后点击“发送消息”，选择联系人和编辑内容

### 6. 接收消息
   *  在应用的可见范围内，则会在企业微信app中接收到消息
   *  待接收人已关注了该企业微信，则微信上也会接收到消息

## 二、调用API
### 1. 开启微信的api管理
* 点击“管理工具”-> “通讯录同步”，开启API接口同步；
* 若不开启，则调用和通讯录相关的api会报无权限的错误

### 2. 参照企业微信的api文档，调用接口
   API详情见: [官网](https://work.weixin.qq.com/api/doc#90000/90135/90664)
* 部门的增删改查
* 成员的增删改查
* 选择接收告警的成员或者分组
* 等等.....

### 3.token说明
 
  * 获取token接口: https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=ID&corpsecret=SECRECT
  * token类型：
      - 发送消息 token： corpid + app_secret , 用于访问应用api,  对通讯录的api管理只能读，无法进行写操作;
      - 通讯录管理 token： corpid + contact_sync_secret，用于管理通讯录api，但无法用于发送消息；
  * 其中app_secret  和 contact_sync_secret 的获取，见前面微信管理后台部分介绍
### 4. 消息发送，简单源码

```
# -*-encoding:utf-8-*-
import requests
import json
CORP_ID = 'wwb4ea78b05f6b0df7'
CORP_SECRET = 'gEu_0u5fsPMrC6z7Jm6dkM_Yfeliay0anogXgMRGE68'

AGENT_ID = 1000002
CORP_WECHAT_URL = "https://qyapi.weixin.qq.com/cgi-bin"
GET_TOKEN_URL = CORP_WECHAT_URL + "/gettoken"
SEND_MSG_URL = CORP_WECHAT_URL + "/message/send"

class Wechat(object):

    def __init__(self):
        self.token = self.get_token(CORP_ID, CORP_SECRET)

    def get_token(self, corpid, corpsecret):
        params = {"corpid": corpid, "corpsecret": corpsecret}
        request = requests.get(GET_TOKEN_URL, params=params)
        try:
            ret_info = json.loads(request.content)
            if isinstance(ret_info, dict):
                if ret_info['errcode'] != 0:
                    print("errmsg:%s" % ret_info['errmsg'])
                else:
                    return ret_info.get("access_token")
        except Exception as error:
            print "get_token met error:%s" % error
        return None

    def send_message(self):
        if not self.token:
            print("access_token is none, send message failed")
        URL = SEND_MSG_URL + "?access_token=%s" % self.token
        header = {"Content-Type": "application/json"}
        data = {
                # "toparty" : "1",
                # "touser": "@all",
                "touser": "ChenXi",
                "msgtype" : "text",
                "agentid" : AGENT_ID,
                "text" : {"content" : "hello 杉岩数据，来自远方的微信告警测试"},
                "safe":0
                }
        request = requests.post(URL, data=json.dumps(data), headers=header)
        print request.content
        
if __name__ == '__main__':
    wechat = Wechat()
    print "token:", wechat.token
    wechat.send_message()

```














