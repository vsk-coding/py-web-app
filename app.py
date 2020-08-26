from flask import Flask, render_template 
import os.path

app= Flask(__name__)


@app.route("/")
def index():
    with open("\\opt\\config\\myname", "r") as f: 
        content = f.read()
    return render_template('index.html', content = content)