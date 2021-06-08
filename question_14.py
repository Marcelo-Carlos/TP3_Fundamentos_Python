#Usando a biblioteca Pygame, escreva um programa que possui uma função que desenha um quadrado de tamanho 50 
# no centro da tela. Quando o usuário clicar em alguma área da janela, o quadrado deve se mover para a posição 
# clicada.
import pygame
from pygame.locals import *

pygame.init()
screen_with, screen_heigth = 800, 600
tela = pygame.display.set_mode((screen_with, screen_heigth))
WHITE, BLACK = (255, 255, 255), (0, 0, 0)
RED, BLUE = (255, 0, 0), (0, 0, 255)
tela.fill(BLACK)
square_width, square_height = 50, 50

x, y = screen_with/2 - square_width, screen_heigth/2 - square_height

class Teclas:
    def __init__(self, MOUSEBUTTONDOWN):
        self.MOUSEBUTTONDOWN = MOUSEBUTTONDOWN
        
def draw_square_red(x,y):
    cor = RED
    pygame.draw.rect(tela, cor, (x,y,square_width, square_height), 0)
        
def move_rect(x,y):
    if event.type == pygame.MOUSEBUTTONDOWN and y > 0:
        pos = pygame.mouse.get_pos()       
        y = pos[1]
        x = pos[0]           
    return x,y    

def write_text(text):
    font = pygame.font.Font(None, 24)
    text = font.render(text, 1, WHITE)
    textpos = text.get_rect(centerx=tela.get_width()/2)
    tela.blit(text, textpos)

terminou = False
while not terminou:
    tela.fill(BLACK)    
    write_text("Question 14 - TP3")    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminou = True  
                        
    x, y = move_rect(x, y)
    draw_square_red(x, y)
    pygame.display.update() 
            
pygame.display.quit()
pygame.quit()
