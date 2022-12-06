# TODO Написать 3 класса с документацией и аннотацией типов
import doctest


class Gluposti:
    def __init__(self, lenivosti: float, gluposti_pomenshe: float):
        """
        Создание и подготовка к работе объекта "Стакан"
        :param lenivosti: Число Ленивостей
        :param gluposti_pomenshe: Число Глупостей_поменьше
        Примеры:
        >>> kurs_po_programirovaniu = Gluposti(1000, 100000)  # инициализация экземпляра класса
        """
        if not isinstance(lenivosti, (int, float)):
            raise TypeError("Давайте измерять ленность в численом эквиваленете")
        self.lenivosti = lenivosti

        if not isinstance(gluposti_pomenshe, (int, float)):
            raise TypeError("Даже вашим глупостям стоит вести счет")
        if gluposti_pomenshe < 0:
            raise ValueError("Не бывает положительных глупостей иначе бы счетки ушел в -1")
        self.gluposti_pomenshe = gluposti_pomenshe

    def snatie_greha(self) -> bool:
        """
        Функция которая ведет создателя класса к свещеннику и отмывает глупости
        :return: чистого
        Примеры:
        >>> kurs_po_programirovaniu = Gluposti(1000, 100000)
        >>> kurs_po_programirovaniu.snatie_greha()
        """
        self.gluposti_pomenshe=0
        self.lenivosti=0


    def add_gluposti(self, glup: float) -> None:
        """
        Добавление ващих глупостей и наоборот уменьшение.
        :param glup: Число глупостей

        Примеры:
        >>> kurs_po_programirovaniu = Gluposti(1000, 100000)
        >>> kurs_po_programirovaniu.add_gluposti(10000)
        """
        if not isinstance(glup, (int, float)):
            raise TypeError("Глупите в области рациональных чисел")

        self.gluposti_pomenshe=self.gluposti_pomenshe+glup

    def ot_vas_ushla_gena(self):
        """
        Будем считать это вашей самой крупной глупостью

        :return: Число совершенных вами в браке ошибоку
        Примеры:
        >>> kurs_po_programirovaniu = Gluposti(1000, 100000)
        >>> kurs_po_programirovaniu.ще(10000)
        """

        gluposti_vbraker=self.gluposti_pomenshe
        self.gluposti_pomenshe=0+1000000000000000
        return gluposti_vbraker



class MSI:
    def __init__(self, model , price):
        self.model=str(model)
        if not isinstance(price, (int, float)):
            raise TypeError("Давайте измерять деньги числами")
        self.price=price
        self.switch_on_off=0
    def start_MSI(self):
        if self.switch_on_off==0:
            self.switch_on_off=1
            self.price=self.price-self.price*0.0001
        else:
            print('MSi_ON USHE')
    def end_msi(self):
        if self.switch_on_off==1:
            self.switch_on_off=0

        else:
            print('MSi_OFF USHE')
    def cost_Msi(self):
        return self.price
class NVIDIA_GEFORCE_RTX_3070TI:
    def __init__(self, power , CUDA):
        if not isinstance(power, (int, float)):
            raise TypeError("Давайте измерять мощность числами")
        self.power=power
        self.CUDA=CUDA
        self.start_power=power
    def up_POWER(self,POWER_UP):
        self.power=self.power+POWER_UP
    def DAMAGE_OT_POWER_UP(self):
        return self.power - self.start_power
    def CUDA_info(self):    
        return self.CUDA
if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации

