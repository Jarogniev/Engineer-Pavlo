import pygame
# import sys

from player import player1

pygame.init()

WIDTH, HEIGHT = 1200, 900
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption('Pavlo engineer')
intro = pygame.image.load('assets/engineer.jpg')            # strona 1 gry
game_window = pygame.image.load('assets/krajobraz.jpg')     # strona 2 gry
intro = pygame.transform.scale(intro, (1200, 900))
game_window = pygame.transform.scale(game_window, (1200, 900))

FPS = 60


def main():
    game_on = True
    game_side = 1
    while game_on:
        pressed = pygame.key.get_pressed()
        pygame.time.Clock().tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_on = False

        if game_side == 1:
            WIN.blit(intro, (0, 0))
        if pressed[pygame.K_SPACE]:
            game_side = 2
        if game_side == 2:
            WIN.blit(game_window, (0, 0))
            # WIN.blit(player1.gamer, (player1.gamerX, player1.gamerY))
            player1.draw_pavlo(player1.gamerX, player1.gamerY)        # odświeżanie postaci
            player1.move_pavlo(pressed)                               # ruch postaci
            pygame.time.delay(5)

        # if pressed[pygame.K_KP_ENTER]:
        #     game_on = False
        #     pygame.quit()
        #     sys.exit()

        pygame.display.update()


if __name__ == '__main__':
    main()
