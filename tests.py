from main import BooksCollector

import pytest


class TestBooksCollector:

    def test_add_one_book_without_genre_true(self):
        collector = BooksCollector()
        collector.add_new_book('Чебурашка')
        assert 'Чебурашка' in collector.books_genre and collector.books_genre['Чебурашка'] == ''

    def test_set_book_genre_true(self):
        collector_1 = BooksCollector()
        book_name = 'Блеск и нищета куртизанок'
        book_genre = 'Мультфильмы'
        collector_1.add_new_book(book_name)
        collector_1.set_book_genre(book_name, book_genre)
        assert collector_1.books_genre[book_name] != ''

    def test_get_added_book_genre_true(self):
        collector_2 = BooksCollector()
        book_name = 'Блеск и нищета куртизанок'
        book_genre = 'Мультфильмы'
        collector_2.add_new_book(book_name)
        collector_2.set_book_genre(book_name, book_genre)
        assert collector_2.get_book_genre(book_name) == book_genre

    def test_get_books_with_specific_genre_zero_added_books_true(self):
        collector_3 = BooksCollector()
        detectives = collector_3.get_books_with_specific_genre('Детективы')
        assert len(detectives) == 0

    def test_get_books_genre_one_book_and_genre_added(self):
        collector_4 = BooksCollector()
        collector_4.add_new_book('Бусинка')
        collector_4.set_book_genre('Бусинка', 'Детектив')
        assert 'Бусинка', 'Детектив' in collector_4.get_books_genre()


    def test_in_books_for_children_no_books_for_adults(self):
        collector_5 = BooksCollector()
        collector_5.add_new_book('Golf')
        collector_5.set_book_genre('Golf', 'Ужасы')
        assert len(collector_5.get_books_for_children()) == 0

    @pytest.mark.parametrize('name', ['Гений и злодейство', 'Варшава', 'Михаил Григорьевич'])
    def test_add_book_in_favorites_true(self, name):
        collector_9 = BooksCollector()
        collector_9.add_new_book(name)
        collector_9.add_book_in_favorites(name)
        assert collector_9.favorites[0] == name

    def test_delete_book_from_favorites_true(self):
        collector_7 = BooksCollector()
        collector_7.add_new_book('Доктор Живаго')
        collector_7.add_book_in_favorites('Доктор Живаго')
        collector_7.add_new_book('Доктор')
        collector_7.add_book_in_favorites('Доктор')
        collector_7.delete_book_from_favorites('Доктор')
        assert len(collector_7.favorites) == 1

    def test_get_list_of_favorites_books_true(self):
        collector_8 = BooksCollector()
        collector_8.add_new_book('Красная шапочка')
        collector_8.add_book_in_favorites('Красная шапочка')
        collector_8.add_new_book('Весна')
        collector_8.add_book_in_favorites('Весна')
        assert 'Красная шапочка', 'Весна' in collector_8.favorites
