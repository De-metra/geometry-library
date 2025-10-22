from .circle import Circle
from .triangle import Triangle
from .base import Shape


_SHAPE_REGISTRY = {
    "circle": Circle,
    "triangle": Triangle
}

def calculate_area(shape_type: str, *args, **kwargs) -> float:
    """Вычисление площади фигуры по её названию"""

    shape_type = shape_type.lower()

    if shape_type not in _SHAPE_REGISTRY:
        raise ValueError(f"Неизвестный тип фигуры: {shape_type}")
    
    shape_class = _SHAPE_REGISTRY[shape_type]
    return shape_class.square(*args, **kwargs)

def register_shape(shape_type: str, shape: Shape):
    """
    Добавление новой фигуры в регистр
    """

    _SHAPE_REGISTRY[shape_type.lower()] = shape