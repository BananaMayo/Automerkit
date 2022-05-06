from database import db
from flask import render_template, request, redirect

def get_polls():
    sql = "SELECT id, topic FROM polls WHERE visible=1 ORDER BY id ASC"
    return db.session.execute(sql).fetchall()

def create_poll(topic, creator_id):
    topic = request.form["topic"]
    sql = "INSERT INTO polls (creator_id, topic, created_at, visible) VALUES (:creator_id, :topic, NOW(), 1) RETURNING id"
    poll_id = db.session.execute(sql, {"topic":topic, "creator_id":creator_id}).fetchone()[0]

    choices = request.form.getlist("choice")
    for choice in choices:
        if choice != "":
            sql = "INSERT INTO choices (poll_id, choice) VALUES (:poll_id, :choice)"
            db.session.execute(sql, {"poll_id":poll_id, "choice":choice})
    
    if "correct" in request.form:
        correct = request.form["correct"]
        sql = "INSERT INTO choices (poll_id, correct_choice) VALUES (:poll_id, :correct_choice)"
        db.session.execute(sql, {"poll_id":poll_id, "correct_choice":correct}) 
    
    if "image" in request.form:
        image = request.form["image"]
        sql_ = "INSERT INTO choices (poll_id, image) VALUES (:poll_id, :image)"
        db.session.execute(sql_, {"poll_id":poll_id, "image":image})

    db.session.commit()
    return poll_id


def get_poll_topic(id):
    sql = "SELECT topic FROM polls WHERE id=:id"
    result = db.session.execute(sql, {"id":id})
    topic = result.fetchone()[0]
    return topic
    
def get_poll_choices(id):
    sql = "SELECT id, choice FROM choices WHERE poll_id=:id"
    result = db.session.execute(sql, {"id":id})
    choices = result.fetchall()
    return choices

def get_picture(id):
    sql = "SELECT ENCODE(image,'base64') as base64 FROM choices WHERE poll_id=:id"
    result = db.session.execute(sql, {"id":id})
    image = result.fetchone()[0]
    return image

def get_choice(choice_id):
    sql = "SELECT choice, correct_choice FROM choices WHERE id=:choice_id"
    return db.session.execute(sql, {"choice_id":choice_id}).fetchone()

def correct_answer(id):
    sql = "SELECT correct_choice FROM choices WHERE poll_id=:id and choice=''"
    correct = db.session.execute(sql, {"id":id}).fetchone()[0]
    db.session.commit()
    return correct

def remove_poll(poll_id, user_id):
    sql = "UPDATE polls SET visible=0 WHERE id=:id AND creator_id=:user_id"
    db.session.execute(sql, {"id":poll_id, "user_id":user_id})
    db.session.commit()
    
def my_polls(user_id):
    sql = "SELECT id, topic FROM polls WHERE creator_id=:user_id AND visible=1 ORDER BY topic"
    return db.session.execute(sql, {"user_id":user_id}).fetchall()