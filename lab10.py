import sqlite3
import base64
import webbrowser


# CONNECTION
conn = sqlite3.connect('week10.db')
c = conn.cursor()
query = 'SELECT id, link FROM lab10'
result = c.execute(query)


# ASK FOR A RECORD
recordNum = input('Enter a record number between 1 and 29: ')


# QUIT | OPEN IN GOOGLE MAPS 
if recordNum == "q":
    print('See you later :)')
    exit
elif int(recordNum) <= 29 and int(recordNum) >= 1:
    c.execute("SELECT link FROM lab10 WHERE id={}".format(recordNum))
    link = c.fetchall()
    newLink = str(link).strip('[]')
    # decode string
    decodedLink = base64.b64decode(newLink)
    # open in browser
    webbrowser.open_new(decodedLink)
else:
    while True:
        print(input('Enter a record number between 1 and 29: '))


c.close()
conn.close()