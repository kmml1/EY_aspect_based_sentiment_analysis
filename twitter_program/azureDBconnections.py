import pyodbc
from twitter_program import credentials
from twitter_program import zamianaZnakow as zz


def select(table):
    table = zz.odkoduj(table)
    select = "SELECT * FROM " + table
    server = credentials.server
    database = credentials.database
    username = credentials.username
    password = credentials.password
    driver = credentials.driver

    with pyodbc.connect(
            'DRIVER=' + driver + ';SERVER=' + server + ';PORT=1433;DATABASE=' + database + ';UID=' + username + ';PWD=' + password) as conn:
        with conn.cursor() as cursor:
            cursor.execute(select)
            lista = []
            row = cursor.fetchone()
            while row:
                lista.append(row)
                row = cursor.fetchone()
            return lista


def query(query):
    server = credentials.server
    database = credentials.database
    username = credentials.username
    password = credentials.password
    driver = credentials.driver

    with pyodbc.connect(
            'DRIVER=' + driver + ';SERVER=' + server + ';PORT=1433;DATABASE=' + database + ';UID=' + username + ';PWD=' + password) as conn:
        with conn.cursor() as cursor:
            try:
                cursor.execute(query)
            except:
                print(query)


def create(table):
    table = zz.odkoduj(table)
    string = "if not exists (select * from sysobjects where name='" + table + "' and xtype='U') CREATE TABLE " + table + " (content ntext, date ntext,sentiment int);"
    query(string)


def insert(table, content, date, sentiment):
    table = zz.odkoduj(table)
    string = "INSERT INTO [" + table + "] (content, date, sentiment) VALUES ('" + content + "','" + date + "','" + str(
        sentiment) + "');"
    query(string)


def drop(table):
    table = zz.odkoduj(table)
    string = "if exists (select * from sysobjects where name='" + table + "' and xtype='U') DROP TABLE " + table + ";"
    query(string)


def deleteFromController(table, name):
    table = zz.odkoduj(table)
    string = "DELETE FROM " + table + " WHERE name = '" + name + "';"
    query(string)


def insertIntoController(name):
    string = "INSERT INTO CONTROLLER (name) VALUES ('" + name + "');"
    query(string)


def createController():
    string = "if not exists (select * from sysobjects where name='CONTROLLER' and xtype='U') CREATE TABLE CONTROLLER (name ntext);"
    query(string)


def resetAll():
    hashtags = ["kwarantanna", "vege", "IgaŚwiatek", "hot16challange", "fitness", "krolowezycia", "kryzys", "ikea",
                "łódź", "haloween", "kawa", "radom", "karmieniepiersia", "pomidorowa", "COVID19", "nvidia",
                "poniedziałek", "biedronka"]
    for hashtag in hashtags:
        drop(hashtag)
        create(hashtag)


def resetHashtag(hashtag):
    drop(hashtag)
    create(hashtag)


def test():
    """create('TEST')
    insert('TEST','twit1','1.11.2021',-1)
    insert('TEST','twit2','2.11.2021',1)
    insert('TEST','twit3','3.11.2021',1)
    insert('TEST','twit4','4.11.2021',-1)
    insert('TEST','twit5','5.11.2021',1)
    insert('TEST','twit6','6.11.2021',1)
    insert('TEST','twit7','7.11.2021',0)
    insert('TEST','twit8','8.11.2021',0)
    insert('TEST','twit9','9.11.2021',0)
    insert('TEST','twit10','10.11.2021',1)
    insert('TEST','twit11','11.11.2021',-1)
    create('TEST2')
    insert('TEST2','twit1','1.10.2021',-1)
    insert('TEST2','twit2','2.10.2021',0)
    insert('TEST2','twit3','3.10.2021',1)
    insert('TEST2','twit4','4.10.2021',0)
    insert('TEST2','twit5','5.10.2021',1)
    insert('TEST2','twit6','6.10.2021',1)
    insert('TEST2','twit7','7.10.2021',0)
    insert('TEST2','twit8','8.10.2021',1)
    insert('TEST2','twit9','9.10.2021',0)
    insert('TEST2','twit10','10.10.2021',1)
    insert('TEST2','twit11','11.10.2021',1)
    createController()
    insertIntoController('TEST1')
    insertIntoController('TEST2')
    table = select("CONTROLLER")
    print(table.pop(0)[0])
    print(table.pop(0)[0])"""

    # create('testowanie')
    # create('TEST3')
    # insert('TEST3','test','11.10.2021',1)
    # table = db.select("testowanie")
    # rekord = table.pop(0)
    # print(rekord[0]) # tekst
    # print(rekord[1]) # data
    # print(rekord[2]) # sentyment
    hashtags = ["kwarantanna", "vege", "IgaŚwiatek", "hot16challange", "fitness", "krolowezycia", "kryzys", "ikea",
                "łódź", "haloween", "kawa", "radom", "karmieniepiersia", "pomidorowa", "COVID19", "nvidia",
                "poniedziałek", "biedronka"]
    for hashtag in hashtags:
        table = select(hashtag)
        print(hashtag + " " + str(len(table)))


def abc():
    return select("COVID19")

print(abc()[1][1])