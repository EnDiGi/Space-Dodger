import pygame

class Player:
    def __init__(self, scrWidth, scrHeight, width, height):
        self.y = scrHeight - height
        self.x = scrWidth // 2 - width // 2
        self.width = width
        
        self.sprite = pygame.Rect(self.x, self.y, width, height)
    
    def move(self, go_left):
      
        if go_left:
            self.x -= 15
        else:
            self.x += 15
        
        self.sprite.x = self.x