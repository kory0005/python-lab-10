import sqlite3
import base64
import webbrowser


# CONNECTION
conn = sqlite3.connect('week10.db')
c = conn.cursor()
# query = 'SELECT id, link FROM lab10'
# result = c.execute(query)


# ADDING NEW ROWS
c.execute('INSERT INTO lab10 (link,city,country,student) VALUES("aHR0cHM6Ly93d3cuZ29vZ2xlLmNvbS9tYXBzL3BsYWNlL0toYXJraXYsK09ibGFzdCtkZStLaGFya2l2LCtVa3JhaW5lL0A0OS45OTQ1MDcsMzYuMTQ1NzQyLDExei9kYXRhPSEzbTEhNGIxITRtNSEzbTQhMXMweDQxMjdhMDlmNjNhYjBmOGI6MHgyZDRjMTg2ODFhYTRiZTBhIThtMiEzZDQ5Ljk5MzUhNGQzNi4yMzAzODM=", "Kharkiv", "Ukraine", "Nonna")')
c.execute('INSERT INTO lab10 (link,city,country,student) VALUES("aHR0cHM6Ly93d3cuZ29vZ2xlLmNvbS9tYXBzL3BsYWNlL0FtaWVucywrRnJhbmNlL0A0OS44OTg1NDA4LDIuMjE0NTk3OCwxMnovZGF0YT0hM20xITRiMSE0bTUhM200ITFzMHg0N2U3ODQxM2Q3OGI3NjBiOjB4NDBhZjEzZTgxNjIyMGUwIThtMiEzZDQ5Ljg5NDA2NyE0ZDIuMjk1NzUz", "Amiens", "France", "Jerome")')
c.execute('INSERT INTO lab10 (link,city,country,student) VALUES("aHR0cHM6Ly93d3cuZ29vZ2xlLmNvbS9tYXBzL3BsYWNlL0lzcGFoYW4sK0lyYW4vQDMyLjY2MjIxMDcsNTEuNTQ2NTk3NCwxMXovZGF0YT0hM20xITRiMSE0bTUhM200ITFzMHgzZmJjMzVmZThjMzI2Nzk5OjB4N2FiNTc4MTZlZjU4MzdmNSE4bTIhM2QzMi42NTM4OTY2ITRkNTEuNjY1OTY1Ng==", "Isfahan", "Iran", "Saba")')
c.execute('INSERT INTO lab10 (link,city,country,student) VALUES("aHR0cHM6Ly93d3cuZ29vZ2xlLmNvbS9tYXBzL3BsYWNlL0lzcGFoYW4sK0lyYW4vQDMyLjY2MjIxMDcsNTEuNTQ2NTk3NCwxMXovZGF0YT0hM20xITRiMSE0bTUhM200ITFzMHgzZmJjMzVmZThjMzI2Nzk5OjB4N2FiNTc4MTZlZjU4MzdmNSE4bTIhM2QzMi42NTM4OTY2ITRkNTEuNjY1OTY1Ng==", "Lviv", "Ukraine", "Illya")')
c.execute('INSERT INTO lab10 (link,city,country,student) VALUES("aHR0cHM6Ly93d3cuZ29vZ2xlLmNvbS9tYXBzL3BsYWNlL0lzcGFoYW4sK0lyYW4vQDMyLjY2MjIxMDcsNTEuNTQ2NTk3NCwxMXovZGF0YT0hM20xITRiMSE0bTUhM200ITFzMHgzZmJjMzVmZThjMzI2Nzk5OjB4N2FiNTc4MTZlZjU4MzdmNSE4bTIhM2QzMi42NTM4OTY2ITRkNTEuNjY1OTY1Ng==", "Gold Coast", "Australia", " ")')
conn.commit()
print("Record Updated successfully ")

c.close()
conn.close()