from config import settings

class index:
	def GET(self):
		return settings.render.index()