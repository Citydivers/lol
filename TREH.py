import pygame
from colores import *

ANCHO = 300
ALTO = 300
ANCHO_RAYA = 100
TAMANO = (ANCHO, ALTO)
NOMBRE = "Tres en raya"

VENTANA = pygame.display.set_mode(TAMANO)
pygame.display.set_caption(NOMBRE)

tiempo = 0
ejecuta = True

while ejecuta == True:
    VENTANA.fill((getColor("NEGRO")))
def dibujar_tabla():
    for i in range(1,4):
        pygame.draw.line(VENTANA,color =getColor("ROJO"),width=3,start_pos=(0,i*ANCHO_RAYA),end_pos=(ANCHO,i*ANCHO_RAYA))
        pygame.draw.line(VENTANA,color =getColor("ROJO"),width=3,start_pos=(i*ANCHO_RAYA,0),end_pos=(i*ANCHO_RAYA,ANCHO))

def dibujar_x():
    pygame.draw.line(VENTANA,color =getColor("BLANCO"),width=3,start_pos=(0,0),end_pos=(100,100))
    pygame.draw.line(VENTANA,color =getColor("BLANCO"),width=3,start_pos=(0,100),end_pos=(100,0))

def dibujar_o():
    pygame.draw.circle(VENTANA,color =getColor("BLANCO"),width=3,start_pos=(0,0),end_pos=(100,100))

def posiciones_o(posicion):
    posiciones = [  [[1,2,3],
                    [4,5,6],
                    [7,8,9]],

                    [   [[50,150,250],
                        [50,150,250],
                        [50,150,250]]],


                    [   [50,50,50],
                        [150,150,150],
                        [250,250,250]]]

    for i in range (len(posiciones[0])):
        for j in range(len(posiciones[0][i])):
            if posiciones [0][i][j]== posicion:
                I = i
                J = j
                break

    x = posiciones[1][i][j]
    y = posiciones[2][i][j]
    return (x,y)

def posiciones_x():
    posiciones = {  1: ([(0,0),(100,100)],[(0,100),(100,0)]),
                    2: ([(0,100),(100,200)],[(100,100),(200,200)]),
                    3: ([(0,0),(100,100)],[(0,100),(100,0)]),
                    4: ([(0,0),(100,100)],[(0,100),(100,0)]),
                    5: ([(0,0),(100,100)],[(0,100),(100,0)]),
                    6: ([(0,0),(100,100)],[(0,100),(100,0)]),
                    7: ([(0,0),(100,100)],[(0,100),(100,0)]),
                    8: ([(0,0),(100,100)],[(0,100),(100,0)]),
                    9: ([(0,0),(100,100)],[(0,100),(100,0)])

    inicio = posiciones

    posiciones = [  [[1,2,3],
                    [4,5,6],
                    [7,8,9]],

                    [   [(0,0),(100,100),[(0,100),(200,100)],[(200,0),(300,100)]],
                        [[(0,100),(100,200)],[(100,100),(200,200)],[(200,100),(300,200)]],
                        [[(0,200),(100,300)],[(100,200),(200,300)],[(200,200),(300,300)]]],


                    [   [(0,100),(100,0),[(100,100),(200,0)],[(200,100),(300,0)]],
                        [[(0,300),(200,100)],[(100,200),(200,100)],[(200,200),(300,100)]],
                        [[(0,300),(300,200)],[(100,300),(200,200)],[(200,300),(300,200)]]]          ]



dibujar_tabla()
dibujar_x()
dibujar_o()
centro = posiciones_o(6)
print (centro)
pygame.display.update()

