def courses_to_take(course_to_prereqs):
    possible_courses = []
    prereqs_to_courses = {}
    number_pre_courses = {}
    number_courses = len(list(course_to_prereqs.keys()))

    # Create a dictionary where the key is the course code and the value are the courses that the key is the prerequisites.
    # Besides that a list with the courses with no prerequisites and another dictionary where the key is the course code
    # and the value is the number of prerequisites.
    for key in course_to_prereqs:
        if key not in prereqs_to_courses:
            prereqs_to_courses[key] = []
        number_pre_courses[key] = len(course_to_prereqs[key])
        if not course_to_prereqs[key]:
            possible_courses.append(key)
        else:
            for value in course_to_prereqs[key]:
                if value not in prereqs_to_courses:
                    prereqs_to_courses[value] = []
                prereqs_to_courses[value].append(key)

    allowed_courses = possible_courses
    attended = {}
    course_grade = []
    # A BFS algorithm that starts with the available courses and gets the possible new courses if the counter
    # of the new course is 0, meaning that the prerequisites were done.
    while allowed_courses:
        allowed_courses_num = len(allowed_courses)
        course_grade += allowed_courses
        avaliable_courses = []
        for i in range(allowed_courses_num):
            course = allowed_courses[i]
            if course not in attended:
                for new_course in prereqs_to_courses[course]:
                    number_pre_courses[new_course] -= 1
                    if number_pre_courses[new_course] == 0:
                        avaliable_courses.append(new_course)
                attended[course] = 1
        allowed_courses = avaliable_courses

    # A list will be returned if all courses are complet
    if len(attended.keys()) == number_courses:
        return course_grade
    else:
        return False


courses = {
  'CSC300': ['CSC100', 'CSC200'],
  'CSC200': ['CSC100'],
  'CSC100': []
}
print courses_to_take(courses)
# ['CSC100', 'CSC200', 'CSC300']
