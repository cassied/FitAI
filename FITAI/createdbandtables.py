import sqlite3
conn=sqlite3.connect("fitai.db")
cursor=conn.cursor()

def tbcreatepeople():
    try:
        cursor.execute('''CREATE TABLE IF NOT EXISTS
            people( 
            userID INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
            username VARCHAR(20) NOT NULL UNIQUE,
            firstname VARCHAR(20) NOT NULL,
            surname VARCHAR(20) NOT NULL,
           password VARCHAR(20) NOT NULL,
           UNIQUE(userID, username)
           )''')
        conn.commit()
        print('Table Created Successfully')
    except sqlite3.Error as e:
        print(e)
def insertadminintopeople():
    try:
        cursor.execute('''INSERT INTO people(username, firstname, surname, password)
                   Values( 'Administrator', 'Ad', 'Min', 'abc')''')
        conn.commit()
        print('Admin Account Created Successfully')
    except sqlite3.Error as e:
        print('ERROR: Admin Account Already exsists')
def tbcreateinformation():
    try:
        cursor.execute('''CREATE TABLE IF NOT EXISTS
            information( 
            person INTEGER,
            age VARCHAR(20) NOT NULL,
            height VARCHAR(20) NOT NULL,
            weight VARCHAR(20) NOT NULL,
            workout VARCHAR(30) NOT NULL,
           goal VARCHAR(20) NOT NULL,
           FOREIGN KEY(person) REFERENCES people(userID)
           )''')
        conn.commit()
        print('Table Created Successfully')
    except sqlite3.Error as e:
        print(e)

    
tbcreatepeople()
insertadminintopeople()
tbcreateinformation()

conn.close()
