from abc import ABC, abstractmethod


class Shape(ABC):
    """
    Абстрактный класс со статическим методом вычисления площади
    """
    
    @staticmethod
    @abstractmethod
    def square(*args, **kwargs) -> float:
        pass

