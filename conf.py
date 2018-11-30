#-*-coding:utf-8-*-

# 企业的id，在管理端->"我的企业" 可以看到
CORP_ID = "wwb4ea78b05f6b0df7"
# 某个自建应用的id及secret, 在管理端 -> 企业应用 -> 自建应用, 点进相应应用可以看到
APP_ID = 1000002
# 应用密钥，只能进行读操作，无写操作权限。对用户，部门等进行写操作报异常：no privilege to access/modify contact/party/agent
APP_SECRET = "gEu_0u5fsPMrC6z7Jm6dkEgYSW3b3SdX59TK5fqpa7Q"
# 通讯录同步密钥，可以对部门，用户进行读写操作， 管理端 -> 管理工具 -> 通讯录同步
CONTACT_SYNC_SECRET = "HNtp7SKdvpmqqJQahl2vJn1HRGZEy09Ddacf5XrBLX8"
DEBUG = False

# 访问通讯录的token, 如部门、用户等的读写操作
# 访问app的token, 如发送消息,不可操作通讯录
# 临时token ，测试用
TOKEN_TYPES = {'contact_sync_token': 'uptiAKUpBhPhU1laaLYOKyzQBzCnbp0hPEr7qFXqVy8k87wVrgN132myVGjKvYFNtdYOGBxjyigaGfQ4qe3HMZMWzVtpduvLI3PHc-x6ihHdbm-Es3x9So9afX3el3guGB3OQrs40SKTs4HRit1A1TZmghrxHeePD2ReDKX3H-Q4CV9snX3kg3yy87Fx8UJji-A6KbKG2MenYhZuMx2jpg',       
               'app_token': 'wjveUe7cbTPcwwmhe2qUsOlq5t_dve0JqP68wDu8VIUC8pZFd5ArCF_dXx850oMBOYB7QYjzg4xOEMIB2GJ_30dKnr-nYyeMr6rCuNeK9MSwNVV_mNTXC5hjA-xX1mSo6DDVmtHVkTsdgAGmflBYf5V3HMJwda-8DtgYdP7xLV3aKqAhPhuHS3tbieBiyfkI2dgrXFP5tXVLanRiAB5NeA'}                

wechat_configure = {"corp_id": "wwb4ea78b05f6b0df7",
                    "app_id": 1000002,
                    "app_secret": "gEu_0u5fsPMrC6z7Jm6dkEgYSW3b3SdX59TK5fqpa7Q",
                    "contact_sync_secret": "HNtp7SKdvpmqqJQahl2vJn1HRGZEy09Ddacf5XrBLX8",
                    "alarm_group_id": 2,
                    "alarm_switch": "on",
                    }