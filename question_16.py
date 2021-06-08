#Usando a biblioteca Pygame, escreva um programa que desenha na tela estrelas de 5 pontas de tamanhos aleatórios 
# a cada vez que o usuário clicar na tela. A ponta superior da estrela deve estar situada onde o usuário clicou.
import pygame
from pygame.locals import *

pygame.init()
screen_with, screen_heigth = 800, 600
tela = pygame.display.set_mode((screen_with, screen_heigth))
WHITE, BLACK = (255, 255, 255), (0, 0, 0)
RED, BLUE = (255, 0, 0), (0, 0, 255)
tela.fill(BLACK)
x, y = screen_with/2, screen_heigth/2

star_points  = [ [365, 351], [400, 220], [435, 351], [571, 344], [457, 419], [506, 546], 
                [400, 460], [294, 546], [343, 419], [229, 344]]
              
class Teclas:
    def __init__(self, MOUSEBUTTONDOWN):
        self.MOUSEBUTTONDOWN = MOUSEBUTTONDOWN

def write_text(text):
    font = pygame.font.Font(None, 24)
    text = font.render(text, 1, WHITE)
    textpos = text.get_rect(centerx=tela.get_width()/2)
    tela.blit(text, textpos)
    
def draw_star():
    cor = RED
    pygame.draw.polygon( tela, RED, star_points) 
    
def move_star(x, y, star_points):
    if event.type == pygame.MOUSEBUTTONDOWN and y > 0:
        pos = pygame.mouse.get_pos()               
        y = pos[1]
        x = pos[0]
        star_points[0] = x - 35, y + 149
        star_points[1] = x, y
        star_points[2] = x + 35, y + 149        
        star_points[3] = x - -171, y - -124                
        star_points[4] = x + 57, y + 199        
        star_points[5] = x + 106, y + 326        
        star_points[6] = x, y + 240        
        star_points[7] = x - 106, y + 336        
        star_points[8] = x + -57, y + 199
        star_points[9] = x + -171, y + 124
          
    return x,y 

terminou = False
while not terminou:
    tela.fill(BLACK)    
    write_text("Question 16 - TP3")    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminou = True  
            
    x, y = move_star(x, y, star_points)                   
    draw_star() 
    pygame.display.update() 
            
pygame.display.quit()
pygame.quit()