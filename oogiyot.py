from flask import Flask
from flask import render_template
app = Flask( __name__ )

menu = [
   { "name" : "apps",
     "link" : "apps.html" },
   { "name" : "about",
     "link" : "about.html" },
]

@app.route('/')
@app.route('/index.html')
def index():
   return render_template( 'index.html', menu=menu )

@app.route('/email.html')
def email():
   return render_template( 'email.html', menu=menu )

@app.route('/apps.html')
def apps():
   return render_template( 'apps.html', menu=menu )

@app.route('/about.html')
def about():
   return render_template( 'about.html', menu=menu )

if __name__ == '__main__':
   app.debug = True
   app.run( host='0.0.0.0', port=80 )
