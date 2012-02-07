import web
render=web.template.render("templates", base='head')
db = web.database(dbn='mysql', user='root', pw='123456', db='MyStakes')
