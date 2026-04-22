import pytest

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
        # словарь books_rating, который нам возвращает метод get_books_genre, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    
    # Тест 1 Добавление новой книги с пустым значением:
    def test_add_new_book_empty_name_not_added(self):
        collector = BooksCollector()
        name = ''
        collector.add_new_book(name)
        assert name not in collector.get_books_genre()

    # Тест 2 Добавление новой книги с названием больше лимита (41 символ):
    def test_add_new_book_too_long_name_not_added(self):
        collector = BooksCollector()
        name = 'a' * 41
        collector.add_new_book(name)
        assert name not in collector.get_books_genre()
    
    # Тест 1.2. Добавление двух одинаковых книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()
        collector.add_new_book('Левша')
        collector.add_new_book('Левша')
        assert len(collector.get_books_genre()) == 1

    # Тест 3: установка жанра книге ( 3 валидных значения)
    @pytest.mark.parametrize(
        'book_name, genre',
        [
            ["Гордость и предубеждение и зомби", "Фантастика"],
            ['Что делать, если ваш кот хочет вас убить', 'Детективы'],
            ['Леди и бродяга', 'Мультфильмы']
        ]
    )
    def test_set_book_genre(self, book_name, genre):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        assert collector.get_book_genre(book_name) == genre

    # Тест 4: Установка невалидного жанра книге
    def test_set_book_genre_invalid_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Книга')
        collector.set_book_genre('Книга', 'Роман')
        assert collector.books_genre['Книга'] == ''

    # Тест 5: Установка жанра несуществующей книге
    def test_set_book_genre_book_not_exist(self):
        collector = BooksCollector()
        collector.set_book_genre('Нет книги', 'Фантастика')
        assert collector.get_book_genre('Нет книги') is None


    # Тест 6: Получение жанра книги по имени
    def test_get_book_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Книга')
        collector.set_book_genre('Книга', 'Комедии')
        assert collector.get_book_genre('Книга') == 'Комедии'

    # Тест 7: Получение None при запросе жанра по имени книги
    def test_get_book_genre_non_existing_book(self):
        collector = BooksCollector()
        assert collector.get_book_genre('Нет книги') is None

    # Тест 8: Выводим список книг с определённым жанром
    def test_get_books_with_specific_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Книга1')
        collector.add_new_book('Книга2')
        collector.set_book_genre('Книга1', 'Фантастика')
        collector.set_book_genre('Книга2', 'Ужасы')
        result = collector.get_books_with_specific_genre('Фантастика')
        assert result == ['Книга1']

    # Тест 9: Выводим пустой список книг с определённым жанром
    def test_get_books_with_specific_genre_empty(self):
        collector = BooksCollector()
        assert collector.get_books_with_specific_genre('Фантастика') == []

    # Тест 10: Выводим пустой список книг с невалидными значениями жанра.
    @pytest.mark.parametrize('genre', ['Неизвестный', ''])
    def test_get_books_with_specific_genre_invalid_genre(self, genre):
        collector = BooksCollector()
        assert collector.get_books_with_specific_genre(genre) == []

    # Тест 11: Проверка типа books_genre возращает словарь
    def test_get_books_genre(self):
        collector = BooksCollector()
        assert isinstance(collector.get_books_genre(), dict)

    # Тест 12: Добавляем валидные значения и получаем словарь.
    def test_get_books_genre_after_adding_and_setting_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Сияние')
        collector.set_book_genre('Сияние', 'Ужасы')
        assert collector.get_books_genre() == {'Сияние': 'Ужасы'}

    # Тест 13: Возвращаем книги, подходящие детям
    def test_get_books_for_children_filters_age_rating(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер')
        collector.add_new_book('Сияние')
        collector.set_book_genre('Гарри Поттер', 'Фантастика')
        collector.set_book_genre('Сияние', 'Ужасы')
        assert collector.get_books_for_children() == ['Гарри Поттер']

    # Тест 14: Возвращаем пустой список книг, подходящих детям.
    def test_get_books_for_children_empty(self):
        collector = BooksCollector()
        collector.add_new_book('Книга1')
        collector.add_new_book('Книга2')
        collector.set_book_genre('Книга1', 'Детективы')
        collector.set_book_genre('Книга2', 'Ужасы')
        assert collector.get_books_for_children() == []
        
    # Тест 15: Тест на добавляние книги в Избранное.
    def test_add_book_in_favorites_valid(self):
        collector = BooksCollector()
        collector.add_new_book('Шерлок Хомс')
        collector.add_book_in_favorites('Шерлок Хомс')
        assert 'Шерлок Хомс' in collector.get_list_of_favorites_books()

    # Тест 16: Тест на добавляние дубликата книги в Избранное.
    def test_add_book_in_favorites_duplicate_not_added(self):
        collector = BooksCollector()
        collector.add_new_book('Шерлок Хомс')
        collector.add_book_in_favorites('Шерлок Хомс')
        collector.add_book_in_favorites('Шерлок Хомс')
        assert len(collector.get_list_of_favorites_books()) == 1

    # Тест 17: Тест на добавляние несуществующей книги в Избранное.
    def test_add_book_in_favorites_non_existing_book(self):
        collector = BooksCollector()
        collector.add_book_in_favorites('Несуществует')
        assert collector.get_list_of_favorites_books() == []

    # Тест 18: Тест на удаление книги из избранного.
    def test_delete_book_from_favorites_removes_book(self):
        collector = BooksCollector()
        collector.add_new_book('Книга')
        collector.add_book_in_favorites('Книга')
        collector.delete_book_from_favorites('Книга')
        assert collector.get_list_of_favorites_books() == []

    # Тест 19: Тест на удаление несуществующей книги из избранного.
    def test_delete_book_from_favorites_non_existing(self):
        collector = BooksCollector()
        collector.delete_book_from_favorites('Несуществует')
        assert collector.get_list_of_favorites_books() == []

    # Тест 20: Проверка, что программа возвращает СПИСОК Избранных книг
    def test_get_list_of_favorites_books_returns_list(self):
        collector = BooksCollector()
        assert isinstance(collector.get_list_of_favorites_books(), list)

    # Тест 20: Тест на получение списка Избранных книг
    def test_get_list_of_favorites_books_with_data(self):
        collector = BooksCollector()
        collector.add_new_book('Маугли')
        collector.add_book_in_favorites('Маугли')
        assert collector.get_list_of_favorites_books() == ['Маугли']



