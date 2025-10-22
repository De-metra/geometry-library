import math
import unittest
from geometry import calculate_area, register_shape
from geometry.circle import Circle
from geometry.triangle import Triangle

class TestGeometryLibrary(unittest.TestCase):
    
    def test_circle_area(self):
        """Тест вычисления площади круга"""

        self.assertAlmostEqual(Circle.square(5), math.pi * 25)
    
    def test_circle_negative_radius(self):
        """Тест вычисление площади круга с отрицательным радиусом"""

        with self.assertRaises(ValueError):
            Circle.square(-1)
    
    def test_circle_zero_radius(self):
        """Тест вычисление площади круга с нулевым радиусом"""

        self.assertEqual(Circle.square(0), 0)

    def test_triangle_area(self):
        """Тест вычисления площади треугольника"""

        self.assertAlmostEqual(Triangle.square(3, 4, 5), 6.0)
    
    def test_triangle_invalid_sides(self):
        """Тест вычисления площади треугольника с невалидными сторонами"""
        
        with self.assertRaises(ValueError):
            Triangle.square(0, 1, 3)  # Нулевая сторона
        
        with self.assertRaises(ValueError):
            Triangle.square(-1, 2, 3)  # Отрицательная сторона
    
    def test_right_triangle(self):
        """Тест проверки прямоугольного треугольника"""

        self.assertTrue(Triangle.is_rectangular(3, 4, 5))
        
        self.assertFalse(Triangle.is_rectangular(5, 5, 5))
    
    def test_register_new_shape(self):
        """Тест вычисления площади прямоугольника"""

        class Square:
            @staticmethod
            def square(a):
                return a * a

        register_shape("square", Square)
        self.assertEqual(Square.square(5), 25.0)
    
    def test_calculate_area_function(self):
        """Тест универсальной функции вычисления площади"""
        
        self.assertAlmostEqual(calculate_area("circle", 2), math.pi * 4)
        self.assertAlmostEqual(calculate_area("triangle", 3, 4, 5), 6.0)