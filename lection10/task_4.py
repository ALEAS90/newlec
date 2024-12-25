# Создайте класс с тестами и напишите фикстуры в conftest.py:
# 1) Фикстуру для класса и используйте её. Например, печать времени начала выполнения класса с тестами и окончания
# 2) Фикстуру для конкретного теста и используйте её не для всех тестов. Например, время выполнения теста.

import pytest

import time

@pytest.mark.usefixtures('for_class_fixt')
class Test:
    def test_0(self, time_start):
        time.sleep(2)
    def test_1(self, time_start):
        time.sleep(5)
        time.sleep(5)
    def test_2(self):
        time.sleep(3)
