#coding=utf-8
import sys
from config import settings
from model import sign
from web import form

reload(sys)
sys.setdefaultencoding('utf-8')

login = form.Form(
        form.Textbox('username',
            form.notnull,
            description="帐号:",
            ),
        form.Password('password',
            form.notnull,
            description="密码:",
            ),
        form.Button('Login'),
        )


class signin:

    def GET(self):
        my_form = login()
        return settings.render.signin("MyStakes", my_form)

    def POST(self):
        my_form = login()
        if not my_form.validates():
            return settings.render.signin("MyStakes", my_form)
        else:
            username = my_form['username'].value
            password = my_form['password'].value
            signin = sign.sign()
            if (signin.login(username, password)):
                return "登陆成功"
            else:
                return "登陆失败"
