import sqlite3
conn = sqlite3.connect("database.sqlite")
cursor = conn.cursor() #получаем объект указателя соеденения

sql = "SELECT * FROM users where login =login" #формируем запрос
n = [("1")]
cursor.execute(sql,n) # передаема запрос к бд
a = cursor.fetchall()  #Получаем результат запроса в виде списка, в котором кортеж
print(a)


# Создание таблицы
#cursor.execute("""CREATE TABLE albums
#                  (title text, artist text, release_date text,
#                   publisher text, media_type text)
#               """)

