from flask import Flask, render_template, request, url_for

app = Flask(__name__)


@app.route("/index/<name>/<group>")
def view_home(name,group):
    return render_template("layout.html",name=name,group=group)


if __name__ == "__main__":
    app.run()