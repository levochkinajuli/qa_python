# qa_python
==================================================== test session starts =====================================================
platform win32 -- Python 3.11.5, pytest-7.4.2, pluggy-1.3.0 -- C:\Users\Юлия\AppData\Local\Programs\Python\Python311\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\Юлия\qa_python
plugins: cov-4.1.0
collected 11 items                                                                                                            

tests.py::TestBooksCollector::test_add_new_book_add_one_book PASSED                                                     [  9%]
tests.py::TestBooksCollector::test_set_book_genre_set_one_book_genre PASSED                                             [ 18%] 
tests.py::TestBooksCollector::test_get_books_genre_one_book_added PASSED                                                [ 27%] 
tests.py::TestBooksCollector::test_get_books_with_specific_genre_zero_added_books PASSED                                [ 36%]
tests.py::TestBooksCollector::test_get_books_genre_one_book_and_genre_added PASSED                                      [ 45%] 
tests.py::TestBooksCollector::test_get_books_for_children_no_books_added PASSED                                         [ 54%] 
tests.py::TestBooksCollector::test_add_book_in_favorites_one_book_added[\u0413\u0435\u043d\u0438\u0439 \u0438 \u0437\u043b\u043e\u0434\u0435\u0439\u0441\u0442\u0432\u043e] PASSED [ 63%]
tests.py::TestBooksCollector::test_add_book_in_favorites_one_book_added[\u0412\u0430\u0440\u0448\u0430\u0432\u0430] PASSED [ 72%]
tests.py::TestBooksCollector::test_add_book_in_favorites_one_book_added[\u041c\u0438\u0445\u0430\u0438\u043b \u0413\u0440\u0438\u0433\u043e\u0440\u044c\u0435\u0432\u0438\u0447] PASSED [ 81%]
tests.py::TestBooksCollector::test_delete_book_from_favorites_one_book_deleted PASSED                                   [ 90%] 
tests.py::TestBooksCollector::test_get_list_of_favorites_books_two_books_added PASSED                                   [100%] 

===================================================== 11 passed in 0.09s ===================================================== 