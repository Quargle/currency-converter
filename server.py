from flask import Flask, send_from_directory
import random

app = Flask(__name__)


@app.route("/")
def hello():
    #return "<h1>Hello from Flask!</h1>"
    return send_from_directory('client/public', 'index.html')



# Path for all the static files (compiled JS/CSS, etc.)
@app.route("/<path:path>")
def home(path):
    return send_from_directory('client/public', path)



@app.route("/get_data")
def get_data():
    # call currency data api from site like fixer.io
    return "return from api"

if __name__ == "__main__":
    app.run(debug=True, port=3000)