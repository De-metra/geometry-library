import math
from .base import Shape


class Circle(Shape):

    @staticmethod
    def square(r : float) -> float:
        """
        Вычисление площади круга по радиусу
        """

        if r < 0:
            raise ValueError("Радиус должен быть положительным числом")
        return math.pi * math.pow(r, 2)
    
    