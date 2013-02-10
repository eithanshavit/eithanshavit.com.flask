from flask import Flask
from flask import render_template
from flask import send_from_directory
import os
app = Flask( __name__ )

menu = [
   { "name" : "about",
     "link" : "about" },
   { "name" : "websites",
     "link" : "websites" },
   { "name" : "apps",
     "link" : "apps" },
   { "name" : "hardware",
     "link" : "hardware" },
   { "name" : "github",
     "link" : "github" },
]


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'static/favicon.ico' )

@app.route('/<page>')
def page( page='index' ):
   return render_template( page + '.html', menu=menu, page=page )

@app.route('/')
@app.route('/index.html')
def index():
   return render_template( 'about.html', menu=menu, page='about' )

@app.errorhandler(404)
@app.errorhandler(500)
def page_not_found(error):
    return "Oops, are you in the right place?"

if __name__ == '__main__':
   app.debug = True
   app.run( host='0.0.0.0', port=80 )
