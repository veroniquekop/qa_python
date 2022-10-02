from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()


    def test_set_book_rating_5_positive_case(self):
        collector = BooksCollector()
        collector.set_book_rating =='5'
        assert collector.set_book_rating == 'This is correct value'

    def test_set_book_rating_12_negative_case(self):
        collector = BooksCollector()
        collector.set_book_rating =='12'
        assert collector.set_book_rating == 'This is an error'

    def test_get_book_rating_equal_name_of_book(self):
        collector = BooksCollector()
        collector.books_rating.get(self.name)
        assert collector.get_book_rating[0] == self.name[0]

    def test_get_books_with_specific_rating_is_list(self):
        collector = BooksCollector()
        collector.books_with_specific_rating = []
        assert collector.get_books_with_specific_rating(self.books_with_specific_rating) == 'This list!'

    def test_get_books_rating_is_dictionary(self):
        collector = BooksCollector()
        collector.books_rating = {}
        assert collector.get_books_rating() == 'This dictionary!'

    def test_add_book_in_favorites_list_is_not_empty(self):
        collector = BooksCollector()
        collector.add_new_book_in_favorites('Гордость и предубеждение и зомби')
        assert len(collector.add_book_in_favorites()) == 1

    def test_delete_book_from_favorites_list_is_empty(self):
        collector = BooksCollector()
        collector.favorites = []
        assert collector.delete_book_from_favorites() == 'List is empty'

    def test_get_list_of_favorites_books_is_list(self):
        collector = BooksCollector()
        collector.get_list_of_favorites_books()
        assert collector.get_list_of_favorites_books() == 'List is not empty'

