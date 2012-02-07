#coding=utf-8
import sys
from config import settings
from model import sign
from web import form
import time
import MySQLdb
import web

reload(sys)
sys.setdefaultencoding('utf-8')

vpass = form.regexp(r".{4,20}$", '密码长度必须在4-20个之间')
vemail = form.regexp(r".*@.*", "邮箱地址必须有效")
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
regiForm = form.Form(
        form.Textbox("username", description="帐号:"),
        form.Textbox("email", vemail, description="E-mail:"),
        form.Password("passw",  description="密码:"),
        form.Password("passw2", description="重复密码:"),
        form.Button("submit", type="submit", description="注册"),
        validates = [
            form.Validator("密码不一致", lambda i: i.passw == i.passw2)]
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

class register:

    def GET(self):
        f = regiForm()
        return settings.render.register("注册", f)

    def POST(self):
        f = regiForm()
        if not f.validates():
            return settings.render.register("注册", f)
        else:
            dict = {'username': f['username'].value, 'passw': f['passw'].value, 'email': f['email'].value, 'created_at': MySQLdb.DateFromTicks(time.time( )), 'reg_ip': web.ctx['ip']}
            register = sign.sign()
            register.register(dict)
            return "注册成功"
