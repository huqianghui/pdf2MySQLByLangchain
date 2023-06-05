import mysql.connector


mydb = mysql.connector.connect(
    host="codex-sample-server.mysql.database.azure.com",
    user="huqianghui",
    password="XXXXX",
    database="codex-sample"
)

def insert_sql(sql):
    mycursor = mydb.cursor()
    mycursor.execute(sql)
    print("Number of rows inserted: %d" % mycursor.rowcount)
    mycursor.close()
    mydb.commit()
    mydb.close()
