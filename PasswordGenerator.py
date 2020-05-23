from random import *
import random
import string
from math import *


def rand_pass(num):
    """ Генерирует пароли

    :param num: length of password
    :return: randomly generated password
    """
    num_list = [str(randint(0, 9)) for i in range(floor(num/2))]
    u_let_list = [random.choice(string.ascii_letters) for i in range(ceil(num/2))]
    p = ''.join(num_list)
    p += ''.join(u_let_list)
    new_list = list(p)
    shuffle(new_list)
    new_list = ''.join(new_list)
    return new_list


def rand_pass_1(num):
    """ Генерирует пароли

        :param num: length of password
        :return: randomly generated password
        """
    s = string.ascii_letters + string.digits
    p = ''.join(sample(s, num))
    return p


length = int(input('Enter any number: '))
password = rand_pass(length)
print(password)
password_1 = rand_pass_1(length)
print(password_1)
