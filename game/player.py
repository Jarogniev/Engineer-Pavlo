import pygame

WIDTH, HEIGHT = 1200, 900
FLOOR = 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))


class Player:


    def __init__(self):
        self.gamer = pygame.image.load('assets/mario.jpg')
        self.gamerX = 100
        self.gamerY = FLOOR
        self.gamer = pygame.transform.scale(self.gamer, (60, 105))
        self.speed = 5
        self.is_jumping = False
        self.jump_count = 0


    # odświeżanie postaci
    def draw_pavlo(self, x, y):
        WIN.blit(self.gamer, (x, y))


    def is_standing(self):
        # TODO: Tu w przyszlosci beda kolizje z podlozem
        if self.gamerY < FLOOR:
            return False
        else:
            return True

    def jump(self):
        # Skakanie
        if self.is_jumping:
            if self.jump_count < self.speed * 4:
                self.move(y=-self.speed * 3)
                self.jump_count += 1
            else:
                self.jump_count = 0
                self.is_jumping = False
        # Spadanie
        if not self.is_standing() and not self.is_jumping:
            self.move(y=self.speed * 3)


    # ruch o koordynaty
    def move(self, x=0, y=0):
        self.gamerX += x
        self.gamerY += y


    # ruch postaci
    def move_pavlo(self, pressed):
        px = 0

        if pressed[pygame.K_a]:
            # W lewo
            px = -self.speed
        if pressed[pygame.K_d]:
            # W prawo
            px = self.speed
        if pressed[pygame.K_SPACE]:
            # W gore
            if self.is_standing():
                self.is_jumping = True

        # Obliczenia horyzontalne
        self.move(x=px)
        # Obliczenia skoku
        self.jump()


player1 = Player()
