name = input()
stop_command = 'Welcome!'
enrolled_students = []
VOLDEMORT_NAME = 'Voldemort'

while name != stop_command:
    if name == VOLDEMORT_NAME:
        enrolled_students.append(name)
        print('You must not speak of that name!')
        break
    elif len(name) < 5:
        print(f'{name} goes to Gryffindor.')
        enrolled_students.append(name)
    elif len(name) == 5:
        print(f'{name} goes to Slytherin.')
        enrolled_students.append(name)
    elif len(name) == 6:
        print(f'{name} goes to Ravenclaw.')
        enrolled_students.append(name)
    elif len(name) > 6:
        print(f'{name} goes to Hufflepuff.')
        enrolled_students.append(name)

    name = input()

if VOLDEMORT_NAME not in enrolled_students:
    print('Welcome to Hogwarts.')
