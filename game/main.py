import pygame

pygame.init()

WIDTH, HEIGHT = 1200, 900
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption('Pavlo engineer')
intro = pygame.image.load('game/assets/engineer.jpg')
game_window = pygame.image.load('game/assets/krajobraz.jpg')
intro = pygame.transform.scale(intro, (1200, 900))
game_window = pygame.transform.scale(game_window, (1200, 900))

gamer = pygame.image.load('game/assets/mario.jpg')
gamerX = 100
gamerY = 600

FPS = 60

def pavlo_movement(pressed, pavlo):
    global gamerX
    if pressed[pygame.K_a]:
        gamerX -= 1
    if pressed[pygame.K_d]:
        gamerX += 1


def pavlo(x, y):
    WIN.blit(gamer, (x, y))

gamer = pygame.transform.scale(gamer, (60, 105))

game = True
a = 1


while game:
    clock = pygame.time.Clock()
    if a == 1:
        WIN.blit(intro, (0, 0))
    pressed = pygame.key.get_pressed()

    pavlo_movement(pressed, pavlo)

    if pressed[pygame.K_SPACE]:
        a = 0
        WIN.blit(game_window, (0, 0))
    if pressed[pygame.K_KP_ENTER]:
        game = False

    pygame.display.update()

    for event in pygame.event.get():
        clock.tick(FPS)
        if event.type == pygame.QUIT:
            game = False

    pavlo(gamerX, gamerY)
