import pyodbc
from twitter_program import credentials
from twitter_program import zamianaZnakow as zz



def select(table):
    table = zz.odkoduj(table)
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

def query(conn,query):
    
    with conn.cursor() as cursor:
        try:
            cursor = conn.cursor()
            cursor.execute(query)
        except:  
            print(query)
            
def create(conn,table):
    table = zz.odkoduj(table)
    string = "if not exists (select * from sysobjects where name='" + table +"' and xtype='U') CREATE TABLE " + table +" (content ntext, date ntext,sentiment int);"
    query(conn,string)

def close(conn):
    conn.close()

def connect():
    server = credentials.server
    database = credentials.database
    username = credentials.username
    password = credentials.password 
    driver = credentials.driver
    return pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)
    
def insert(conn,table,content,date,sentiment):
    table = zz.odkoduj(table)
    content.replace("'","")
    string = "INSERT INTO [" + table + "] (content, date, sentiment) VALUES ('"+ content + "','"+ date + "','"+ str(sentiment) + "');"
    query(conn,string)

def drop(conn,table):
    table = zz.odkoduj(table)
    string = "if exists (select * from sysobjects where name='" + table +"' and xtype='U') DROP TABLE " + table +";"
    query(conn,string)

def deleteFromController(conn,table,name):
    table = zz.odkoduj(table)
    string = "DELETE FROM " + table +" WHERE name = '" + name + "';"
    query(conn,string)

def insertIntoController(conn,name):
    string = "INSERT INTO CONTROLLER (name) VALUES ('"+ name + "');"
    query(conn,string)

def createController(conn):
    string = "if not exists (select * from sysobjects where name='CONTROLLER' and xtype='U') CREATE TABLE CONTROLLER (name ntext);"
    query(conn,string)

def resetAll(conn):
    hashtags = ["kwarantanna", "vege","IgaŚwiatek","hot16challange","fitness","krolowezycia","kryzys","ikea","łódź","haloween","kawa","radom","karmieniepiersia","pomidorowa","COVID19","nvidia","poniedziałek","biedronka"]
    for hashtag in hashtags:
        drop(conn,hashtag)
        create(conn,hashtag)

def resetHashtag(conn,hashtag):
    drop(conn,hashtag)
    create(conn,hashtag)
