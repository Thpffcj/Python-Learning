# _*_ coding: utf-8 _*_
__author__ = 'Thpffcj'

import MySQLdb

conn = MySQLdb.Connect(
	host='127.0.0.1',
	port=3306,
	user='root',
	passwd='000000',
	db='article_spider',
	charset='utf8'
)

cursor = conn.cursor()

print(conn)
print(cursor)

cursor.close()
conn.close()
