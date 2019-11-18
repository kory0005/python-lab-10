import sqlite3
import base64


# CONNECTION
conn = sqlite3.connect('week10.db')
c = conn.cursor()


# CREATE NEW ROW
while True:
    link = input('Link in base64 format: ')
    city = input('City: ')
    country = input('Country: ')
    student = input('Student: ')
    c.execute("INSERT INTO lab10 (link,city,country,student) VALUES('{}','{}','{}','{}')".format(link, city, country, student))
    print("Record Added Successfully!")
    conn.commit()

c.close()
conn.close()