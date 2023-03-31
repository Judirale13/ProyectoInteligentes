
from Reconocimiento_Serpiente import *
from Reconocimiento_Naranja import *
def calculate_direction(snake_position, food_position):
    # Obtener la posición de la cabeza de la serpiente y la comida
    x1, y1 = snake_position
    x2, y2 = food_position

    # Calcular la diferencia entre las posiciones
    dx, dy = x2 - x1, y2 - y1

    # Seleccionar la dirección con la mayor diferencia absoluta
    if abs(dx) > abs(dy):
        if dx > 0:
            return 'right'
        else:
            return 'left'
    else:
        if dy > 0:
            return 'down'
        else:
            return 'up'
