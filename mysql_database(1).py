import pymysql


def database_creat(databasename):
    db=pymysql.connect(host='localhost',user='root',password='123456',port=3306)
    cursor=db.cursor()
    sql='CREATE DATABASE {} DEFAULT CHARACTER  SET utf8'.format(databasename)
    cursor.execute(sql)
    db.close()

def table_creat(databasename,sql):
    db=pymysql.connect(host='localhost',user='root',password='123456',port=3306,db=databasename)
    cursor=db.cursor()
    cursor.execute(sql)
    db.close()

def table_data_insert(databasename,sql):
    db = pymysql.connect(host='localhost', user='root', password='123456', port=3306, db=databasename)
    cursor = db.cursor()
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
    db.close()

#sql_creat = 'CREATE TABLE IF NOT EXISTS stars(id VARCHAR(625) NOT null,title VARCHAR(625) NOT null,href VARCHAR(625) NOT null, medium_get VARCHAR(625),time_get VARCHAR(625) not null ,detail_get VARCHAR(825) not null)'
