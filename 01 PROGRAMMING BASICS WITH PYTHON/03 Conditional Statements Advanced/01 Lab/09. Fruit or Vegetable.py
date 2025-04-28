fruits = ['banana', 'apple', 'kiwi', 'cherry', 'lemon', 'grapes']
vegetables = ['tomato', 'cucumber', 'pepper', 'carrot']

food = input()

if food in fruits:
    print('fruit')
elif food in vegetables:
    print('vegetable')
else:
    print('unknown')

# Дълго решение
#
# food = input()
#
# if (food == 'banana' or
#     food == 'apple' or
#     food == 'kiwi' or
#     food == 'cherry' or
#     food == 'lemon' or
#     food == 'grapes'):
#     print('fruit')
# elif (food == 'tomato' or
#       food == 'cucumber' or
#       food == 'pepper' or
#       food == 'carrot'):
#     print('vegetable')
# else:
#     print('unknown')