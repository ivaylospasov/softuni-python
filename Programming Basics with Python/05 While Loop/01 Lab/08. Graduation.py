name = input()
year_grade: float = 0
average_grade = 0
year_grades_sum = 0
total_year_grades = 0
total_fails = 0

while True:
    year_grade = float(input())

    if year_grade < 4:
        total_fails += 1
        if total_fails >= 2:
            total_year_grades += 1
            print(f'{name} has been excluded at {total_year_grades} grade')
            break
    else:
        total_year_grades += 1
        year_grades_sum += year_grade
        average_grade = year_grades_sum / total_year_grades
        print(f'{name} finishes {total_year_grades} grade')

    if total_year_grades == 12:
        print(f'{name} graduated. Average grade: {average_grade:.2f}')
        break

