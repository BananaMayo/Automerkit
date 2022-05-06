from app import app
from flask import render_template, request, redirect
import users
import polls
import statistic

@app.route("/")
def index():
    return render_template("index.html", polls=polls.get_polls())

@app.route("/new", methods=["GET", "POST"])
def new():
    return render_template("new.html")

@app.route("/create", methods=["GET", "POST"])
def create():
    users.require_role(2)

    if request.method == "GET":
        return render_template("new.html")

    if request.method == "POST":
        users.check_csrf()

        topic = request.form["topic"]
        if len(topic) < 1 or len(topic) > 15:
            return render_template("error.html", message="Automerkissä tulee olla 1-15 merkkiä")
        
        image = request.form["image"]
        if not image:
            return render_template("error.html", message="Et valinnut kuvaa")

        poll = polls.create_poll(topic, users.user_id())
        return redirect("/poll/"+str(poll))

@app.route("/poll/<int:id>")
def play_poll(id):
    users.require_role(1)
    image = polls.get_picture(id)
    topic = polls.get_poll_topic(id)
    choices = polls.get_poll_choices(id)

    return render_template("poll.html", id=id, topic=topic, choices=choices, base64=image)


@app.route("/answer", methods=["POST"])
def answer():

    #id = request.form["id"]
    answer = request.form["answer"]

    #correct = polls.correct_answer(id)
    #choices = polls.get_choice(poll_id)
    return render_template("answer.html", answer = answer)

@app.route("/statistics")
def poll_statistics():
    users.require_role(2)
    data = statistic.all_stats(users.user_id())
    return render_template("statistics.html", data=data)


@app.route("/remove", methods=["GET", "POST"])
def remove():
    users.require_role(2)

    if request.method == "GET":
        my_polls = polls.my_polls(users.user_id())
        return render_template("remove.html", list=my_polls)
    
    if request.method == "POST":
        users.check_csrf()

        if "poll" in request.form:
            poll = request.form["poll"]
            polls.remove_poll(poll, users.user_id())

        return redirect("/")


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
            return render_template("error.html", message="Salasanat eivät täsmää")
        if password1 == "":
            return render_template("error.html", message="Salasanan kenttä on tyhjä")

        role = request.form["role"]
        if role not in ("1", "2"):
            return render_template("error.html", message="Tuntematon käyttäjätaso")

        if not users.register(username, password1, role):
            return render_template("error.html", message="Rekisteröinti ei onnistunut")
        return redirect("/")
