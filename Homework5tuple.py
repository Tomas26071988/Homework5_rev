
# 1. Создание переменной immutable_var с кортежем из нескольких элементов разных типов данных
immutable_var = (1, 2, 'a', 'b', True)

# 2. Вывод кортежа на экран
print("Immutable tuple:", immutable_var)

# 3. Попытка изменить элементы кортежа и объяснение
try:
    # Попытка изменить первый элемент кортежа
    immutable_var[0] = 100
except TypeError as e:
    print("Ошибка при изменении кортежа:", e)
    print("Невозможность изменять элементы кортежа объясняется тем, что кортежи являются неизменяемыми объектами. Это означает, что после их создания вы не можете изменять, добавлять или удалять элементы.")

# 4. Создание изменяемой структуры данных
mutable_list = [1, 2, 'a', 'b']  # Список из нескольких элементов

# Изменение элементов списка
mutable_list[0] = 100  # Изменяем первый элемент
mutable_list.append('Modified')  # Добавляем новый элемент в список

# Вывод измененного списка
print("Mutable list:", mutable_list)