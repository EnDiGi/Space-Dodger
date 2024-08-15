import pygame, sys
from player import Player
from bullet import Bullet

pygame.init()

WIDTH, HEIGHT = 1000, 800

WIN = pygame.display.set_mode((WIDTH, HEIGHT))

BG = pygame.transform.scale(pygame.image.load("bg.jpeg"), (WIDTH, HEIGHT))

def draw(player, frames, bullets):
    WIN.blit(BG, (0, 0))
    pygame.draw.rect(WIN, "red", player.sprite)
    
    if frames % 10 == 0:
        bullets.append(Bullet(WIDTH))
    
    for bullet in bullets:
        pygame.draw.rect(WIN, "white", bullet.sprite)
        bullet.fall()
    
    pygame.display.update()

def end():
    return

def main():
    
    while True:
        game()
        
        end()

def check_limit(player):
    if 0 <= player.x <= WIDTH - player.width:
        return True
    return False

def game():
    
    player = Player(WIDTH, HEIGHT, 80, 80)
    
    left = False
    right = False
    frames = 0
    bullets = list()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.FINGERDOWN:
                x = event.x * WIDTH
                
                if x < WIDTH // 2:
                    player.move(True)
                    left = True
                elif x > WIDTH // 2:
                    player.move(False)
                    right = True
            elif event.type == pygame.FINGERUP:
                left = False
                right = False
            
            elif event.type == pygame.K_LEFT:
                player.move(left = True)
            elif event.type == pygame.K_RIGHT:
                player.move(left = False)
        
        if left:
            player.move(True)
        elif right:
            player.move(False)
        
        if check_limit(player):
            draw(player, frames, bullets)
        
        if any(bullet.check_collision(player.sprite) for bullet in bullets if bullet.y >= 200):
            break
            
        pygame.time.Clock().tick(60)
        frames += 1

if __name__ == '__main__':
    main()