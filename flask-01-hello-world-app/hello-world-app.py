from flask import Flask 

app = Flask(__name__)

@app.route("/")
def head():
    return "<h1>Hello World from Betty!</h1>"

@app.route("/second")
def second():
    return "Peace at home peace in the world. M.Kemal Ataturk"

@app.route("/third/subthird")
def third():
    return "<h2>Our true mentor in life is science.M.Kemal Ataturk</h2>"

@app.route("/forth/<string:id>")
def forth(id):
    return f'Id of this page is {id}'


if __name__ == "__main__":
    app.run(debug=True)