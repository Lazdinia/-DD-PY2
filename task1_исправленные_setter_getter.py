class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self.__name = None
        self.__author = None
        self.__set_parametr(name,author)
    def __str__(self):
        return f"Книга {self.__name}. Автор {self.__author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.__name!r}, author={self.__author!r})"
    # def __repr__(self):
    #     #Я переопределил __rerp__ из задания чтобы его можно было наследовать
    #     f="Book"
    #     a=self.__dict__
    #     a=str(a).replace(':','=').replace('{','').replace('}','').replace("_",'').replace(f'{f}','')
    #     b=a.split(',')
    #     c=''
    #     for i,ii in enumerate(b):
    #         d=ii.replace("'",'',2)
    #         if i !=len(b)-1:
    #             c=c+d+','
    #         else:
    #             c=c+d
    #     return f"{self.__class__.__name__}({c})"

    def __set_parametr (self, name, author):
        self.__name=name
        self.__author=author
    def get_author(self):
        return self.__author
    def get_name(self):
        return self.__name

class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name,author)
        self.pages = pages
    def __repr__(self):
        #Я переопределил __rerp__ из задания чтобы его можно было наследовать
        f="Book"
        a=self.__dict__
        a=str(a).replace(':','=').replace('{','').replace('}','').replace("_",'').replace(f'{f}','')
        b=a.split(',')
        c=''
        for i,ii in enumerate(b):
            d=ii.replace("'",'',2)
            if i !=len(b)-1:
                c=c+d+','
            else:
                c=c+d
        return f"{self.__class__.__name__}({c})"
    #def __str__(self):
        #return f"Книга {self._Book__name}. Автор {self._Book__author}. Число страниц {self.pages}"

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self,new_pages):

        self._pages=new_pages


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name,author)
        self.duration = duration

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self,new_duration):
        if not isinstance(new_duration, (int, float)):
            raise TypeError("Давайте измерять duration в численом эквиваленете")
        if new_duration<0:
            raise TypeError("Продолжительность книги должна быть положительной")
        self._duration=new_duration

    def __repr__(self):
        #Я переопределил __rerp__ из задания чтобы его можно было наследовать
        f="Book"
        a=self.__dict__
        a=str(a).replace(':','=').replace('{','').replace('}','').replace("_",'').replace(f'{f}','')
        b=a.split(',')
        c=''
        for i,ii in enumerate(b):
            d=ii.replace("'",'',2)
            if i !=len(b)-1:
                c=c+d+','
            else:
                c=c+d
        return f"{self.__class__.__name__}({c})"

    #def __str__(self):
        #return f"Аудио книга {self._Book__name}. Автор {self._Book__author} . Длительность {self.duration}"

proverka=Book('sd','das')

print(proverka.__repr__())
print(proverka.__str__())
proverka= PaperBook('sd','das',2)
print(proverka.__repr__())
proverka= AudioBook('sd','das',2.43)
print(proverka.__str__())
print(proverka.__repr__())
