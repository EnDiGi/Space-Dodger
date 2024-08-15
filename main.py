import pygame, sys
from player import Player
from bullet import Bullet

pygame.init()

WIDTH, HEIGHT = 1000, 800
FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))

BG = pygame.transform.scale(pygame.image.load("bg.jpeg"), (WIDTH, HEIGHT))

def draw(player, frames, bullets, score, font):
    text = font.render(f"{score}s", True, (255, 255, 255))
    text_rect = text.get_rect(topleft = (10, 10))
    
    WIN.blit(BG, (0, 0))
    WIN.blit(text, text_rect)
    pygame.draw.rect(WIN, "red", player.sprite)
    
    if frames % 6 == 0:
        bullets.append(Bullet(WIDTH))
    
    for bullet in bullets:
        pygame.draw.rect(WIN, "white", bullet.sprite)
        bullet.fall()
    
    pygame.display.update()

def end(score, font):
    new = False
    
    small_font = pygame.font.Font(None, 74)
    
    with open("best.txt", "r") as f:
        old = int(f.read())
      
    best = max(old, score)
    if best == score:
        new = True
    if old == best:
        new = False
        
    with open("best.txt", "w") as f:
        f.write(str(best))
        
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type in [pygame.FINGERDOWN, pygame.KEYDOWN]:
                return
        
        score_txt = font.render(str(score), True, (255, 255, 255))
        rect = score_txt.get_rect(center = (WIDTH // 2, HEIGHT // 2))
        
        if new:
            best_txt = small_font.render("New highscore!" , False, (255, 255, 255))
            best_rect = best_txt.get_rect(center = (WIDTH // 2, HEIGHT // 2 + 100))
        else:
            best_txt = small_font.render(f"Best: {best}" , False, (255, 255, 255))
            best_rect = best_txt.get_rect(center = (WIDTH // 2, HEIGHT // 2 + 100))
          
        WIN.blit(score_txt, rect)
        WIN.blit(best_txt, best_rect)
        
        pygame.display.update()
        pygame.time.Clock().tick(FPS)

def main():
    font = pygame.font.Font(None, 125)
    
    while True:
        score = game(font)        
        end(score, font)

def check_limit(player):
    if 0 <= player.x <= WIDTH - player.width:
        return True
    return False

def game(font):
    
    player = Player(WIDTH, HEIGHT, 80, 80)
    
    left = False
    right = False
    frames = 0
    bullets = list()
    score = -1
    
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
            draw(player, frames, bullets, score, font)
            
        if any(bullet.check_collision(player.sprite) for bullet in bullets if bullet.y >= 200):
            return score
        
        if frames % FPS == 0:
            score += 1
            
        pygame.time.Clock().tick(FPS)
        frames += 1

if __name__ == '__main__':
    main()