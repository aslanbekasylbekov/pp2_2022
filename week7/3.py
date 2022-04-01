import pygame
WIDTH = 600
HEIGHT = 500
BALL_R = 25
x = 50
y = 50 
pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
done = True
while done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x -= 20
            elif event.key == pygame.K_RIGHT:
                x += 20
            elif event.key == pygame.K_DOWN:
                y += 20
            elif event.key == pygame.K_UP:
                y -= 20
    screen.fill((0,0,0))
    screen.fill("WHITE")
    ball = pygame.draw.circle(screen,"red",(x,y),BALL_R)
    if x >= 575:
        x = 575
    if x <= 25:
        x = 25
    if y >= 475:
        y = 475
    if y <= 25:
        y = 25
    pygame.display.update()