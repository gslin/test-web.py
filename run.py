#!/usr/bin/env python3

import web

urls = ()
app = web.application(urls, globals())
application = app.wsgifunc()
