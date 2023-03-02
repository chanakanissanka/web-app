from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "<html><body><h1>!!!Hello Welcome you all to Azure Core Services!!! V2</h1></body></html>\n"
