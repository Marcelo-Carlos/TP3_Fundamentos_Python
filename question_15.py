#Usando a biblioteca Pygame, escreva um programa que possui uma função que desenha na tela um estrela de 
# 5 pontas no tamanho que preferir. 
import pygame
from pygame.locals import *

pygame.init()
screen_with, screen_heigth = 800, 600
tela = pygame.display.set_mode((screen_with, screen_heigth))
WHITE, BLACK = (255, 255, 255), (0, 0, 0)
RED, BLUE = (255, 0, 0), (0, 0, 255)
tela.fill(BLACK)
x, y = screen_with/2, screen_heigth/2

star_points  = [ (365, 351), (400, 220), (435, 351), (571, 344), (457, 419),
                 (506, 546), (400, 460), (294, 546), (343, 419), (229, 344)]

def write_text(text):
    font = pygame.font.Font(None, 24)
    text = font.render(text, 1, WHITE)
    textpos = text.get_rect(centerx=tela.get_width()/2)
    tela.blit(text, textpos)
    
def draw_star(x,y):
    cor = RED
    pygame.draw.polygon( tela, RED, star_points) 

terminou = False
while not terminou:
    tela.fill(BLACK)    
    write_text("Question 15 - TP3")    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminou = True  
                        
    draw_star(x,y) 
    pygame.display.update() 
            
pygame.display.quit()
pygame.quit()
