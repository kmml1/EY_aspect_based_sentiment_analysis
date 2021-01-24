import pyodbc
import credentials


def select(table):
    select = "SELECT * FROM "+ table

    server = credentials.server
    database = credentials.database
    username = credentials.username
    password = credentials.password 
    driver = credentials.driver

    with pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password) as conn:
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

    with pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password) as conn:
        with conn.cursor() as cursor:
            cursor.execute(query)
            
def create(table):
    string = "if not exists (select * from sysobjects where name='" + table +"' and xtype='U') CREATE TABLE " + table +" (content ntext, date ntext,sentiment int);"
    query(string)

def insert(table,content,date,sentiment):
    string = "INSERT INTO " + table + " (content, date, sentiment) VALUES ('"+ content + "','"+ date + "','"+ str(sentiment) + "');"
    query(string)

def drop(table):
    string = "if exists (select * from sysobjects where name='" + table +"' and xtype='U') DROP TABLE " + table +";"
    query(string)

def deleteFromController(table,name):
    string = "DELETE FROM " + table +" WHERE name = '" + name + "';"
    query(string)

def insertIntoController(name):
    string = "INSERT INTO CONTROLLER (name) VALUES ('"+ name + "');"
    query(string)

def createController():
    string = "if not exists (select * from sysobjects where name='CONTROLLER' and xtype='U') CREATE TABLE CONTROLLER (name ntext);"
    query(string)

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

    create('TEST3')
    insert('TEST3','test','11.10.2021',1)
    table = select("TEST3")
    print(table.pop(0)[0])
    drop('TEST3')
test()
