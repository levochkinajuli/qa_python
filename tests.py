from main import BooksCollector

import pytest


class TestBooksCollector:

    def test_add_new_book_add_one_book(self):
        collector = BooksCollector()
        collector.add_new_book('Чебурашка')
        assert 'Чебурашка' in collector.books_genre and collector.books_genre['Чебурашка'] == ''

    def test_set_book_genre_set_one_book_genre(self):
        collector = BooksCollector()
        book_name = 'Блеск и нищета куртизанок'
        book_genre = 'Мультфильмы'
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, book_genre)
        assert collector.books_genre[book_name] == book_genre

    def test_get_books_genre_one_book_added(self):
        collector = BooksCollector()
        book_name = 'Блеск и нищета куртизанок'
        book_genre = 'Мультфильмы'
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, book_genre)
        assert collector.get_book_genre(book_name) == book_genre

    def test_get_books_with_specific_genre_zero_added_books(self):
        collector = BooksCollector()
        assert len(collector.get_books_with_specific_genre('Детективы')) == 0

    def test_get_books_genre_one_book_and_genre_added(self):
        collector = BooksCollector()
        collector.add_new_book('Бусинка')
        collector.set_book_genre('Бусинка', 'Детектив')
        assert 'Бусинка', 'Детектив' in collector.get_books_genre()


    def test_get_books_for_children_no_books_added(self):
        collector = BooksCollector()
        collector.add_new_book('Golf')
        collector.set_book_genre('Golf', 'Ужасы')
        assert len(collector.get_books_for_children()) == 0

    @pytest.mark.parametrize('name', ['Гений и злодейство', 'Варшава', 'Михаил Григорьевич'])
    def test_add_book_in_favorites_one_book_added(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.add_book_in_favorites(name)
        assert collector.favorites[0] == name

    def test_delete_book_from_favorites_one_book_deleted(self):
        collector = BooksCollector()
        collector.add_new_book('Доктор Живаго')
        collector.add_book_in_favorites('Доктор Живаго')
        collector.add_new_book('Доктор')
        collector.add_book_in_favorites('Доктор')
        collector.delete_book_from_favorites('Доктор')
        assert len(collector.favorites) == 1

    def test_get_list_of_favorites_books_two_books_added(self):
        collector = BooksCollector()
        collector.add_new_book('Красная шапочка')
        collector.add_book_in_favorites('Красная шапочка')
        collector.add_new_book('Весна')
        collector.add_book_in_favorites('Весна')
        assert len(collector.favorites) == 2
