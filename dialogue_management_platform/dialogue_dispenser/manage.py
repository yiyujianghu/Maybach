# -*-conding:utf-8-*-
# Base Information:
# @author:      yiyujianghu
# @project:     <Maybach>
# @file:        manage.py
# @time:        2020/8/3 8:33 下午

"""
Notes:...
"""

from gevent import monkey
monkey.patch_all()
from gevent import pywsgi
from app import create_app
from flask_cors import CORS


app = create_app()
CORS(app, supports_credentials=True)
# 跨域支持
def after_request(resp):
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp

app.after_request(after_request)


if __name__ == '__main__':
    print("正在启动服务器......")
    server = pywsgi.WSGIServer(("0.0.0.0", 5000), app)
    print("服务器配置成功！")
    server.serve_forever()
