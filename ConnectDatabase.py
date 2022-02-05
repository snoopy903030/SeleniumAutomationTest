import mysql.connector

mydb = mysql.connector.connect(
    host = 'LOCALHOST',
    user = 'root',
    password = 'Templ@te',
    database = 'unsplash'
)

mycursor = mydb.cursor()
mycursor.execute("select * from unsplash.logininfo")
myresult = mycursor.fetchall()

for x in myresult:
  print(x)
