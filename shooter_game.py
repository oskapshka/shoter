#Создай собственный Шутер!

from pygame import *
from random import randint
from time import time as timer 

win_widht = 1220 #переменная с шириной и высотой окна
win_height = 700
window = display.set_mode((win_widht, win_height))#установка размера окна 
display.set_caption("шутер гейм сигма бой 42 лол кек 1488") #названик окна
background = transform.scale(image.load("galaxy.jpg"), (win_widht, win_height))#установка бэкграунда


class GameSprite(sprite.Sprite):#create class
 #конструктор класса
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        #Вызываем конструктор класса (Sprite):
        sprite.Sprite.__init__(self)#иницилизация 

       #каждый спрайт должен хранить свойство image - изображение
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed


       #каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
 #метод, отрисовывающий героя на окне
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))#функция для вывода персаножа


#класс главного игрока

   #метод для управления спрайтом стрелками клавиатуры
class Player(GameSprite):
   #метод для управления спрайтом стрелками клавиатуры
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:#установка барьеара
            self.rect.x -= self.speed#set speed
        if keys[K_RIGHT] and self.rect.x < 1210:#установка барьера
            self.rect.x += self.speed#set speed
 #метод "выстрел" (используем место игрока, чтобы создать там пулю)
    def fire(self):#create class fire
        bullet = Bullet('bullet.png', self.rect.centerx, self.rect.top, 15, 20, 15)#create object bullet
        buba.add(bullet)#add to group of sprite


class Vrag(GameSprite):#create class vrag
    def update(self):
        global lose
        self.rect.y += self.speed
        if self.rect.y >= 699:#если высота болше или равна 699
            self.rect.y = -30#устанавливаем высоту -30
            self.rect.x = randint(20, 1200)#ставим ранодомное число для х от 20 до 1200
            lose += 1 #добавляем 1 очков скореборд 

class Bullet(GameSprite):#создаем класс bullet
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y <= -10:
            self.kill()#если объект класса bullet достигает кординаты -10 то мы его стираем
        

playerr = Player('rocket.png', 575 , 570 , 80, 100, 7) #создание игрока




lose = 0#переменная
kill = 0#переменная
asteroidG = sprite.Group()
buba = sprite.Group()#создание класса buba
bobs = sprite.Group()#добавления bob-ав в группу спрайтов
for boba in range(8):#создание bob с помощью цикла в кол-во 9 штук
    vrag = Vrag('boba.png', randint(100 , 1120), randint(-90, -40), 80, 80, randint(2, 4))
    bobs.add(vrag)



for boba in range(5):#создание bob с помощью цикла в кол-во 9 штук
    asteroid_size = randint(70, 110)
    asteroid = Vrag('asteroid.png', randint(100 , 1120), randint(-90, -40), asteroid_size , asteroid_size, randint(2, 4))
    asteroidG.add(asteroid)


mixer.init()
mixer.music.load('space.ogg')#создание фоновой музыки
mixer.music.play()
fire_sound = mixer.Sound('fire.ogg')

finish = False
run = True

font.init()#иницилизация текста
font2 = font.Font(None, 36)#установка основного ширифта

lose_text = font2.render("ты бот проиграл иди учись", 1, (255, 255, 255))

win = font2.render("я бот ты выиграл я пошел учиться", 1, (255, 255, 255))
  
num_fire = 0
rel_time = 0

while run:#зоднание игрового цикла
    for e in event.get():#создание кнопки выхода
        if e.type == QUIT:
            run = False
        elif e.type == MOUSEBUTTONUP and e.button == 1:

            
                    #проверяем, сколько выстрелов сделано и не происходит ли перезарядка
            if num_fire < 5 and rel_time == False:
                num_fire = num_fire + 1
                fire_sound.play()
                playerr.fire()
                
            if num_fire  >= 5 and rel_time == False : #если игрок сделал 5 выстрелов
                last_time = timer() #засекаем время, когда это произошло
                rel_time = True #ставим флаг перезарядки

    if finish == False:#отрисовка всех объектов 
        window.blit(background,(0, 0))
        playerr.reset()
        asteroidG.update()
        asteroidG.draw(window)
        bobs.update()
        bobs.draw(window)
        buba.update()
        buba.draw(window)
        playerr.update()
        text = font2.render("Пропущено: " + str(lose), 1, (255, 255, 255))#установка цвета и размера ширифта 
        window.blit(text, (10, 20))
        text = font2.render("уничтожено: " + str(kill), 1, (255, 255, 255))
        window.blit(text, (10, 43))

        if rel_time == True:
            now_time = timer() #считываем время

            if now_time - last_time < 3: #пока не прошло 3 секунды выводим информацию о перезарядке
                reload = font2.render('Wait, reload...', 1, (150, 0, 0))
                window.blit(reload, (260, 460))
            else:
                num_fire = 0   #обнуляем счётчик пуль
                rel_time = False #сбрасываем флаг перезарядки
        
        collides = sprite.groupcollide(bobs, buba, True, True)
        for c in collides:
            #этот цикл повторится столько раз, сколько монстров подбито
            kill = kill + 1
            vrag = Vrag('boba.png', randint(100 , 1120), randint(-90, -40), 80, 80, randint(2, 4))
            bobs.add(vrag)

        if sprite.spritecollide(playerr, asteroidG, False):
            finish = True
            window.blit(lose_text, (200, 200))

        if sprite.spritecollide(playerr, bobs, False) or lose >= 20:
            finish = True #проиграли, ставим фон и больше не управляем спрайтами.
            window.blit(lose_text, (200, 200))


       #проверка выигрыша: сколько очков набрали?
        if kill >= 20:
            finish = True
            window.blit(win, (200, 200))
        

    display.update()
    