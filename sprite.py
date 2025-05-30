from pygame import *

win_width = 700
win_height = 500

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65,65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self, window):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update(self):
        key_pressed = key.get_pressed()

        if key_pressed[K_w] and self.rect.y > win_height - 65:
            self.rect.y -= self.speed

        if key_pressed[K_s] and self.rect.y < win_height - 65:
            self.rect.y += self.speed

        if key_pressed[K_a] and self.rect.x > win_width - 65:
            self.rect.x -= self.speed

        if key_pressed[K_d] and self.rect.x < win_width - 65:
            self.rect.x += self.speed


class Enemy(GameSprite):
    def update(self):
        
        if self.rect.x <= 440:
            direction = "rigth"

        if direction == "rigth":
            self.rect.x += self.speed

        if self.rect.x >= 600:
            self.direction = 'left'

        if self.direction == 'left':
            self.rect.x -= self.speed