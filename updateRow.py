import sqlite3

# CONNECTION
conn = sqlite3.connect('week10.db')
c = conn.cursor()

# CREATE NEW DATA
while True:
    city = input('City: ')
    country = input('Country: ')
    student = input('Student: ')
    newId = input('id: ')
    c.execute("UPDATE lab10 SET City='{}', Country='{}', Student='{}' WHERE id={}".format(city, country, student, newId))
    print("Record Updated successfully ")
    conn.commit()


c.close()
conn.close()