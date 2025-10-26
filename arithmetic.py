print("Решите данный пример: 4*100-54=?")
correct=4*100-54
user=input("Введите свой вариант ответа: ")
user=int(user)
if correct == user:
    print("Вверный ответ!")
else:
    print("Не верный ответ! Вот верный: "+str(correct))