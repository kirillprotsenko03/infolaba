import pygame
import sys
import random
import time
from vk_functions import send_game_vk_message
from encoding import ders_crypt
from infolaba import TOKEN


WIDTH, HEIGHT = 800, 600
TITLE = "DASHA traveler"
FPS = 150
BLACK = 0, 0, 0
RED = 255, 0, 0
GREEN = 0, 255, 0
WHITE = 255, 255, 255


class Player:
    def __init__(self, screen, start_pos: tuple):
        self.screen = screen
        self.picture = pygame.image.load("picture.png")
        self.rect = self.picture.get_rect()
        self.rect.x, self.rect.y = start_pos
        self.speed = 3
        self.right_moving, self.left_moving = False, False

    def get_x(self) -> int:
        return self.rect.x

    def get_y(self) -> int:
        return self.rect.y

    def change_right_moving(self):
        self.right_moving = not self.right_moving

    def change_left_moving(self):
        self.left_moving = not self.left_moving

    def move_right(self):
        if self.right_moving:
            if self.rect.right - self.speed - 4 < WIDTH:  # 4 because of invisible picture size
                self.rect.x += self.speed

    def move_left(self):
        if self.left_moving:
            if self.rect.left + self.speed > 0:
                self.rect.x -= self.speed

    def draw(self):
        self.screen.blit(self.picture, self.rect)


class Letter:
    def __init__(self, screen, letter):
        self.screen = screen
        self.letter = letter
        self.size = 50
        self.x = random.randint(0, WIDTH - self.size)
        self.y = -self.size
        self.font = pygame.font.Font(None, 45)
        self.text = self.font.render(self.letter, True, WHITE)
        self.rect = pygame.Rect(self.x, self.y, self.size, self.size)

    def is_collision_rect(self, rect: pygame.Rect) -> bool:
        if self.rect.colliderect(rect):
            return True
        return False

    def move(self):
        self.rect.y += 1

    def draw(self):
        rect = pygame.draw.rect(self.screen, RED, self.rect)
        text_rect = self.text.get_rect(center=rect.center)
        self.screen.blit(self.text, text_rect)


class LettersManager:
    def __init__(self, screen, messenger):
        self.messenger = messenger
        self.screen = screen
        self.alphabet = [chr(char_code) for char_code in range(97, 123)]
        self.active_letters = []
        self.time = time.time()

    def add_letter(self):
        if time.time() - self.time >= 2:
            self.active_letters.append(Letter(self.screen, chr(random.randint(97, 122))))
            self.time = time.time()

    def move(self, player_rect, active_bullets):
        for letter in self.active_letters:
            letter.move()
            if letter.is_collision_rect(player_rect):
                self.active_letters.remove(letter)
            for bullet in active_bullets:
                if letter.is_collision_rect(bullet.rect):
                    self.messenger.add_letter(letter.letter)
                    active_bullets.remove(bullet)
                    self.active_letters.remove(letter)

    def draw(self):
        for letter in self.active_letters:
            letter.draw()


class Bullet:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.speed = 2
        self.rect = pygame.Rect(x + 45 // 2, y, 5, 15)

    def get_y(self):
        return self.rect.y

    def move(self):
        self.rect.y -= self.speed

    def draw(self):
        pygame.draw.rect(self.screen, GREEN, self.rect)


class BulletsManager:
    def __init__(self, screen):
        self.screen = screen
        self.active_bullet = []

    def add_bullet(self, x, y):
        self.active_bullet.append(Bullet(self.screen, x, y))

    def move(self):
        for bullet in self.active_bullet:
            bullet.move()
            if bullet.rect.y < 0:
                self.active_bullet.remove(bullet)

    def draw(self):
        for bullet in self.active_bullet:
            bullet.draw()


class Messenger:
    def __init__(self, screen):
        self.text = ""
        self.user_id = self._get_user_id()
        self.screen = screen

    def send_message(self):
        if self.text != "":
            self.text = ders_crypt(self.text)
            send_game_vk_message(self.user_id, self.text, TOKEN)
            self.text = ""

    def add_letter(self, letter: str):
        self.text += letter

    def _get_user_id(self) -> int:
        user_id = input("please, enter your vk id ")
        if user_id == "":
            user_id = 238124929  # my vk id

        return user_id

    def draw_message(self):
        font = pygame.font.Font(None, 45)
        text = font.render(self.text, False, (0, 180, 0))
        self.screen.blit(text, (10, 50))


def handle_event(player, bullets, messenger):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.change_left_moving()
            if event.key == pygame.K_RIGHT:
                player.change_right_moving()
            if event.key == pygame.K_SPACE:
                bullets.add_bullet(player.get_x(), player.get_y())
            if event.key == pygame.K_RETURN:
                messenger.send_message()
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.change_left_moving()
            if event.key == pygame.K_RIGHT:
                player.change_right_moving()


def draw_screen(screen, player, letters, bullets):
    screen.fill(BLACK)
    player.draw()
    letters.draw()
    bullets.draw()
    pygame.display.flip()


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    messenger = Messenger(screen)
    clock = pygame.time.Clock()
    pygame.display.set_caption(TITLE)
    player = Player(screen, (WIDTH // 2 - 25, HEIGHT - 50))
    manager_letters = LettersManager(screen, messenger)
    manager_bullets = BulletsManager(screen)
    while True:
        handle_event(player, manager_bullets, messenger)
        player.move_left()
        player.move_right()
        manager_letters.move(player.rect, manager_bullets.active_bullet)
        manager_letters.add_letter()
        manager_bullets.move()
        draw_screen(screen, player, manager_letters, manager_bullets)
        clock.tick(FPS)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
