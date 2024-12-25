# Напишите 5 тестов на функцию all_division. Обязательно должен быть тест деления на ноль.
# Промаркируйте часть тестов. Например, smoke.
# В консоли с помощью pytest сделайте вызов:
# 1) Всех тестов
# 2) Только с маркером smoke
# 3) По маске. Выберите такую маску, чтобы под неё подпадали не все тесты, но больше одного
# Пришлите на проверку файл с тестами и скрины с вызовами и их результаты

import pytest



def all_division(*arg1):
    division = arg1[0]
    for i in arg1[1:]:
        division /= i
        # print(i)
    # print(division)

    return division


# all_division(1,-2,-2)

"""Тесты"""

@pytest.mark.smoke
def test_value():
    assert all_division(10, 10) == 1, 'проверка результата решения'

def test_zero():
    with pytest.raises(ZeroDivisionError):
        all_division(4, 3, 0, 8)


def test_numbers():
    with pytest.raises(TypeError):
        all_division(4, 'd', 0, 8)


def test_index_error():
    with pytest.raises(IndexError):
        all_division(), 'не хватает аргументов'

@pytest.mark.smoke
def test_negative_numbers():
    assert all_division(1,-2,-2) == 0.25

