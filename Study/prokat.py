message = input("Какую машину хотите?: ")
print("Хорошо я посмотрю есть ли у нас " + message + ".")

table = input("На сколько месть вы хотите заказать стол?: ")
table = int(table)
if table >= 8:
    print("Извините у нас нет " + str(table) + " мест.")
else:
    print("Мы зарезервировали для вас " + str(table) + " мест")
