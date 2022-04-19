from database import db

def all_stats(user_id):
    sql = """SELECT id, topic FROM polls
             WHERE visible=1 AND creator_id=:user_id ORDER BY topic"""
    polls = db.session.execute(sql, {"user_id": user_id}).fetchall()
    list_of_data = []

    for poll in polls:
        sql = """SELECT u.name, COUNT(*), COALESCE(SUM(a.result),0)
                 FROM choices c, users u, answers a
                 WHERE c.poll_id=:poll_id AND a.choice_id=c.id AND u.id=a.user_id
                 GROUP BY u.id, u.name ORDER BY u.name"""
        results = db.session.execute(sql, {"poll_id": poll[0]}).fetchall()
        list_of_data.append((poll[1], results))

    return list_of_data

def poll_stats(poll_id, user_id):
    sql = """SELECT COUNT(*), COALESCE(SUM(a.result),0) FROM choices c, answers a
             WHERE c.poll_id=:poll_id AND a.user_id=:user_id AND a.choice_id=c.id"""
    return db.session.execute(sql, {"poll_id":poll_id, "user_id":user_id}).fetchone()