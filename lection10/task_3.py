# Из набора тестов задания task_2 создайте один тест с параметрами, используя @pytest.mark.parametrize
# Промаркируйте 1 параметр из выборки как smokе, а 1 набор данных скипните

import pytest


def all_division(*arg1):

    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division


# all_division(2, 4, 89)

@pytest.mark.parametrize("a, b, result", [pytest.param(10, 10, 1, marks=pytest.mark.smoke),
                                          (10, 1.6, 6.25),
                                          (-7, 1, -7),
                                          (0, 4, 0),
                                          pytest.param(1, -2, -0.5, marks=pytest.mark.skip("тест скипнут"))])
def test_value(a, b, result):
    assert all_division(a, b) == result, 'проверка результата решения'







# @pytest.mark.smoke
# def test_value():
#     assert all_division(10, 10) == 1, 'проверка результата решения'
#
#
# # def test_zero():
# #     with pytest.raises(ZeroDivisionError):
# #         all_division(4, 3, 0, 8)
#
# @pytest.mark.parametrize('x',[4,1])
# @pytest.mark.parametrize('y',[0,0])
# def test_zero(x,y):
#     try:
#         all_division(x,y)
#     except ZeroDivisionError:
#         print('деление на ноль')
#     # with pytest.raises(ZeroDivisionError):
#     #      all_division(x, y)
#
# @pytest.mark.skip('скипнут исходя из условий задания')
# def test_numbers():
#     with pytest.raises(TypeError):
#         all_division(4, 'd', 0, 8)
#
#
# def test_index_error():
#     with pytest.raises(IndexError):
#         all_division(), 'не хватает аргументов'
#
# def test_negative_numbers():
#     assert all_division(1,-2,-2) == 0.25