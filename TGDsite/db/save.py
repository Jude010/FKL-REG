import connect

def save_to_db(project):
    #save project to db
    conn = connect.get_db_conn()
    cur = conn.cursor()

    cur.execute("INSERT INTO project (name , privacy , floors)")
