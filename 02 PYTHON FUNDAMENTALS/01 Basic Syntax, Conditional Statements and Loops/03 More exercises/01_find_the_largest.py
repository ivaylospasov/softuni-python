number_string = input()
numbers_list = []

for letter in number_string:
    numbers_list.append(int(letter))

numbers_list.sort(reverse=True)

for i in numbers_list:
    print(i, end="")
