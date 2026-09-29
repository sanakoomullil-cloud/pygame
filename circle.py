import pygame, random
pygame.init()

# Setup screen, position, and color
W, H = 800, 600
screen = pygame.display.set_mode((W, H))
x, y, radius, speed = W // 2, H // 2, 30, 7
color = [0, 150, 255]

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:  x -= speed
    if keys[pygame.K_RIGHT]: x += speed
    if keys[pygame.K_UP]:    y -= speed
    if keys[pygame.K_DOWN]:  y += speed

    # Check wall collisions & bounce back
    hit = False
    if x - radius < 0: x, hit = radius, True
    if x + radius > W: x, hit = W - radius, True
    if y - radius < 0: y, hit = radius, True
    if y + radius > H: y, hit = H - radius, True

    # Change to a random color on impact
    if hit:
        color = [random.randint(50, 255) for _ in range(3)]

    # Draw everything
    screen.fill((30, 30, 30))
    pygame.draw.circle(screen, color, (x, y), radius)
    pygame.display.flip()
    clock.tick(60)