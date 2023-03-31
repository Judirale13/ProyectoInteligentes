
from Reconocimiento_Serpiente import *
from Reconocimiento_Naranja import *

def calculate_direction(snake_position, food_position):
    # Obtener la posición de la cabeza de la serpiente y la comida
    
    x1, y1 = snake_position
    x2, y2 = food_position

    # Calcular la diferencia entre las posiciones
    dx = x2 - x1
    dy = y2 - y1

    # Si la comida está a la izquierda de la cabeza de la serpiente
    if dx < 0:
        return 'left'
    # Si la comida está a la derecha de la cabeza de la serpiente
    elif dx > 0:
        return 'right'
    # Si la comida está arriba de la cabeza de la serpiente
    elif dy < 0:
        return 'up'
    # Si la comida está abajo de la cabeza de la serpiente
    elif dy > 0:
        return 'down'
    # Si la comida está en la misma posición que la cabeza de la serpiente
    else:
        return None