import random
from datetime import datetime, timedelta


def all_even_numbers():
    mylist = [x for x in range(0, 101, 2)]
    yield mylist


def random_increasing_number():
    y = 1
    while True:
        yield y
        m = int(random.uniform(0, 100))
        y += m


def next_day():
    today = datetime.today().date()
    for i in range(100):
        yield today
    today += timedelta(days=1)
