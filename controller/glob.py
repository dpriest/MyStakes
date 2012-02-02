from config import settings
import web


class index:

    def GET(self):
        i = web.input(name = 'web')
        return  settings.render.index()
