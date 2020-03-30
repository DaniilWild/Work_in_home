import pygame
import play

#вариант домашнего задания - дать список файлов с инструментами и попросить сделать другой набор 

# интерфейс - подсказки, кнопки управления:
play.set_backdrop('light blue')
introduce1 = play.new_text(words='Piano for fun!', x=0, y=200)
introduce2 = play.new_text(words='Create your melody by pressing the keys', x=0, y=150)

key_play_melody = play.new_box(color='light green', border_color='black', border_width=1, x=-100, y=-170, width=160, height=50)
kpm = play.new_text(words='play melody', x=-100, y=-170, font_size=20)

key_clear_melody = play.new_box(color='light yellow', border_color='black', border_width=1, x=100, y=-170, width=160, height=50)
kcm = play.new_text(words='clear melody', x=100, y=-170, font_size=20)
sound_clear_melody = pygame.mixer.Sound('C:\Users\Даниил\Desktop\clear_melody.wav')

# клавиши и звуки для них:
keys = []
sounds = []
for i in range(8):
    key_x = -180 + i * 50 # 40 - ширина клавиши, 10 - расстояние между ними
    key = play.new_box(color='white', border_color='black', border_width=3, x=key_x, y=0, width=40, height=100)
    sound = pygame.mixer.Sound(str(i+1)+'.ogg') # звуковые файлы пронумерованы!
    keys.append(key)
    sounds.append(sound)

# ---------------------заготовка------------------ (сочетания клавиш для VSC?)

# мелодия пока не записана:
melody = []

@play.when_program_starts
def start():
    pygame.mixer_music.load('hello.mp3')
    pygame.mixer_music.play()
        
@key_clear_melody.when_clicked
def clear():
    melody.clear()
    sound_clear_melody.play()

@key_play_melody.when_clicked
# играть записанную мелодию:
async def play_m():
    for i in range(len(melody)): #возможно, переименовать переменную, чтобы ребенок не путался
        await play.timer(seconds=0.5)
        sounds[melody[i]].play() # сыграть звук с номером, записанным на этом месте

@play.repeat_forever
async def play_piano():
    for i in range(len(keys)):
        if keys[i].is_clicked:
            keys[i].color = 'light grey'
            sounds[i].play()
            await play.timer(seconds=0.3)
            keys[i].color = 'white'
            melody.append(i) #запоминаем номер сыгранной клавиши

play.start_program()