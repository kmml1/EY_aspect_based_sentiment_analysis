import pyodbc
def select(table):
    select = "SELECT * FROM "+ table
    server = 'tcp:twitterstorage.database.windows.net'
    database = 'TwitterStorage'
    username = 'lukasikb'
    password = 'Okon123!'   
    driver= '{SQL Server}'

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

    server = 'tcp:twitterstorage.database.windows.net'
    database = 'TwitterStorage'
    username = 'lukasikb'
    password = 'Okon123!'   
    driver= '{SQL Server}'

    with pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password) as conn:
        with conn.cursor() as cursor:
            cursor.execute(query)
            
def create(table):
    string = "if not exists (select * from sysobjects where name='" + table +"' and xtype='U') CREATE TABLE " + table +" (content ntext, date ntext);"
    query(string)

def insert(table,content,date):
    string = "INSERT INTO " + table + " (content, date) VALUES ('"+ content + "','"+ date + "');"
    query(string)

def drop(table):
    string = "if exists (select * from sysobjects where name='" + table +"' and xtype='U') DROP TABLE " + table +";"
    query(string)

def deleteFromController(table,name):
    string = "DELETE FROM " + table +" WHERE name = '" + name + "';"
    query(string)

def insertIntoController(name,refresh,lastId):
    string = "INSERT INTO CONTROLLER (name, refresh,lastId) VALUES ('"+ name + "',"+ str(refresh) + ", " + str(lastId) + ");"
    query(string)

def createController():
    string = "if not exists (select * from sysobjects where name='CONTROLLER' and xtype='U') CREATE TABLE CONTROLLER (name ntext, refresh int, lastId int);"
    query(string)

def test():
    create('TEST')
    insert('TEST','test1','9.11.2021')
    table = select("TEST")
    print(table.pop(0)[0])
    createController()
    insertIntoController('test2',10,1)
    table = select("CONTROLLERTEST")
    print(table.pop(0)[0])
    drop('CONTROLLERTEST')
    drop('TEST')
test()