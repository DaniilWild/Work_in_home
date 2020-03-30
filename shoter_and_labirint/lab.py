from pygame import *
#класс-родитель для других спрайтов

class GameSprite(sprite.Sprite):
  #конструктор класса
  def __init__(self, player_image, player_x, player_y, player_speed):
      sprite.Sprite.__init__(self)
      self.image = transform.scale(image.load(player_image), (80, 80))
      self.speed = player_speed
      self.rect = self.image.get_rect()
      self.rect.x = player_x
      self.rect.y = player_y
  def reset(self):
      window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] == 1 and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] == 1 and self.rect.x < win_width - 80:
            self.rect.x += self.speed
        if keys[K_UP] == 1 and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] == 1 and self.rect.y < win_height - 80:
            self.rect.y += self.speed

class Enemy(GameSprite):
    side = "left"

    def update(self):
        if self.rect.x <= 410:
            self.side = 'right'
        if self.rect.x >= win_width - 85:
            self.side =  'left'

        if self.side == 'left':
            self.rect.x -=self.speed
        else:
            self.rect.x +=self.speed

class Wall(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, wall_x, wall_y, wall_width, wall_height):
       sprite.Sprite.__init__(self)
       self.color_1 = color_1
       self.color_2 = color_2
       self.color_3 = color_3
       self.width = wall_width
       self.height = wall_height
       self.image = Surface([self.width, self.height])
       self.image.fill((color_1, color_2, color_3))
       self.rect = self.image.get_rect()
       self.rect.x = wall_x
       self.rect.y = wall_y
    def draw_wall(self):
        draw.rect(window, (self.color_1, self.color_2, self.color_3), (self.rect.x, self.rect.y, self.width, self.height))
          

win_width = 700
win_height = 500
display.set_caption("Лабиринт")
window = display.set_mode((win_width, win_height))
packman = Player('C:\Эталонный код\hero.png', 5, win_height - 80, 5)
monster = Enemy('C:\Эталонный код\cyborg.png', win_width - 80, 200, 5)
Wall1 = Wall(200,150,10, 350 , 300 ,150,20)
Wall2 = Wall(200,150,10, 350 , 300 ,20,200)
Wall3 = Wall(200,150,10, 100 , 100 ,150,150)
#Wall4 = Wall(200,200,200, 400 , 400 ,50,50)  # Точка победы 
final_sprite = GameSprite('C:\Эталонный код\pac-1.png' , 400 , 400 ,0) 
end_game = False
run = True
while run:
    if end_game == False:
        window.fill((255, 255, 255))
        monster.reset()
        monster.update()
        packman.reset()
        packman.update()
        Wall1.draw_wall()
        Wall2.draw_wall()
        Wall3.draw_wall()
        #Wall4.draw_wall()
        final_sprite.reset()
    time.delay(50)

    for e in event.get():
        if e.type == QUIT:
            run = False

    if sprite.collide_rect(packman, monster) or sprite.collide_rect(packman, Wall1) or sprite.collide_rect(packman, Wall2) or sprite.collide_rect(packman, Wall3):
        end_game = True
        window.fill((255, 255, 255))
        img = image.load('C:\Эталонный код\game-over_1.png')
        d = img.get_width() // img.get_height()
        window.blit(transform.scale(img, (win_height * d, win_height)), (90, 0))

    if sprite.collide_rect(packman , final_sprite):
        end_game = True
        window.fill((255, 255, 255))
        img = image.load('C:\Эталонный код\thumb.jpg')
        window.blit(transform.scale(img, (win_height , win_height)), (0, 0))


    display.update()