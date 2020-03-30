import play

# интерфейс - подсказки, кнопки управления:
play.set_backdrop('light blue')
introduce1 = play.new_text(words='Piano for fun!', x=0, y=200)
introduce2 = play.new_text(words='Create your melody by pressing the keys', x=0, y=150)

# клавиши и звуки для них:
keys = []

for i in range(8):
    key_x = -180 + i * 50 # 40 - ширина клавиши, 10 - расстояние между ними
    key = play.new_box(color='white', border_color='black', border_width=3, x=key_x, y=0, width=40, height=100)
    keys.append(key)

play.start_program()