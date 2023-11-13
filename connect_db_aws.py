import psycopg2


try:
    conn = psycopg2.connect(
        database="db",
        user="project",
        password="project",
        host="project1.cttzgmxwwmvp.eu-east-3.rds.amazonaws.com",
        port="5432"
    )

    #print(conn.info)

    cursor = conn.cursor()
    cursor.execute('SELECT * FROM information_schema.tables')
    rows = cursor.fetchall()
    for table in rows:
        print(table)

    conn.close()


except Exception as e:
    print("An error occurred:", str(e))
    import traceback
    print("Traceback:", traceback.format_exc())