# МОЕ РЕШЕНИЕ
#
# searched_book_title: str = input()
# checked_book_title: str = input()
# checked_books_number: int = 0
#
# while checked_book_title != searched_book_title:
#
#     if checked_book_title == 'No More Books':
#         print('The book you search is not here!')
#         print(f'You checked {checked_books_number} books.')
#         break
#
#     checked_books_number += 1
#     checked_book_title = input()
#
# if checked_book_title == searched_book_title:
#     print(f'You checked {checked_books_number} books and found it.')

book_name = input()
book_count = 0
is_book_found = False
current_book = input()

while current_book != 'No More Books':
    if current_book == book_name:
        is_book_found = True
        print(f'You checked {book_count} books and found it.')
        break

    book_count += 1
    current_book = input()

if not is_book_found:
    print('The book you search is not here!')
    print(f'You checked {book_count} books.')