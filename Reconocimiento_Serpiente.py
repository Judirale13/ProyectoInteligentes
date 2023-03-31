import pyautogui
import cv2
import numpy as np

# Definir las coordenadas de la ventana del navegador donde está el juego Snake
x = 415
y = 230
width = 580
height = 500

# Definir una función para encontrar la comida en la imagen del juego
def find_snake(image):
    # Convertir la imagen a formato HSV
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    
    # Definir los rangos de color para la manzana naranja
    lower_orange = np.array([0, 120, 100])
    upper_orange = np.array([20, 255, 255])
    
    # Crear una máscara que detecte los colores dentro de los límites especificados
    mask = cv2.inRange(hsv_image, lower_orange, upper_orange)
    #cv2.imshow('Game Image', mask)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()
    # Aplicar un filtro Gaussiano para reducir el ruido
    blur_image = cv2.GaussianBlur(mask, (5, 5), 0)
    
    # Detectar los bordes en la imagen usando el operador Canny
    canny_image = cv2.Canny(blur_image, 100, 200)

    # Encontrar los contornos de la máscara
    contours, _ = cv2.findContours(canny_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    # Si se detectó un contorno, devolver la posición de su centro
    if len(contours) > 0:
        largest_contour = max(contours, key=cv2.contourArea)
        moments = cv2.moments(largest_contour)
        if moments['m00'] > 0:
            cx = int(moments['m10'] / moments['m00'])
            cy = int(moments['m01'] / moments['m00'])
            return cx, cy
    
    # Si no se detectó ningún contorno, devolver None
    return None

# Tomar una captura de pantalla del área de la ventana que contiene el juego
game_image = pyautogui.screenshot(region=(x, y, width, height))
game_image = np.array(game_image)

# Encontrar la snake en la imagen
snake_position = find_snake(game_image)

# Imprimir la posición de la snake (si se detectó)
if snake_position  is not None:
    print("Posición de la snake: ", snake_position)
else:
    print("No se encontró snake en la imagen.")
