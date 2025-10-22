import math
from .base import Shape

class Triangle(Shape):

    @staticmethod
    def square(a: float, b: float, c: float) -> float:
        """
        Вычисление площади треугольника по трём сторонам
        """

        sides = sorted([a, b, c])
        if any(side <= 0 for side in sides):
            raise ValueError("Все стороны треугольника должны быть положительным числом")
        
        p = sum(sides) / 2
        return math.sqrt(p * (p - a) * (p - b) * (p - c))
    
    @staticmethod
    def is_rectangular(a: float, b: float, c: float) -> bool:
        """
        Проверяет является ли треугольник прямоугольным
        """

        a, b, c = sorted([a, b, c])
        return (a ** 2 + b ** 2 == c ** 2)
