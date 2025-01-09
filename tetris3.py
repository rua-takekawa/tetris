
import tkinter 
import random
from tkinter import messagebox

size = 30

app = tkinter.Tk()
app.title =("タイトル")
can = tkinter.Canvas(app, width= size*12, height = size*21,)
can.pack()

app.mainloop()

def game_loop():
    can.delete("all")
    draw_tetris()
    can.after(50, game_loop)
app = tkinter.Tk()
app.title =("タイトル")
can = tkinter.Canvas(app, width= size*12, height = size*21,)
can.pack()

game_loop()   #追加
app.mainloop()

tetroI = [0,0, 0,-1, 0,1, 0,2]
tetroJ = [-1,1, 0,-1, 0,0, 0,1]
tetroL = [0,0, 0,-1, 1,1, 0,1]
tetroO = [0,0, 1,0, 0,-1, 1,-1,]
tetroS = [-1,0, 0,-1, 1,-1, 0,0]
tetroT = [-1,0, 0,0, 1,0, 0,1]
tetroZ = [-1,-1, 0,-1, 1,0, 0,0]
tetro  = [tetroI, tetroJ, tetroL, tetroO, tetroS, tetroT, tetroZ]
color = ["red", "yellow", "lime", "green", "blue", "navy", "fuchsia", "white", "black"]
type = random.randint(0,6)

moveX = 5   # 開始位置(X座標)
moveY = 1   # 開始位置(Y座標)

def draw_tetris():
    i = 0
    while i < 4:
        x = (tetro[type] [ i * 2 ] + moveX) * size
        y = (tetro[type] [ i * 2 + 1 ] + moveY) * size
        can.create_rectangle( x, y, x+size, y+size, fill=color[type])
        i += 1

app = tk.Tk() # type: ignore
can = tk.Canvas(app, width= size*12, height = size*21, bg="#E5E5E5" ) # type: ignore
can.pack()

app.bind("<KeyPress>", keypress)   # type: ignore #追加
game_loop()

app.mainloop()

def keypress(event):
    global moveX, moveY
    if event.keysym == "Left":
        moveX -= 1
    elif event.keysym == "Right":
        moveX += 1
    elif event.keysym == "Up":
        moveY -= 1
    elif event.keysym == "Down":
        moveY += 1

def game_field():
    i = 0
    j = 0
    while i < 22:
        field_y = i * size
        while j < 12:
            field_x = j * size 
            can.create_rectangle( 
                        field_x, field_y,   #始点
                        field_x + size, field_y + size, #終点
                        width=1, fill="white",outline="#ACACAC")   #オプション
            j += 1
        i += 1
        j = 0
def game_loop():
    can.delete("all")
    game_field()   #追加
    draw_tetris()
    can.after(50, game_loop)

defence_field = [
    [8,7,7,7,7,7,7,7,7,7,7,8],
    [8,7,7,7,7,7,7,7,7,7,7,8],
    [8,7,7,7,7,7,7,7,7,7,7,8],
    [8,7,7,7,7,7,7,7,7,7,7,8],
    [8,7,7,7,7,7,7,7,7,7,7,8],
    [8,7,7,7,7,7,7,7,7,7,7,8],
    [8,7,7,7,7,7,7,7,7,7,7,8],
    [8,7,7,7,7,7,7,7,7,7,7,8],
    [8,7,7,7,7,7,7,7,7,7,7,8],
    [8,7,7,7,7,7,7,7,7,7,7,8],
    [8,7,7,7,7,7,7,7,7,7,7,8],
    [8,7,7,7,7,7,7,7,7,7,7,8],
    [8,7,7,7,7,7,7,7,7,7,7,8],
    [8,7,7,7,7,7,7,7,7,7,7,8],
    [8,7,7,7,7,7,7,7,7,7,7,8],
    [8,7,7,7,7,7,7,7,7,7,7,8],
    [8,7,7,7,7,7,7,7,7,7,7,8],
    [8,7,7,7,7,7,7,7,7,7,7,8],
    [8,7,7,7,7,7,7,7,7,7,7,8],
    [8,7,7,7,7,7,7,7,7,7,7,8],
    [8,7,7,7,7,7,7,7,7,7,7,8],
    [8,8,8,8,8,8,8,8,8,8,8,8]
]
def game_field():
    i = 0
    j = 0
    while i < 22:
        field_y = i * size
        j = 0
        while j < 12:
            field_x = j * size 
            can.create_rectangle( 
                        field_x, field_y,   #始点
                        field_x + size, field_y + size, #終点
                        width=1, fill=color[defence_field[i][j]],outline="#ACACAC")
            if defence_field[i][j] == 8:
                can.create_rectangle( 
                        field_x, field_y,   #始点
                        field_x + size, field_y + size, #終点
                        fill=color[8])   #オプション
                    
            j += 1
        i += 1

def judge(x, y):
    global moveX, moveY
    result = True
    i = 0
    while i < 4:
        j = tetro[type] [i * 2] + x
        k = tetro[type] [i * 2 + 1] + y
        if defence_field[ k ] [ j ] != 7:
            result = False
        i += 1
    if result == True:
            moveX = x
            moveY = y
    return result
def keypress(event):
    global moveX, moveY
    judge_x = moveX
    judge_y = moveY
    if event.keysym == "Left":
        judge_x -= 1
    elif event.keysym == "Right":
        judge_x += 1
    elif event.keysym == "Up":
        judge_y -= 1
    elif event.keysym == "Down":
        judge_y += 1
    judge(judge_x, judge_y)
def keypress(event):
    global moveX, moveY
    judge_x = moveX
    judge_y = moveY
    rotation = []
    rotation.extend(tetro[type])
    if event.keysym == "Left":
        judge_x -= 1
    elif event.keysym == "Right":
        judge_x += 1
    elif event.keysym == "Down":
        judge_y += 1
    elif event.keysym == "space":
        rotation.clear()
        i = 0
        while i < 4:
            rotation.append(tetro[type][i*2+1]*(-1))
            rotation.append(tetro[type][i*2])
            i += 1
    judge(judge_x, judge_y, rotation)
def judge(x, y, rotation):
    global moveX, moveY
    result = True
    i = 0
    while i < 4:
        j = rotation [i * 2] + x
        k = rotation [i * 2 + 1] + y
        if defence_field[ k ] [ j ] != 7:
            result = False
        i += 1
    if result == True:
            moveX = x
            moveY = y
            tetro[type].clear()
            tetro[type].extend(rotation)
    return result
def drop_tetris():
    global moveX, moveY, type
    rotation = []
    rotation.extend(tetro[type])
    result = judge(moveX, moveY +1, rotation)
    if result == False:
        i = 0
        while i < 4:
            x = tetro[type][i*2] + moveX
            y = tetro[type][i*2+1] + moveY
            defence_field[y][x] = type
            i += 1
        delete_line()#次で使います
        type = random.randint(0,6)
        moveX = 4
        moveY = 1
    can.after(1000, drop_tetris)

app = tkinter.Tk()
can = tkinter.Canvas(app, width= size*12, height = size*21, bg="#E5E5E5" )
can.pack()
#---処理---

app.bind("<KeyPress>", keypress)

game_loop()
drop_tetris() #追加

#----END---
app.mainloop()
def delete_line():
    i = 1
    while i < 21:
        if 7 not in defence_field[i]:
            j = 0
            while j < i:
                k = 0
                while k < 12:
                    defence_field[i-j][k] = defence_field[i-j-1][k]
                    k += 1
                j += 1
        i += 1

    i = 1  #GAMEOVER
    while i < 11:
        if 7 != defence_field[1][i]:
            messagebox.showinfo("information", "GAMEOVER")
            exit()
        i += 1
