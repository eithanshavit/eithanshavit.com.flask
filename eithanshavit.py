from flask import Flask
from google.appengine.ext.webapp.util import run_wsgi_app
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
   { "name" : "photography",
     "link" : "photography" },
   { "name" : "github",
     "link" : "github" },
]

verbalClockImages = {
   "final" : [
      { "name" : "vc_front.jpg"},
      { "name" : "vc_frontclose.jpg"},
      { "name" : "vc_frontclose2.jpg"},
   ],
   "hardware" : [
      { "name" : "vc_layout.png"},
      { "name" : "vc_schematics.png"},
      { "name" : "vc_pcb.jpg"},
      { "name" : "vc_assembled.jpg"},
      { "name" : "vc_witharduino.jpg"},
   ],
   "plastic" : [
      { "name" : "vc_wordpanel.jpg"},
      { "name" : "vc_holepanel.jpg"},
      { "name" : "vc_cutout.jpg"},
   ],
   "craft" : [
      { "name" : "vc_leds.jpg"},
      { "name" : "vc_finalback.jpg"},
   ],
}


@app.route( '/favicon.ico' )
def favicon():
    return send_from_directory( os.path.join( app.root_path, 'static'), 'favicon.png' )

@app.route( '/hardware.html' )
@app.route( '/hardware' )
def hardware():
   return render_template( 'hardware.html', menu=menu, page='hardware',
   vcImages=verbalClockImages )

@app.route( '/<page>' )
def page( page='index' ):
   return render_template( page + '.html', menu=menu, page=page )

@app.route( '/' )
@app.route( '/index.html' )
def index():
   return render_template( 'about.html', menu=menu, page='about' )


@app.errorhandler( 404 )
@app.errorhandler( 500 )
def page_not_found( error ):
   return "Oops, are you in the right place?"

if __name__ == '__main__':
   run_wsgi_app( app )
