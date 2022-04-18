import psycopg2

conn= None
cur = None

try:
    #koden nedan kopplar till databasen
    #se postgres properties för att hitta rätt nycklar
    conn = psycopg2.connect(
                host = 'localhost',
                database = 'pytest',
                user = 'postgres',
                password = 'madoka22')

    cur = conn.cursor()

    #exekverar SQL queries
    #Syntax är samma som i SQL
    #'%s' är en placeholder för kommande variabler
    #sql kan utföras på två sätt, antinge med cur.execute eller create_script
    
    #cur.execute("CREATE TABLE pyexample (id int SERIAL PRIMARY KEY, name VARCHAR(50));")

    #cur.execute("INSERT INTO pyexample (name) VALUES(%s, %s)", ("Klaudia"))

    create_script = ''' CREATE TABLE IF NOT EXISTS pyexample(
                            id      int PRIMARY KEY,
                            name varchar(40) NOT NULL,
                            email varchar(40))'''
    cur.execute(create_script)

    insert_script = 'INSERT INTO pyexample (id, name, email) VALUES (%s, %s, %s,)'
    insert_value =(1, 'Klaudia')

    cur.execute(insert_script, insert_value)

    #detta sparar all SQL som man kör
    conn.commit()
except Exception as error:
    print(error)
finally:
    if cur is not None:
        cur.close()
    if cur is not None:
        conn.close()
