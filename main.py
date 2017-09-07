import sqlite3
conn = sqlite3.connect("database.sqlite") #Подключаемся к  бд
cursor = conn.cursor() #получаем объект указателя соеденения

login = input("Введите логин")
passs = input("Введите пароль")

sql ="SELECT * FROM users where login  = '{login}' and pass = '{passs}' ".format(login = login,passs=passs) #формируем запрос c использованием F строк
cursor.execute(sql) # передаема запрос к бд
sqel_request = cursor.fetchall()  #Получаем результат запроса в виде списка, в котором кортеж
if len(sqel_request) > 0:
    print("Вы успешно авторизовались под логином",login)
else:
    print("Вы ввели что-то не так")