from flask import Flask, abort, request
from flask import render_template
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("bashScript.html")

@app.route("/input")
def input():
    query = request.args.get("test")
    if query == "help":
        return render_template("help.html")
    else:
        return abort(404)

if __name__ == '__main__':
    app.run(port=5000, debug=True)
