from random import randint
from database import db
from flask import render_template, request, redirect

#jos render_template ei toimi niin käytä esim: return db.session.execute(sql).fetchall()

def get_polls():
    sql = "SELECT id, topic, created_at FROM polls ORDER BY id DESC"
    result = db.session.execute(sql)
    polls = result.fetchall()
    return render_template("index.html", polls=polls)

def create_poll(topic, creator_id):
    topic = request.form["topic"]
    sql = "INSERT INTO polls (creator_id, topic, created_at, visible) VALUES (:creator_id, :topic, NOW(), 1) RETURNING id"
    poll_id = db.session.execute(sql, {"creator_id":creator_id, "topic":topic}).fetchone()[0]
    
    choices = request.form.getlist("choice")
    for choice in choices:
        if choice != "":
            sql = "INSERT INTO choices (poll_id, choice) VALUES (:poll_id, :choice)"
            db.session.execute(sql, {"poll_id":poll_id, "choice":choice})
    db.session.commit()
    return poll_id

    #<p>Auton kuva:<br>
    #<input type="file" accept="image/*" /> <br>

def answer_poll(id):
    sql = "SELECT topic FROM polls WHERE id=:id"
    result = db.session.execute(sql, {"id":id})
    topic = result.fetchone()[0]
    sql = "SELECT id, choice FROM choices WHERE poll_id=:id"
    result = db.session.execute(sql, {"id":id})
    choices = result.fetchall()
    return render_template("poll.html", id=id, topic=topic, choices=choices)

def send_answer():
    poll_id = request.form["id"]
    if "answer" in request.form:
        choice_id = request.form["answer"]
        sql = "INSERT INTO answers (choice_id, sent_at) VALUES (:choice_id, NOW())"
        db.session.execute(sql, {"choice_id":choice_id})
        db.session.commit()
    return redirect("/result/" + str(poll_id))

#def result(id):
#    sql = "SELECT topic FROM polls WHERE id=:id"
#    result = db.session.execute(sql, {"id":id})
#    topic = result.fetchone()[0]
#    sql = "SELECT c.choice, COUNT(a.id) FROM choices c LEFT JOIN answers a " \
#          "ON c.id=a.choice_id WHERE c.poll_id=:poll_id GROUP BY c.id"
#    result = db.session.execute(sql, {"poll_id":id})
#    choices = result.fetchall()
#    return render_template("result.html", topic=topic, choices=choices)


def remove_poll(poll_id, user_id):
    sql = "UPDATE polls SET visible=0 WHERE id=:id AND creator_id=:user_id"
    db.session.execute(sql, {"id":poll_id, "user_id":user_id})
    db.session.commit()
    

def my_polls(user_id):
    sql = "SELECT id, topic FROM polls WHERE creator_id=:user_id AND visible=1 ORDER BY topic"
    return db.session.execute(sql, {"user_id":user_id}).fetchall()