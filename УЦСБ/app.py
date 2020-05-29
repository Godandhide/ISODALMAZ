from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
@app.route('/home')
def index():
    return render_template("index.html")


@app.route('/vova')
def vova():
    return render_template("index_vova.html")


if __name__ == "__main__":
    app.run(debug=True)