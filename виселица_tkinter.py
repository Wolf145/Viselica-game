# по сути это мой первый репозиторий и первая программа, написанная на tkinter
from tkinter import *
import random

root, root1 = Tk(), Tk()
root.title('Виселица')#заголовок окна программы
root1.title('Подсказка')
canvas = Canvas(root, width = 600, height = 700)#размеры окна. width - длина, height - ширина
canvas.pack()#размещение холста на экране - основного места для работы программы
canvas1 = Canvas(root1, width = 600, height = 200)

def background():#заполнение поля игры клеточкками
    y = 0
    while y < 700:
        x = 0
        while x < 600:
            canvas.create_rectangle(x, y, x + 33, y + 33, fill = 'white', outline = 'blue')
            x += 33
        y += 33

faq = '''Привет.
Это игра виселица.
Здесь надо отгадывать слова, вводя правильные буквы.

Нажми кнопку \'Начать игру\''''
canvas['bg'], canvas1['bg'] = 'white', 'white'#задний фон окна
canvas.create_text(310, 240, text = faq, fill = 'black', font = ('Helvetica', '14'))#fill - цвет текста, font - стиль и размер, text - текст, который выводится на экран

words = [ 'дикобраз', 'енот', 'медведь', 'заяц', 'лисица', 'хомяк', 'голубь', 'тушканчик', 'игуана', 'саламандра', 'ленивец', 'лягушка']
words_hint = {'дикобраз' :
'''Существо с самыми длинными
иголками среди млекопитающих''',

              'енот' :
'''Хищные млекопитающие, которые в
некоторых мультфильмах представлены, как воры''',

              'медведь' :
'''Бывают белые и бурые.
Водятся, в основном, в западной Сибири''',

              'заяц' :
'''Высоко прыгает, зимой становится белым.
Был врагом волка в \'Ну погоди!\'''',

              'лисица' :
'''Хитрая и рыжая обманщица
в русских сказках''',

              'хомяк' : 
'''Дикое животное,
запасающее еду за щеками''',

              'голубь' : 
'''Птица, обитающая
во многих городах мира''',

              'тушканчик' : 
'''Мышь с удлиненными
задними лапами''',

              'игуана' : 
'''Крупная растительноядная
ящерица''',

              'саламандра' : 
'''Земноводное,
похожее на ящерицу''',

              'ленивец' : 
'''Медленное животное,
обитающее в Африке''',

              'лягушка' : 
'''Земноводное, детенышем
которого является головастик'''}

button1 = Button(root, text = 'Начать игру', width = 10, height = 2, command = lambda: main_game())#Создание кнопки начала игры. command - то, что делает кнопка при нажатии
button1.place(x = 250, y = 620)#размещение кнопки
button1['bg'] = 'green'#задний фон кнопки

alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

canvas1.pack()

def main_game():
    canvas.delete("all")#очистка холста от всего
    canvas1.delete("all")
    
    button1['text'] = 'переиграть'#изменение текста кнопки
    background()
    
    wrd = random.choice(words)
    canvas1.create_text(300, 30, text = words_hint[wrd], fill = 'black', font = ('Helvetica', '14'))
    hddn_wrd = wrd[0] + ' _' * (len(wrd) - 2) + ' ' + wrd[len(wrd) - 1]
    hddn_wrd = hddn_wrd.split()
    hddn_wrd1 = dict()

    for i in range(len(wrd)):
        hddn_wrd1[wrd[i]] = []

    for i in range(len(wrd)):
        hddn_wrd1[wrd[i]].append(i)

    x1 = 270

    for i in hddn_wrd:#размещение первой и последней букв на холсте + скрытые буквы в виде нижнего подчеркивания
        canvas.create_text(x1, 350, text = i, fill = 'black', font = ('Helvetica', '14'))
        
        x1 += 20

    buttons = dict()

    def alf(i1):
        buttons[i1] = Button(root, text = i1, width = 6, height = 2, command = lambda: lose_or_win(i1))

    for i in alphabet:
        alf(i)

    x, y, let = 5, 400, 0
    
    for i in range(3):
        for j in range(11):
            buttons[alphabet[let]].place(x = x, y = y)
            
            let += 1
            x += 54
            
        x = 5
        y += 50

    global tries
    tries = 0

    def lose_or_win(btn):
        if btn in wrd:
            buttons[btn]['bg'] = 'green'
            
            for i in range(len(hddn_wrd1[btn])):
                hddn_wrd[hddn_wrd1[btn][i]] = btn

                x2 = 270
            
                for i in hddn_wrd:
                    canvas.create_text(x2, 350, text = i, fill = 'black', font = ('Helvetica', '14'))
                
                    x2 += 20

        if btn not in wrd:
            buttons[btn]['bg'] = 'red'

            global tries
            tries += 1
            
            if tries == 1:
                canvas.create_line(250, 310, 400, 310)#создание линии

            if tries == 2:
                canvas.create_line(250, 310, 250, 25)

            if tries == 3:
                canvas.create_line(250, 25, 325, 25)

            if tries == 4:
                canvas.create_line(325, 25, 325, 61)

            if tries == 5:
                canvas.create_oval(300, 60, 350, 110, outline="black", width=1)#создание круга координаты - крайняя правая и левая точка окружности, width - толщина линии окружности

            if tries == 6:
                canvas.create_line(325, 111, 325, 211)

            if tries == 7:
                canvas.create_line(325, 111, 295, 181)

            if tries == 8:
                canvas.create_line(325, 111, 355, 181)

            if tries == 9:
                canvas.create_line(325, 211, 295, 281)

            if tries == 10:
                canvas.create_line(325, 211, 355, 281)

        buttons[btn]['state'] = DISABLED

        if '_' not in hddn_wrd:
            canvas.create_text(280, 580, text = 'Ты отгадал слово!', fill = 'green', font = ('Helvetica', '14'))
            
            for i in buttons:
                buttons[i]['state'] = DISABLED#замораживание кнопки

        if tries == 10:
            canvas.create_text(280, 580, text = 'Ты проиграл', fill = 'red', font = ('Helvetica', '14'))
            
            for i in buttons:
                buttons[i]['state'] = DISABLED


root.mainloop()
