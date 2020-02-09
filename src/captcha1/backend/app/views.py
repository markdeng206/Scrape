from django.http import HttpResponse
import os
from core.settings import SAMPLE_USERNAME, SAMPLE_PASSWORD, URL_MAP
import json
import requests

# 从服务器获取 response_str
# from geetest import GeetestLib
# from core.settings import GEETEST_ID, GEETEST_KEY
# gt = GeetestLib(GEETEST_ID, GEETEST_KEY)

CAPTCHA_TYPE = os.getenv('CAPTCHA_TYPE', 'SLIDE')

assert CAPTCHA_TYPE in URL_MAP.keys()


def init(request):
    response = requests.get(URL_MAP[CAPTCHA_TYPE])
    data = json.dumps(response.json()['data'])
    return HttpResponse(data)


def login(request):
    if request.method != 'POST':
        return HttpResponse(status=405)
    data = json.loads(request.body)
    username = data.get('username')
    password = data.get('password')
    if username != SAMPLE_USERNAME or password != SAMPLE_PASSWORD:
        return HttpResponse(status=401, content='用户名或密码不正确')
    # 取消服务端验证
    # captcha = data.get('captcha', {})
    # geetest_challenge = captcha.get('geetest_challenge')
    # geetest_validate = captcha.get('geetest_validate')
    # geetest_seccode = captcha.get('geetest_seccode')
    # result = gt.success_validate(geetest_challenge, geetest_validate, geetest_seccode)
    # if not result:
    #     return HttpResponse(status=401, content='验证码验证失败')
    return HttpResponse(status=200, content='登录成功')
