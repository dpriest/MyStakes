#! usr/bin/env python
# coding: utf-8

import web

urls=(
	"/","index",
)

render=web.template.render("templates")

app=web.application(urls,globals())

class index:
	def GET(self):
		return render.index()

if __name__=="__main__":
	app.run()