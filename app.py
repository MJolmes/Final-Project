from flask import Flask, render_template

from views import my_view

app = Flask(__name__)
app.register_blueprint(my_view)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html", e=e)

@app.errorhandler(500)
def server_down():
    return render_template("500.html")


if __name__ == "__main__":
    app.run(debug=True, port=8000)
