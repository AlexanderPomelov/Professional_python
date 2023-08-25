import datetime

from application.salary import calculate_salary
from application.people import get_employees

if __name__ == '__main__':
    print(f'Знакомство с модулем datetime - вывод сегодняшней даты и времени: {datetime.datetime.today()}')

    calculate_salary(2,2)

    get_employees('Vasya')


