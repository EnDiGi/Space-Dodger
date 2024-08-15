import pygame
from random import randint

class Bullet:
    def __init__(self, width):
        self.x = randint(0, width)
        self.y = -50
        
        self.sprite = pygame.Rect(self.x, self.y, 10, 20)
    
    def fall(self):
        self.y += 7
        self.sprite.y = self.y
       
    def check_collision(self, player):
        if player.colliderect(self.sprite):
            return True
        return False