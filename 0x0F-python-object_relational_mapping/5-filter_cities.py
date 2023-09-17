#!/usr/bin/python3
'''a script that lists all states from the database hbtn_0e_0_usa'''
import MySQLdb
import sys


if __name__ == '__main__':
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()
    cur.execute("SELECT name FROM cities WHERE state_id\
                = (SELECT id FROM states WHERE name= %s)", (sys.argv[4], ))
    rows = cur.fetchall()
    string = ', '.join([str(row[0]) for row in rows])
    print(string)
    cur.close()
    db.close()
