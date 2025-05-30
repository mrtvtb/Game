from pygame import *
from sprite import *

win_width = 700
win_height = 500

window = display.set_mode((win_width, win_height))
display.set_caption("Maze")
background = transform.scale(image.load("Labirint/background.jpg"), (win_width, win_height))


mixer.init()
mixer.music.load('Labirint/jungles.ogg')
mixer.music.play()

Hero = Player('Labirint/hero.png', 50, 50, 5)
Cyborg = Enemy('Labirint/cyborg.png', 450, 250, 5)
Gold = GameSprite('Labirint/treasure.png', 550, 400, 0)


running = True
FPS = 60
clock = time.Clock()

while running:
    for e in event.get():
        if e.type == QUIT:
            running = False
    window.blit(background,(0, 0))

    Hero.update()
    Hero.reset(window)

    Cyborg.update()
    Cyborg.reset(window)
    
    Gold.reset(window)
    display.update()
    clock.tick(FPS)

quit()