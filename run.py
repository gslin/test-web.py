#!/usr/bin/env python3

import web

urls = ('/', 'controllers.index')
app = web.application(urls, globals())
application = app.wsgifunc()
