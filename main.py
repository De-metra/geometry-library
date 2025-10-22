from geometry import calculate_area, register_shape
from geometry.triangle import Triangle
from geometry.circle import Circle


def main():
    print("=== Демонстрация работы библиотеки Geometry ===\n")

    radius = 5
    circle_area = Circle.square(radius)
    print(f"Площадь круга с радиусом {radius}: {circle_area:.2f}")

    a, b, c = 3, 4, 5
    triangle_area = Triangle.square(a, b, c)
    print(f"Площадь треугольника со сторонами {a}, {b}, {c}: {triangle_area:.2f}")

    is_right = Triangle.is_rectangular(a, b, c)
    print(f"Треугольник ({a}, {b}, {c}) прямоугольный? {'Да' if is_right else 'Нет'}")

    print("\nИспользуем универсальную функцию calculate_area():")
    print("Площадь круга (r=2):", calculate_area("circle", 2))
    print("Площадь треугольника (3,4,5):", calculate_area("triangle", 3, 4, 5))

    class Square:
        @staticmethod
        def square(a):
            return a * a

    register_shape("square", Square)
    square_area = calculate_area("square", 6)
    print("\nДобавлен новый тип фигуры: квадрат")
    print(f"Площадь квадрата со стороной 6: {square_area}")

    print("\n=== Работа завершена ===")

if __name__ == "__main__":
    main()
