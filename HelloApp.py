print("Hello Python from Visual Studio!")
s="*"*30
print(s)
print("NewProject")
print(s)
# Пользователь вводит курс доллара в рублях. Показать таблицу цен 1$, 2$, ..., 100$ в рублях,
# третьим столбцом добавить количество кг конфет, которые можно купить на данные суммы,
# если цена 1 кг конфет равна 20 руб. Пример: 1$ - 70 р - 3.5 кг и так далее (всего 10 строк)
d = 0
r = input("Введите курс доллара в рублях: ")
if r.isdigit():
    r = int(r)
    while d < 10:
        d += 1  # увеличивающаяся переменная под доллары
        a = (d*r)  # переменная для записи в неё рублей
        k = a/20  # для записи кг
        print("{0}$ - {1}р. - {2}кг." .format(d, a, k))
else:
    print("Ошибка, введите неотрицательное число")