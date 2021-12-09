import pygame
import sys


WIDTH, HEIGHT = 800, 600
TITLE = "DASHA traveler"
BLACK = 0, 0, 0


class Player:
    def __init__(self, screen, start_pos: tuple, speed):
        self.screen = screen
        self.x, self.y = start_pos
        self.speed = speed
        self.picture = pygame.image.load("picture.png")
        self.player_rect = self.picture.get_rect()
        self.right_moving, self.left_moving = False, False

    def change_right_moving(self):
        self.right_moving = not self.right_moving

    def change_left_moving(self):
        self.left_moving = not self.left_moving

    def move_right(self):
        if self.right_moving:
            self.x += self.speed

    def move_left(self):
        if self.left_moving:
            self.x -= self.speed

    def draw(self):
        self.screen.blit(self.picture, (self.x, self.y))


def handle_event(screen, player):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.change_left_moving()
            if event.key == pygame.K_RIGHT:
                player.change_right_moving()
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.change_left_moving()
            if event.key == pygame.K_RIGHT:
                player.change_right_moving()


def draw_screen(screen, player):
    screen.fill(BLACK)
    player.draw()
    pygame.display.flip()


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption(TITLE)
    player = Player(screen, (WIDTH // 2 - 25, HEIGHT - 50), 1)
    while True:
        handle_event(screen, player)
        player.move_left()
        player.move_right()
        draw_screen(screen, player)


if __name__ == "__main__":
    main()
