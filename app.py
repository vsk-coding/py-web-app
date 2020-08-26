from flask import Flask, render_template 
import os.path

app= Flask(__name__)


@app.route("/")
def index():
    with open("/opt/config/myname", "r") as f: 
        content = f.read()
    return render_template('index.html', content = content)

if __name__ == "__main__":
     app.run(host='0.0.0.0', debug=True, port=5000)