from flask import Flask, render_template, request, redirect, url_for
from db import db
from models import usuarios

app = Flask (__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///dados.db"
db.init_app(app)

@app.route("/")
def home():
    users = db.session.query(usuarios).all()
    return render_template("index.html", users=users)

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    elif request.method == "POST":
        name = request.form["nameForm"]
        email = request.form["emailForm"]
        telefone = request.form["telefoneForm"]

        usuario = usuarios(name=name, email=email, telefone=telefone)
        db.session.add(usuario)
        db.session.commit()

        return redirect(url_for("home"))
    
@app.route("/delete/<int:id>")
def delete(id):
    user = db.session.query(usuarios).filter_by(id=id).first()
    db.session.delete(user)
    db.session.commit()

    return redirect(url_for("home"))

@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    user = db.session.query(usuarios).filter_by(id=id).first()
    if request.method == "GET":
        return render_template("edit.html", user=user)
    elif request.method == "POST":
        name = request.form["nameForm"]
        email = request.form["emailForm"]
        telefone = request.form["telefoneForm"]

    user.name = name
    user.email = email
    user.telefone = telefone
    db.session.commit()
    return redirect(url_for("home"))

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
