import numpy as np
import random as rnd
import pygame
from sense_hat import SenseHat

sense = SenseHat()


pygame.init()

clock = pygame.time.Clock()
FPS = 60


R = (255, 0, 0)  # Red
W = (255, 255, 255)  # White
B = (0, 0, 255)
G = (0, 255, 0)
Y  = (255, 255, 0)
C = (0, 255, 255)
M = (255, 0, 255)
D = (0, 0, 0)


ac = [R, W, B, Y, G, C, M]

length = 1



board = np.zeros((8, 8), dtype=np.int8) # Board setup

headpos = hx, hy = 1, 1 # Starting positionss
fruitpos = fx, fy = 6, 6

board[headpos] = 1
board[fruitpos] = -1

FPS = 1


running = True
while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        
        if event.action == "pressed":
    
            
            if event.direction =="up":
                hy -= 1
            if event.direction =="down":
                hy += 1
            if event.direction =="right":
                hx -= 1
            if event.direction =="left":
                hx += 1
    
    if hx < 0 or hx > 7 or hy < 0 or hy > 7: # Check if out of Bounds
        running = False
    
    if board[hx, hy] == -1: # Check fruit pickup
        length += 1
        while True:
            fx = rnd.randint(0, 7)
            fy = rnd.randint(0, 7)
            if board[fx, fy] == 0:
                break
    
    if board[hx, hy] > 1: # Check self collision
        running = False
    
    
    for i in range(8): # Update Body
        for j in range(8):
            if board[i, j] > 0:
                board[i, j] += 1
            if board[i, j] > length:
                board[i, j] = 0
    
    
    board[hx, hy] = 1 # Update Head and fruit
    board[fx, fy] = -1
    
    for i in range(8):
        for j in range(8):
            if board[i, j] > 1:
                sense.set_pixel(i, j, W)
            else:
                sense.set_pixel(i, j, D)
       
