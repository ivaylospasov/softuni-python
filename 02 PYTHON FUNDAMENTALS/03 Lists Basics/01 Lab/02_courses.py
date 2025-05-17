number_of_courses = int(input())
course_list = []

for course in range(number_of_courses):
    course_name = input()
    course_list.append(course_name)

print(course_list)