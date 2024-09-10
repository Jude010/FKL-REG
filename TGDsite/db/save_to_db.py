from . import connect

def save_to_db(project , user , signature , date):
    #save project to db
    conn = connect.get_db_conn()

    cur = conn.cursor()

    # insert project details into DB and recieve new project ID
    cur.execute("INSERT INTO project (pname , privacy , floors , user_id) SELECT '" + project['name'] + "' ,'" + project['privacy'] + "' ,'"  + project['floors'] + "', user_id FROM users  WHERE username = '" + user + "' RETURNING proj_id ;")
    pid = cur.fetchone()[0]
    conn.commit()

    # insert signature date and pid into signatures DB
    cur.execute("INSERT INTO signatures (sig , date , proj_id) VALUES ('" + signature + "' ,'" + str(date)  + "' ,'" + str(pid) + "')")
    conn.commit()

    # for each stair in project inser data into db and connect the project id and stair id in DB
    for i in range(project['stair_num']) :
        stair = project['stairs'][str(i)]
        cur.execute("INSERT INTO stairs (name , rise , part_m, inside) values ('" + stair['name'] + "' ,'" + stair['rise']  + "' ,'" + str(stair['part_m']) + "' ,'" + stair['inside'] + "') RETURNING stair_id;")
        sid = cur.fetchone()[0]
        cur.execute("INSERT INTO proj_stair (stair_id , proj_id) values ('" + str(sid) + "' ,'" + str(pid) + "')")
        conn.commit()

    conn.close()
    