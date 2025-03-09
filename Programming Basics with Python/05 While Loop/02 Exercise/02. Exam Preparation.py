possible_fail_times = int(input())
current_task = input()

poor_grades = 0
is_failed = False
is_finished = False
tasks_count = 0
task_grade = 0
average_score = 0
grades_sum = 0
last_task_name = current_task

while poor_grades < possible_fail_times:

    if current_task == 'Enough':
        is_finished = True
        break

    task_grade = int(input())

    grades_sum += task_grade
    tasks_count += 1
    average_score = grades_sum / tasks_count

    if task_grade <= 4:
        poor_grades += 1
        if poor_grades >= possible_fail_times:
            is_failed = True
            break

    last_task_name = current_task
    current_task = input()

if is_failed:
    print(f'You need a break, {poor_grades} poor grades.')

if is_finished:
    print(f'Average score: {average_score:.2f}')
    print(f'Number of problems: {tasks_count}')
    print(f'Last problem: {last_task_name}')
