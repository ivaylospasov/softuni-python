students_count = int(input())

grade = 0
top_students_number = 0
grades_4_to_5 = 0
grades_3_to_4 = 0
fail = 0
total_grades = 0

for student in range(1, students_count + 1):
    grade = float(input())
    if 5 <= grade <= 6:
        top_students_number += 1
        # total_grades += grade
    elif 4 <= grade < 5:
        grades_4_to_5 += 1
        # total_grades += grade
    elif 3 <= grade < 4:
        grades_3_to_4 += 1
        # total_grades += grade
    elif 2 <= grade < 3:
        fail += 1
    total_grades += grade

top_students_percentage = top_students_number / students_count * 100
between_4_and_5_percentage = grades_4_to_5 / students_count * 100
between_3_and_4_percentage = grades_3_to_4 / students_count * 100
fail_percentage = fail / students_count * 100
average_grade = total_grades / students_count

print(f'Top students: {top_students_percentage:.2f}%')
print(f'Between 4.00 and 4.99: {between_4_and_5_percentage:.2f}%')
print(f'Between 3.00 and 3.99: {between_3_and_4_percentage:.2f}%')
print(f'Fail: {fail_percentage:.2f}%')
print(f'Average: {average_grade:.2f}')