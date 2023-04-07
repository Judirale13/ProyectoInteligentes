import pyautogui
from PIL import Image, ImageDraw
import platform
import cv2
import numpy as np
from Reconocimiento_Serpiente import find_snake
from Reconocimiento_Naranja import find_food
from Calculo_direccion import calculate_direction, a_star,move
#from Movimiento import move_snake
import time

# Definir las coordenadas de la ventana del navegador donde está el juego Snake
x = 54
y = 420
width = 1090
height = 962


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

    # Ajustar la dirección de la serpiente si está cerca de los límites de la ventana
    #direction = adjust_direction(direction, x, y, width, height)
    
    # Simular la pulsación de la tecla correspondiente
    #pyautogui.press(direction)

cell_size = 64
def generate_graph(image_path):
    # Load the image and convert to grayscale
    image = image_path
    pixels = image.load()
    # Define the dimensions of the board and the cell size

    # Initialize the graph
    graph = {}
    # Loop through the cells and add nodes to the graph
    for x in range(cell_size // 2, width, cell_size):
        for y in range(cell_size // 2, height, cell_size-5):
           r, g, b, a = pixels[x, y]
           #print(r,g,b)
           if ((r < 215 or r > 240) and (g < 105 or g > 140) and (b<70 or b>90)):
            node = (x // cell_size, y // cell_size)
            graph[node] = {} 
                # Check the neighboring cells to find connections
            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nx, ny = x + dx * cell_size, y + dy * cell_size
                if 0 <= nx < width and 0 <= ny < height:
                    r, g, b, a = pixels[nx, ny]
                    if ((r < 215 or r > 240) and (g < 105 or g > 140) and (b<70 or b>90)):
                        neighbor = (nx // cell_size, ny // cell_size)
                        graph[node][neighbor] = 1
    #for node, neighbors in graph.items():
        #print(f"Node {node}:")
        #for neighbor, cost in neighbors.items():
        #   print(f"  -> Neighbor {neighbor} (cost {cost})")
    #g = draw_graph_on_image(graph,image_path)
    return graph

def draw_graph_on_image(graph, image_path):
    # Load the original image
    image = image_path
    # Draw the edges between nodes
    draw = ImageDraw.Draw(image)
    for x in range(0, image.width, cell_size):
        draw.line([(x, 0), (x, image.height)], fill=(0, 255, 0), width=1)
    for y in range(0, image.height, cell_size):
        draw.line([(0, y), (image.width, y)], fill=(0, 255, 0), width=1)
    
    # Save the new image with the graph drawn on it
    img = np.array(image)
    cv2.imshow('Game Image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

previous_move=""
while True:
    # Tomar una captura de pantalla del área de la ventana que contiene el juego
    game_image = pyautogui.screenshot(region=(x,y,width,height))
    graph = generate_graph(game_image)
    np_image = np.array(game_image)
    #cv2.imshow('Game Image', np_image)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()
    
    # Encontrar la comida en la imagen
    snake_position = find_snake(np_image)
    food_position = find_food(np_image)
    # Imprimir la posición de la comida (si se detectó)
    if food_position is not None:
            #direction = a_star(graph, snake_position, food_position)
                try:
                #direction = calculate_direction(direction, snake_position, food_position)
                    astar=a_star(graph,snake_position,food_position)
                #print(astar)
                    previous_move = move(previous_move, astar,snake_position)
                except:
                    continue
            #pyautogui.press(direction)
            #pyautogui.press("space")

            #print("Posición de la comida: ", food_position)
        #print("Posición de la snake: ", snake_position)
    else:
        print("No se encontró comida en la imagen.")
    # Emitir una orden de movimiento a la serpiente para que se mueva en la dirección adecuada


    #direction = calculate_direction(snake_position, food_position)
    #print(direction)
    # Mover la serpiente hacia la comida
    #actual_direction = calculate_direction(actual_direction, snake_position, food_position)
    #pyautogui.sleepv = 0.0
    # Esperar un bree periodo de tiempo para que la serpiente tenga tiempo de moverse antes de repetir el proceso
    # time.sleep(0.05)