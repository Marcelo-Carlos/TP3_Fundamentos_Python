#Usando a biblioteca Pygame, escreva um programa que possui uma função que desenha um círculo verde de 100 px 
# de diâmetro no centro da tela que se inicie o movimento da esquerda para a direita. 
# Sempre que chegar em alguma extremidade, o círculo deve trocar a direção e aumentar a velocidade em 1.
import pygame
from pygame.locals import *

pygame.init()
screen_width, screen_height = 800, 600
tela = pygame.display.set_mode((screen_width, screen_height))
WHITE, BLACK = (255, 255, 255), (0, 0, 0)
RED, BLUE = (255, 0, 0), (0, 0, 255)
GREEN = (0,255,0)
tela.fill(BLACK)
velocity = 1


class Teclas:
    def __init__(self, w, a, s, d):
        self.w = w
        self.a = a
        self.s = s
        self.d = d
        
x, y = screen_width/2, screen_height/2
teclas = Teclas(False, False, False, False)


def draw_blue_circle(x,y):
    cor = GREEN
    pygame.draw.circle(tela, GREEN, (x, y), 50)
        
def move_element(teclas,x,y,velocity):  
    limit = False
    
    if teclas.w and y > 0:
        y -= 2    
    elif teclas.w and y == 0:
        y = screen_width
        limit = True
    
    elif teclas.a and y < screen_height:
        y += 2
    elif teclas.a and y == screen_height:
        y = 0
        limit = True
        
    elif teclas.s and x > 0:
        x -= 2
    elif teclas.s and x == 0:
        x -= 2
        limit = True
    elif teclas.s and x < 0:
        x = screen_width
        
    elif teclas.d and x < screen_width:
        x += 2
    elif teclas.d and x == screen_width:
        x += 2
        limit = True
    elif teclas.d and x > screen_width:
        x = 0
        
    if limit == True:              
        velocity *= 2
        
    
    return x,y,velocity  

def write_text(text):
    font = pygame.font.Font(None, 24)
    text = font.render(text, 1, WHITE)
    textpos = text.get_rect(centerx=tela.get_width()/2)
    tela.blit(text, textpos)


terminou = False
while not terminou:
    tela.fill(BLACK)    
    write_text("Question 13 - TP3")    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminou = True
        #Enquanto estiver pressionado     
        if event.type == pygame.KEYDOWN:
            if event.key == K_w:
                teclas.w = True
            elif event.key == K_a:
                teclas.a = True
            if event.key == K_s:
                teclas.s = True
            if event.key == K_d:
                teclas.d = True
        #Momento que parar a tecla
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                teclas.w = False
            elif event.key == pygame.K_a:
                teclas.a = False
            elif event.key == pygame.K_s:
                teclas.s = False
            elif event.key == pygame.K_d:
                teclas.d = False        
                            
    x, y, velocity= move_element(teclas, x, y,velocity)
    draw_blue_circle(x, y)   
    pygame.display.update() 
             
pygame.display.quit()
pygame.quit()