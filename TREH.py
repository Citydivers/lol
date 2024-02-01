import pygame
from colores import *

ANCHO = 300
ALTO = 400
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

pygame.display.update()
dibujar_tabla()
dibujar_x()
dibujar_o()


