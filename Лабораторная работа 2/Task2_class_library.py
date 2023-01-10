BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]
# TODO написать класс Book
class Book():
    def __init__(self, id_, name, pages):
        self.id_=id_
        self.name=name
        self.pages=pages
    def get_id(self):
        return (self.id_)
    def __str__(self):
        return (f'Книга "{self.name}"')
    def __repr__(self) -> str:

        return (f"Book(id_={self.id_}, name='{self.name}', pages={self.pages})")



# TODO написать класс Library

class Library():
    def __init__(self, books=None):
        if books==None:
            self.books=[0]
            self.books[0]=None
        else:
            self.books=books
    def get_next_book_id(self):
        if self.books[0]==None:
            key_id_=1
        else:
            for i, ii in enumerate(self.books):
                key_id_=ii.get_id()+1
        return (key_id_)
    def get_index_by_book_id(self, keys_id):
        index=None
        for i,ii in enumerate(self.books):
            if ii.get_id()==keys_id:
                index=i

        if index==None:
            try:
                raise ValueError("Книги с запрашиваемым id не существует ")
            except ValueError as e:
                return(e)
        else:
            return(index)


if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
