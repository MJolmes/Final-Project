from flask import render_template, redirect, url_for, Blueprint

my_view = Blueprint('my_view', __name__)


@my_view.route("/")
def page1():
    return render_template("index1.html")

@my_view.route("/page2")
def page2():
    return render_template("index2.html")

@my_view.route("/page3")
def page3():
    return render_template("index3.html")

@my_view.route("/page4")
def page4():
    return render_template("index4.html")

@my_view.route("/page5")
def page5():
    return render_template("index5.html")

@my_view.route("/admin_page")
def admin_page():
    return render_template("admin.html")




@my_view.route("/home")
def home_redirect():
    return redirect(url_for("my_view.page1"))

@my_view.route("/javascript")
def java_redirect():
    return redirect(url_for("my_view.page1"))

@my_view.route("/js")
def js_redirect():
    return redirect(url_for("my_view.page1"))

@my_view.route("/admin")
def admin_redirect():
    return redirect(url_for("my_view.admin_page"))

