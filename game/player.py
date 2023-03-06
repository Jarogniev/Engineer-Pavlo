import pygame

WIDTH, HEIGHT = 1200, 900
WIN = pygame.display.set_mode((WIDTH, HEIGHT))


class Player:

    def __init__(self):
        self.gamer = pygame.image.load('assets/mario.jpg')
        self.gamerX = 100
        self.gamerY = 600
        self.gamer = pygame.transform.scale(self.gamer, (60, 105))
        self.speed = 5

    # odświeżanie postaci
    def draw_pavlo(self, x, y):
        WIN.blit(self.gamer, (x, y))

    # ruch postaci
    def pavlo_movement(self, pressed, draw_pavlo):
        m = 8
        if pressed[pygame.K_a]:
            self.gamerX -= self.speed
        if pressed[pygame.K_d]:
            self.gamerX += self.speed
        if pressed[pygame.K_SPACE]:
            self.gamerY -= 15
        else:
            self.gamerY = 600


player1 = Player()
