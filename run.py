#!/usr/bin/env python3

import routing
import web

urls = routing.urls

app = web.application(urls, globals())
application = app.wsgifunc()
