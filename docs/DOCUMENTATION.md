# GEOMETRIC_LIB
В библиотеке geometric_lib представлены функции, вычисляющие площадь и периметр (или длину) основных фигур планиметрии:
- Круга (окружности)
- Прямоугольника
- Квадрата
- Треугольника

## [circle.py](../circle.py)
### area(r) - площадь круга
Принимает число r, возвращает площадь круга с радиусом r
```
import math

def area(r):
    return math.pi * r * r
```
```
>>> area(7.77)
189.6670591159112
```

### perimeter(r) - длина окружности
Принимает число r, возвращает длину окружности с радиусом r
```
import math

def perimeter(r):
    return 2 * math.pi * r
```
```
>>> perimeter(7.77)
48.82034983678538
```

## [rectangle.py](../rectangle.py)
### area(a, b) - площадь прямоугольника
Принимает 2 числа a и b, возвращает площадь прямоугольника со сторонами a и b
```
def area(a, b):
    return a * b 
```
```
>>> area(3.41, 14)
47.74
```

### perimeter(a, b) - периметр прямоугольника
Принимает 2 числа a и b, возвращает периметр прямоугольника со сторонами a и b
```
def perimeter(a, b):
    return 2 * (a + b)
```
```
>>> perimeter(3.41, 14)
34.82
```

## [square.py](../square.py)
### area(a) - площадь квадрата
Принимает число a, возвращает площадь квадрата со стороной a
```
def area(a):
    return a * a
```
```
>>> area(10)
100
```

### perimeter(a) - периметр квадрата
Принимает число a, возвращает периметр квадрата со стороной a
```
def perimeter(a):
    return 4 * a
```
```
>>> perimeter(10)
40
```

## [triangle.py](../triangle.py)
### area(a, h) - площадь треугольника
Принимает 2 числа a и h, возвращает площадь треугольника с основанием a 
и высотой h, проведённой к основанию a
```
def area(a, h):
    return a * h / 2 
```
```
>>> area(3.22, 10)
16.1
```

### perimeter(a, b, c) - периметр треугольника
Принимет 3 числа a, b и c, возвращает периметр треугольника со сторонами a, b и c
```
def perimeter(a, b, c):
    return a + b + c
```
```
>>> perimeter(3.22, 5, 6.808)
15.028
```

## История изменения проекта
```
* 238608d (HEAD -> new_features_501697) Fixed perimeter() in rectangle.py
* f638044 Added triangle.py
* 1da1ea0 Added rectangle.py
| * 86edb1c (origin/release) L-05: Update Docs. Add user agreement info
| * 438b89a L-05: Add user agreement
| * 6adb962 L-03: Docs added
| | * 3049431 (origin/feature) L-04: Add rectangle.py
| |/  
|/|   
| | * b5b0fae (origin/develop) L-04: Update docs for calculate.py
| | * d76db2a L-04: Add calculate.py
| | * 51c40eb L-04: Doc updated for triangle
| | * d080c78 L-04: Triangle added
| |/  
|/|   
* | d078c8d (origin/main, origin/HEAD, main) L-03: Docs added
|/  
* 8ba9aeb L-03: Circle and square added
```