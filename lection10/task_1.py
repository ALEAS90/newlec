# Напишите генератор generate_random_name(), используя модуль random,
# который генерирует два слова из латинских букв от 1 до 15 символов, разделенных пробелами
# Например при исполнении следующего кода:
# gen = generate_random_name()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
#
# Выводится:
# tahxmckzexgdyt ocapwy
# dxqebbukr jg
# aym jpvezfqexlv
# iuy qnikkgxvxfxtxv

import random
import string

alpha = string.ascii_lowercase


def generate_random_name(alpha):
    while True:
        first_word = ''
        second_word = ''

        for word in range(random.randrange(1, 15, 1)):
            first_word += random.choice(alpha)
        for word in range(random.randrange(1, 15, 1)):
            second_word += random.choice(alpha)

        yield str(first_word) + " " + str(second_word)


gen = generate_random_name(alpha)
gen

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

