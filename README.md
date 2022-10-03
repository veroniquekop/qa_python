# qa_python
def test_add_new_book_add_book_twice(self):
1.Добавляем книгу дважды
def test_set_book_rating_5_positive_case(self):
2.Устанавливаем допустимый рейтинг (позитивный кейс) 

def test_set_book_rating_12_negative_case(self):
3.Устанавливаем недопустимый рейтинг (негативный кейс) 

def test_get_book_rating_equal_name_of_book(self):
4.Проверяем, что рейтинг книги можно получить по её названию

def test_get_books_with_specific_rating_4_positive_case(self):
5.Проверяем, что книги с определенным рейтингом хранятся в списке

def test_get_books_rating_is_dictionary(self):
6.Проверяем, что books_rating - это словарь

def test_add_book_in_favorites_if_book_is_not_there_yet(self):
7.Проверяем, что книга из словаря ещё не была добавлена в список "Избранное"

def test_delete_book_from_favorites_book_is_not_favorites(self):
8.Проверяем, что после удаления книги её нет в списке "Избранное"

def test_get_list_of_favorites_books_is_list(self):
9.Проверяем, что в списки Избранное есть книги

