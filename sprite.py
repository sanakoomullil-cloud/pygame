import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()


x, y, w, h, speed = 150, 250, 60, 60, 5

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:  x -= speed
    if keys[pygame.K_RIGHT]: x += speed
    if keys[pygame.K_UP]:    y -= speed
    if keys[pygame.K_DOWN]:  y += speed

    screen.fill((240, 240, 240)) 

    
    pygame.draw.rect(screen, (0, 128, 255), (x, y, w, h))
    pygame.draw.rect(screen, (255, 87, 34), (550, 250, 80, 80))

    pygame.display.flip()
    clock.tick(60)