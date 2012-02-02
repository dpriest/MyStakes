#! usr/bin/env python
# coding: utf-8
import web
from config.url import urls

app=web.application(urls,globals(), True)

if __name__=="__main__":
	app.run()
