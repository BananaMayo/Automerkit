from app import app
from flask import render_template, request, redirect
import users
import polls

#from database import db
#täytyy korjata db. alkuiset toiminnot

@app.route("/")
def index():
    return render_template("index.html", polls=polls.get_polls())

@app.route("/create", methods=["POST", "GET"])
def create_poll():
    users.require_role(2)

    if request.method == "GET":
        return render_template("new.html")

    if request.method == "POST":
        users.check_csrf()

        text = request.form["text"]
        if len(text) < 1 or len(text) > 15:
            return render_template("error.html", message="Automerkissä tulee olla 1-15 merkkiä")
        
        poll = polls.create_poll()
        return redirect("/deck/"+str(poll))


@app.route("/new")
def new():
    return render_template("new.html")


@app.route("/poll/<int:id>")
def poll(id):
    users.require_role(1)
    return render_template("poll.html", answer=polls.answer_poll(id))
    
### KOKEILU, ei välttämättä toimi
@app.route("/answer", methods=["POST"])
def answer():
        return render_template(polls.send_answer())


###stats TÄMÄ PITÄÄ KORJATA
@app.route("/result/<int:id>")
def results():
    pass

#### TEE TÄMÄ SEURAAVAKSI
@app.route("/remove")
def remove():
    pass


###Login osuus

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if not users.login(username, password):
            return render_template("error.html", message="Väärä tunnus tai salasana")
        return redirect("/")

@app.route("/logout")
def logout():
    users.logout()
    return redirect("/")

@app.route("/register", methods=["get", "post"])
def register():
    if request.method == "GET":
        return render_template("register.html")

    if request.method == "POST":
        username = request.form["username"]
        if len(username) < 1 or len(username) > 20:
            return render_template("error.html", message="Tunnuksessa tulee olla 1-20 merkkiä")

        password1 = request.form["password1"]
        password2 = request.form["password2"]
        if password1 != password2:
            return render_template("error.html", message="Salasanat eroavat")
        if password1 == "":
            return render_template("error.html", message="Salasana on tyhjä")

        role = request.form["role"]
        if role not in ("1", "2"):
            return render_template("error.html", message="Tuntematon käyttäjärooli")

        if not users.register(username, password1, role):
            return render_template("error.html", message="Rekisteröinti ei onnistunut")
        return redirect("/")