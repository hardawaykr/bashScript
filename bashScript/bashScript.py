from flask import Flask, abort, request
from flask import render_template
from utils import Trie
app = Flask(__name__)

@app.route("/")
def home():
    trie = Trie()
    return render_template("bashScript.html")

@app.route("/input")
def input():
    query = request.args.get("test")
    if query == "help":
        return render_template("help.html")
    else:
        tokens = query.split(" ")
        if tokens[0] == 'alias':
            if len(tokens) == 3:
                return render_template("alias.html", shortcut=tokens[1],
                        command=tokens[2])
            else:
                abort(404)
        else:
            abort(404)

if __name__ == '__main__':
    app.run(port=5000, debug=True)
