import pygame
import random
from pygame.locals import *
from boton import Boton


pygame.init()


screen = 1000, 600
screen = pygame.display.set_mode((screen))

musica = ["musica1.mp3", "musica2.mp3", "musica3.mp3"]

pygame.mixer.music.load(random.choice(musica))
pygame.mixer.music.play(-1)


pygame.display.set_caption("Minijuegos")


# Definir Colores


FONDO = (32, 30, 32)
BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)
COLOR_TEXTO = (75, 75, 75)


# Definir Colores
hola = pygame.image.load('hola1.png')
screen.blit(hola,(0,0))



icono = pygame.image.load("hola3.png")
pygame.display.set_icon(icono)



start = True


boton1 = Boton(200, 200, 200, 100, COLOR_TEXTO, BLANCO, ROJO, 'PARCHIS')
boton2 = Boton(600, 200, 200, 100, COLOR_TEXTO, BLANCO, AZUL, 'LA OCA')


botones = [boton1, boton2]


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
           


    # Obtener la posición del mouse
    mouse_pos = pygame.mouse.get_pos()


    # Actualizar los botones
    for boton in botones:
        boton.update(mouse_pos)


    # Dibujar los botones
    for boton in botones:
        boton.draw(screen)
           
    pygame.display.update()
    pygame.mixer.music.stop()



pygame.quit()
