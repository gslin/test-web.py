import web

render = web.template.render('views/')

class index(object):
    def GET(self):
        return render.index()
