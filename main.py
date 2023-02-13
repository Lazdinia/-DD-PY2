
import doctest


class AUTO:
    def __init__(self, Mark: str, Serial: str, numer: str):
        """
        Создание и подготовка к работе объекта "Машина"
        :param Mark: Марка машины
        :param Serial: Серийный номер
        Примеры:
        >>> CAR = AUTO("FORD", "S666-01", "GO88NO")  # инициализация экземпляра класса
        """
        if not isinstance(Mark, str):
            raise TypeError("Напишите как текс")
        self.Mark = Mark

        if not isinstance(Serial, str):
            raise TypeError("Серийный номер это текст")
        self.Serial = Serial

        self.Numer=None
        self.change_numer(numer)
        self.probeg=0

    def __str__(self)-> str:
        """
        Функция которая создает строковое предстваление класс
        :return: str
        Примеры:
        >>> CAR = AUTO("FORD", "S666-01", "GO88NO")  # инициализация экземпляра класса
        >>> CAR.__str__()
        """
        return f"Марка машины {self.Mark}, Серийный Номер {self.Serial} , Номер на авто {self.Numer}"

    def __repr__(self)->str:
        """
                Функция которая позволяет копировать предстваление класса
                :return: str
                Примеры:
                >>> CAR = AUTO("FORD", "S666-01", "GO88NO")  # инициализация экземпляра класса
                >>> CAR.__repr__()
                """
         #Я переопределил __rerp__ из задания чтобы его можно было наследовать
        a=self.__dict__
        a=str(a).replace(':','=').replace('{','').replace('}','').replace("_",'')
        b=a.split(',')
        c=''
        for i,ii in enumerate(b):
             d=ii.replace("'",'',2)
             if i !=len(b)-1:
                 c=c+d+','
             else:
                 c=c+d
        return f"{self.__class__.__name__}({c})"


    def change_numer(self, new_numer: str) -> None:
        """
            Смена номера в ГИБДД.
            :param new_numer: Ваш новый номер

            Примеры:
            >>> CAR = AUTO("FORD", "S666-01", "GO88NO")  # инициализация экземпляра класса
            >>> CAR.change_numer('S010TY')
        """
        if not isinstance(new_numer, str):
            raise TypeError("Номер на машине это текст")
        if len(new_numer) == 5:
            raise ValueError("Номер состоит из 6 символов")
        self.Numer = new_numer

    @property
    def probeg(self):
        """
                Getter Пробег машины.
                    :param probeg: Ваш пробег
                    У стандартных машин пробег не известен

                    Примеры:
                    >>> CAR = AUTO("FORD", "S666-01", "GO88NO")  # инициализация экземпляра класса
                """
        return self._probeg
    @probeg.setter
    def probeg(self, new_probeg):
        """
                        Setter Пробег машины.
                            :param new_probeg : Новый пробег
                            :param probeg: Ваш пробег
                            У стандартных машин пробег не известен

                            Примеры:
                            >>> CAR = AUTO("FORD", "S666-01", "GO88NO")  # инициализация экземпляра класса
                        """
        self._probeg=new_probeg



class AUTO_from_USA(AUTO):
    """
           Создание и подготовка к работе объекта "Машина из Америки"
           :param Mark: Марка машины
           :param Serial: Серийный номер
           :param Numer: Номер на машине из неограниченого числа символо
           Отличие от класса машины в том что номер на машине может иметь произвольную длину!
           Примеры:
           >>> CAR = AUTO_from_USA("FORD", "S666-01", "GO8NO")  # инициализация экземпляра класса
           """
    def change_numer(self, new_numer)-> None:
        """
                   Переопределение метода смены номера"
                   :return None
                   Примеры:
                   >>> CAR = AUTO_from_USA("FORD", "S666-01", "GO8NO")  # инициализация экземпляра класса
                   """
        if not isinstance(new_numer, str):
            raise TypeError("Номер на машине это текст")
        self.Numer = new_numer

class AUTO_with_probeg(AUTO):
    def __init__(self, Mark: str, Serial: str, numer: str,probeg: int, cost : int):
        """
           Создание и подготовка к работе объекта "Машина с пробегом"
           :param Mark: Марка машины
           :param Serial: Серийный номер
           :param Numer: Номер на машине из неограниченого числа символо
           :param probeg: Информация о пробеге машины
           :param cost : Цена в машине
           Отличие от класса машины в том что номер на машине может иметь параметр пробег!
           Примеры:
                    >>> CAR = AUTO_with_probeg("FORD", "S666-01", "GO88NO",10000, 200000)  # инициализация экземпляра класса
           """
        super().__init__(Mark,Serial,numer)
        self.probeg=probeg
        if not isinstance(cost, int):
            raise TypeError("Серийный номер это текст")
        self.cost=cost
    def iznos(self):
        """
                   Функция расчета износа машины
                   Примеры:
                            >>> CAR = AUTO_with_probeg("FORD", "S666-01", "GO88NO",10000, 200000)  # инициализация экземпляра класса
                            >>> CAR.iznos()
                   """
        cost=self.cost*(1/self.probeg)
        return cost
    def __str__(self):
        """
            Строковое представление перегружаю т.к. появился новый параметр
            Примеры:
                >>> CAR = AUTO_with_probeg("FORD", "S666-01", "GO88NO",10000, 200000)   # инициализация экземпляра класса
                >>> CAR.__str__()
        """
        return f"Марка машины {self.Mark}, Серийный Номер {self.Serial} , Номер на авто {self.Numer}, Количество пройденых киллометров {self.probeg}"

if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации

CAR = CAR = AUTO_with_probeg("FORD", "S666-01", "GO88NO",10000, 200000)
print(CAR.__str__())
print(CAR.__repr__())

