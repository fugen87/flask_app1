from flask import Flask, render_template, request, send_file, redirect, url_for, Response, redirect

app = Flask(__name__, static_folder = "static", template_folder = 'templates')
import sys
import os

@app.route('/', method=['GET','POST'])

def Menu_func():
    import os
    
    return render_template('Frontpage.html')
    
if __name__=="__main__":
    app.run(debug=True,host='localhost',port=8081)
