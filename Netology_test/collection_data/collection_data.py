from Netology_test.tests.data import courses, mentors, durations

""" 1 """

def short_long_courses(courses, mentors, durations):
    global minimal, maximal
    courses_list = []
    for courses, mentors, duration in zip(courses, mentors, durations):
        course_dict = {'title': courses, 'mentors': mentors, 'duration': duration}
        courses_list.append(course_dict)
    minimal = min(durations)
    maximal = max(durations)
    maxes = []
    minis = []
    for index, duration in enumerate(durations):
        if duration == maximal:
            maxes.append(index)
        elif duration == minimal:
            minis.append(index)
    courses_min = []
    courses_max = []
    for id in minis:
        courses_min.append(courses_list[id]['title'])
    for id in maxes:
        courses_max.append(courses_list[id]['title'])
    return (f'Самый короткий курс(ы): {", ".join(courses_min)} - {minimal} месяца(ев)\n'
            f'Самый длинный курс(ы): {", ".join(courses_max)} - {maximal} месяца(ев)')

# print(short_long_courses(courses, mentors, durations))

""" 2 """

def sorted_courses(courses, mentors, durations):
    courses_list = []
    for course, mentor, duration in zip(courses, mentors, durations):
        course_dict = {"title": course, "mentors": mentor, "duration": duration}
        courses_list.append(course_dict)
    durations_dict = {}
    for id, course in enumerate(courses_list):
        key = course['duration']
        durations_dict.setdefault(key, [])
        durations_dict[key].append(id)
    durations_dict = dict(sorted(durations_dict.items()))
    result_list = []
    for durat, cours in durations_dict.items():
        for id in cours:
            result = f'{courses_list[id]["title"]} - {durat} месяцев'
            result_list.append(f'{courses_list[id]["title"]} - {durat} месяцев')
    return result_list

# print(sorted_courses(courses, mentors, durations))

""" 3 """


def unique_mentors():
    all_list = []
    for m in mentors:
        all_list.extend(m)
    all_names_list = []
    for mentor in all_list:
        name = mentor.split()[0]
        all_names_list.append(name)
    unique_names = set(all_names_list)
    all_names_sorted = sorted(unique_names)
    all_names_sorted = ', '.join(all_names_sorted)
    return f'Уникальные имены преподавателей: {all_names_sorted}'

# print(unique_mentors(courses, mentors))
