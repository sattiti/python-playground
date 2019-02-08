# -*- coding: utf-8 -*-

import responder

api = reponsder.API()

@route('/')
def index(res, resp):
  resp.text = 'hello world'


if __name__ == '__main__':
  api.run()
