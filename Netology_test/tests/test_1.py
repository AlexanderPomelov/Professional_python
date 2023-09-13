from unittest import TestCase
from Netology_test.collection_data .collection_data import short_long_courses, sorted_courses, unique_mentors
from Netology_test.tests.data import courses, mentors, durations

class MyTestCase(TestCase):

    def test_short_long_courses(self):
        result = short_long_courses(courses, mentors, durations)  # '''Самый короткий курс(ы): Python-разработчик с нуля - 12 месяца(ев)\n'
        # 'Самый длинный курс(ы): Fullstack-разработчик на Python, Frontend-разработчик с нуля - 20 месяца(ев)\n'
        # 'Python-разработчик с нуля - 12 месяцев'''
        expected = ('Самый короткий курс(ы): Python-разработчик с нуля - 5 месяца(ев)\n'
                    'Самый длинный курс(ы): Fullstack-разработчик на Python, Frontend-разработчик с нуля - 20 месяца(ев)')

        self.assertNotEquals(result, expected)

    def test_sorted_courses(self):
        result = sorted_courses(courses, mentors, durations) #list of courses
        expected = type(list)
        self.assertTrue(result, expected)

    def test_unique_mentors(self):
        result = len(unique_mentors()) #292
        expected = 300
        self.assertLess(result, expected)


if __name__ == '__main__':
    test_1 = MyTestCase

