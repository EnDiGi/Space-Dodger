import pygame

class Player:
    def __init__(self, scrWidth, scrHeight, width, height):
        self.y = scrHeight - height
        self.x = scrWidth // 2 - width // 2
        self.width = width
        self.scrWidth = scrWidth
        
        self.sprite = pygame.Rect(self.x, self.y, width, height)
    
    def move(self, go_left):
        if go_left:
            self.x -= 15
        elif not go_left:
            self.x += 15
        
        if self.x <= 0:
            self.x = 0
        elif self.x >= self.scrWidth - self.width:
            self.x = self.scrWidth - self.width
        
        self.sprite.x = self.x