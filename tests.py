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

    def test_add_new_book_add_book_twice(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Гордость и предубеждение и зомби')
        assert len(collector.get_books_rating()) == 1
    def test_set_book_rating_5_positive_case(self):
        collector = BooksCollector()
        collector.set_book_rating = '5'
        assert collector.set_book_rating == '5'

    def test_set_book_rating_12_negative_case(self):
        collector = BooksCollector()
        collector.set_book_rating = '12'
        assert collector.set_book_rating != '5'

    def test_get_book_rating_equal_name_of_book(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_rating('Гордость и предубеждение и зомби', 4)
        assert collector.get_book_rating('Гордость и предубеждение и зомби') == 4

    def test_get_books_with_specific_rating_4_positive_case(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_rating('Гордость и предубеждение и зомби', 4)

        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.set_book_rating('Что делать, если ваш кот хочет вас убить', 5)

        # assert collector.get_books_with_specific_rating(4)[0] == 'Гордость и предубеждение и зомби'
        assert len(collector.get_books_with_specific_rating(4)) == 1

    def test_get_books_rating_is_dictionary(self):
        collector = BooksCollector()
        assert collector.get_books_rating() == {}

    def test_add_book_in_favorites_if_book_is_not_there_yet(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_rating('Гордость и предубеждение и зомби', 4)
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        assert 'Гордость и предубеждение и зомби' in collector.get_list_of_favorites_books()

    def test_delete_book_from_favorites_book_is_not_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_rating('Гордость и предубеждение и зомби', 4)
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        collector.delete_book_from_favorites('Гордость и предубеждение и зомби')
        assert 'Гордость и предубеждение и зомби' not in collector.get_list_of_favorites_books()

    def test_get_list_of_favorites_books_more_one(self):
        collector = BooksCollector()

        collector.add_new_book('Война и мир')
        collector.set_book_rating('Война и мир', 4)
        collector.add_book_in_favorites('Война и мир')

        assert len(collector.get_list_of_favorites_books()) >= 1
