from pygame import *
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65,65))
        self.x = player_x
        self.y = player_y
        self.speed = player_speed
        self.rect = self.image.get_rect()
    def reset(self, window):
        window.blit(self.image, (self.x, self.y))