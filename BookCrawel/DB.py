'''
Created on Nov 24, 2016

@author: zhangxing
'''

import configparser
import os
import mysql.connector as mysql

config = configparser.ConfigParser()
cnf_path=os.path.join(os.path.join(os.path.dirname(os.getcwd()),'Config'),'mysql.cnf')
config.read(cnf_path)


host = config.get('mysql', 'host')
user = config.get('mysql','user')
psd = config.get('mysql','password')
db = config.get('mysql','database')
port = config.getint('mysql','port')
charset = config.get('mysql','charset')


def get_connnection():
    try:
        conn = mysql.connect(host=host, port=port,user=user,password=psd,database=db)
    except Exception as e:
        print(e)
    return conn

def execute(sql):
    conn = get_connnection();
    try:
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
    except Exception as e:
        print(e)
    
    finally:
        cur.close()
        conn.close()
        


if __name__=='__main__':
    
#     conn = get_connnection()
#     sql = 'insert into test values(1565,\'first haha\');'
#     cur = conn.cursor()
#     cur.execute(sql)  
#     cur.execute("select * from test")
#     for i in cur:
#         print(i)
#          
#     conn.commit()
#     cur.close()
#     conn.close()

    sql = 'insert into test values(65,\'second\');'
    execute(sql)
        
