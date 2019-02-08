# -*- coding: utf-8 -*-
import requests
from flask import Flask, request, jsonify
from flask import render_template
from jinja2 import Environment, FileSystemLoader

app = Flask(__name__)
# set templates directory
app.jinja_loader = FileSystemLoader('res')

# print page
@app.route("/")
def index():
  doc = """<!DOCTYPE html>
  <html lang="ja">
  <head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>HOME</title>
  </head>
  <body>
  <div class="wrapper">
  <header id="header">
  <h1 id="logo">LOGO</h1>
  <nav>
  <ul id="hnav">
  <li class="hn" id="hn0"><a href="/">HOME</a></li>
  <li class="hn" id="hn1"><a href="/about">About</a></li>
  <li class="hn" id="hn2"><a href="/works/">Works</a></li>
  <li class="hn" id="hn3"><a href="/contact/">Contact</a></li>
  </ul>
  </nav>
  </header>
  </div>
  <div class="wrapper">
  <main id="contents">
  <h2>main page</h2>
  <p>hello</p>
  <div class="tb0">
  <table>
  <tr>
  <th><div><p>name</p></div></th>
  <th>value</th>
  </tr>
  <tr>
  <td><div><p>aaa</p></div></td>
  <td>bbb</td>
  </tr>
  </table>
  </div>
  </main>
  </div>
  <div class="wrapper">
  <footer id="footer">
  <nav>
  <ul id="fnav">
  <li class="fn" id="fn0"><a href="/">HOME</a></li>
  <li class="fn" id="fn1"><a href="/about/">About</a></li>
  <li class="fn" id="fn2"><a href="/works/">Works</a></li>
  <li class="fn" id="fn3"><a href="/contact/">Contact</a></li>
  </ul>
  </nav>
  </footer>
  </div>
  </body>
  </html>
  """
  return doc


# load template
@app.route('/about')
def about():
  return render_template('index.html')


# get json from other api
@app.route('/jsontest', methods=['GET'])
def jsontest():
  u = ''
  param = request.args.get('p')
  apiurl = '{}{}'.format(u, param)
  r = requests.get(apiurl)
  return jsonify(r.content)

if __name__ == "__main__":
  app.run()
