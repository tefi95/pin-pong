from pygame import *

BLACK = (0, 0, 0)
WIDTH = 700
HEIGHT = 500
FPS = 60
BACKGROUND = (54, 57, 64) #цвет фона
screen = display.set_mode((700, 500))
display.set_caption('ping-pong')
clock = time.Clock()

class GameSprite(sprite.Sprite):
    def init(self, player_image, player_x, player_y, player_speed):
        super().init()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.screen = screen


    def reset(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))

# background = transform.scale(image.load('mario.jpg'), (700, 500))

class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed

        if keys_pressed[K_RIGHT] and self.rect.x < 640:
            self.rect.x += self.speed


class Enemy(GameSprite):
    def init(self, image, player_x, player_y, speed):
        super().init(image, player_x, player_y, speed)
        self.right = True

    def update(self):
        self.rect.y += self.speed


game = True

#игровой цикл
while game:
    clock.tick(FPS)
    # screen.blit(background, ((0, 0)))

    #работа с событиями
    for e in event.get():
        # проверить закрытие окна
        if e.type == QUIT:
            game = False


    screen.fill(BACKGROUND)
    display.update()