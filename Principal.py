import pyautogui
import cv2
import numpy as np
from Reconocimiento_Serpiente import find_snake
from Reconocimiento_Naranja import find_food
from Calculo_direccion import calculate_direction
#from Movimiento import move_snake
import time
# Definir las coordenadas de la ventana del navegador donde está el juego Snake
x = 415
y = 230
width = 580
height = 500


def adjust_direction(direction, x, y, width, height):
    # Ajustar la dirección si la serpiente está cerca de los límites de la ventana
    if direction == 'up' and y < 50:
        direction = 'right'
    elif direction == 'down' and y > height - 50:
        direction = 'left'
    elif direction == 'left' and x < 50:
        direction = 'up'
    elif direction == 'right' and x > width - 50:
        direction = 'down'
    return direction

def move_snake(direction, x, y, width, height):
    print("calculando")
    # Ajustar la dirección de la serpiente si está cerca de los límites de la ventana
    direction = adjust_direction(direction, x, y, width, height)
    
    # Obtener la tecla correspondiente a la dirección
    if direction == 'up':
        key = 'up'
    elif direction == 'down':
        key = 'down'
    elif direction == 'left':
        key = 'left'
    elif direction == 'right':
        key = 'right'
    else:
        return
    # Simular la pulsación de la tecla correspondiente
    pyautogui.press(key)


while True:
# Tomar una captura de pantalla del área de la ventana que contiene el juego
    game_image = pyautogui.screenshot(region=(x, y, width, height))
    game_image = np.array(game_image)

    # Encontrar la comida en la imagen
    food_position = find_food(game_image)
    snake_position = find_snake(game_image)
    # Imprimir la posición de la comida (si se detectó)
    if food_position is not None:
        
        direction = calculate_direction(snake_position, food_position)
        #print("Posición de la comida: ", food_position)
        #print("Posición de la snake: ", snake_position)
    else:
        print("No se encontró comida en la imagen.")
    # Emitir una orden de movimiento a la serpiente para que se mueva en la dirección adecuada

    
    #direction = calculate_direction(snake_position, food_position)
    print(direction)
    # Mover la serpiente hacia la comida
    move_snake(direction, x, y, width, height)
    # Esperar un breve periodo de tiempo para que la serpiente tenga tiempo de moverse antes de repetir el proceso
    time.sleep(0.01)
  
