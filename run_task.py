# импортируем задачу add_two_numbers из файла task.py
from tasks import  add_two_numbrs

# используем асинрхронный для задачи add_two_numbrs
result = add_two_numbrs.delay (3,5)

# печатаем, что получилось
print(result.get())
