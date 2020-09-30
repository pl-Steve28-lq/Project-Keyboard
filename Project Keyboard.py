from pynput.keyboard import Listener, Key, GlobalHotKeys
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import tkinter.font as Font
from Utils.winoverlay import Window
import sys, os, time, base64, json, pyglet

pyglet.font.add_file('./Utils/NanumSquare_acB.ttf')

VERSION = '1.0'
WIDTH = 400
HEIGHT = 130
btnW = 50
btnH = 50
KEY = list('sdfjkl')
STATS = {i:0 for i in KEY}
isPress = {i:False for i in KEY}
cfb = '#6495ed'
dcy = '#008b8b'
BG = 'black'
transparent = '#000001'
bigFONT = Font.Font(family='나눔스퀘어_ac bold', size=20)
smallFONT = Font.Font(family='나눔스퀘어_ac bold', size=13)
title = 'PyKeyViewer {} [Steve28]'.format(VERSION)
btnplace = [10, 70, 130, WIDTH-btnW-130, WIDTH-btnW-70, WIDTH-btnW-10]


window = Window(size=(WIDTH, HEIGHT+40))
test = window.root

test.configure(bg="#000000")
screen_width = test.winfo_screenwidth()
screen_height = test.winfo_screenheight()
window.position = (0, screen_height-HEIGHT)


def exiter(event):
    isexit = messagebox.askokcancel(title, 'Quit? \n종료하시겠습니까?')
    if isexit:
        test.destroy()
        sys.exit()


def corner(event):
    W, H = screen_width, screen_height
    w, h = window.position
    isC = messagebox.askokcancel(title, 'Move Corner? \n화면 구석으로 이동하시겠습니까?')
    if isC:
        res = []
        if w < 200+WIDTH: res.append(0)
        elif W-w < 200+WIDTH: res.append(W-WIDTH)
        else: res.append(w)
        if h < 100+HEIGHT: res.append(0)
        elif H-h < 100+HEIGHT: res.append(H-HEIGHT)
        else: res.append(h)

        test.geometry('+{}+{}'.format(res[0], res[1]))


def keychange(idx, new):
    KEY[idx] = new
    STATS[new] = 0
    isPress[new] = False
    exec('btn{}.configure(text=new.upper())'.format(idx))
    exec('lbl{}.configure(text=STATS[new])'.format(idx))
    

'''
def btns(name, ind):
    print('btn{} = Button(test, text="{}", bg=BG, fg=dcy, font=bigFONT, relief="flat")'.format(name, name.upper()))
    print('btn{}.place(x=btnplace[{}], y=20, width=btnW, height=btnH)'.format(name, ind))

def lbls(name, ind):
    print('lbl{} = Label(test, text="{}", bg=BG, fg=dcy, font=bigFONT, relief="flat")'.format(name, 0))
    print('lbl{}.place(x=btnplace[{}], y=90, width=btnW, height=btnH)'.format(name, ind))
'''

btn0 = Button(test, text="S", bg=BG, fg=dcy, font=bigFONT, relief="flat")
btn1 = Button(test, text="D", bg=BG, fg=dcy, font=bigFONT, relief="flat")
btn2 = Button(test, text="F", bg=BG, fg=dcy, font=bigFONT, relief="flat")
btn3 = Button(test, text="J", bg=BG, fg=dcy, font=bigFONT, relief="flat")
btn4 = Button(test, text="K", bg=BG, fg=dcy, font=bigFONT, relief="flat")
btn5 = Button(test, text="L", bg=BG, fg=dcy, font=bigFONT, relief="flat")

btn0.place(x=btnplace[0], y=20, width=btnW, height=btnH)
btn1.place(x=btnplace[1], y=20, width=btnW, height=btnH)
btn2.place(x=btnplace[2], y=20, width=btnW, height=btnH)
btn3.place(x=btnplace[3], y=20, width=btnW, height=btnH)
btn4.place(x=btnplace[4], y=20, width=btnW, height=btnH)
btn5.place(x=btnplace[5], y=20, width=btnW, height=btnH)

lbl0 = Label(test, text="0", bg=BG, fg=dcy, font=smallFONT, relief="flat")
lbl1 = Label(test, text="0", bg=BG, fg=dcy, font=smallFONT, relief="flat")
lbl2 = Label(test, text="0", bg=BG, fg=dcy, font=smallFONT, relief="flat")
lbl3 = Label(test, text="0", bg=BG, fg=dcy, font=smallFONT, relief="flat")
lbl4 = Label(test, text="0", bg=BG, fg=dcy, font=smallFONT, relief="flat")
lbl5 = Label(test, text="0", bg=BG, fg=dcy, font=smallFONT, relief="flat")

lbl0.place(x=btnplace[0], y=80, width=btnW, height=btnH)
lbl1.place(x=btnplace[1], y=80, width=btnW, height=btnH)
lbl2.place(x=btnplace[2], y=80, width=btnW, height=btnH)
lbl3.place(x=btnplace[3], y=80, width=btnW, height=btnH)
lbl4.place(x=btnplace[4], y=80, width=btnW, height=btnH)
lbl5.place(x=btnplace[5], y=80, width=btnW, height=btnH)


def update(idx):
    exec('lbl{}.configure(text=STATS["{}"])'.format(idx, KEY[idx]))

def save(event):
    savedir = filedialog.asksaveasfilename(initialdir="/", title=title, filetypes=(('PKV files', '*.pkvstat'),('all files', '*.*')))
    newdir = savedir + '.pkvstat'
    if savedir != "":
        with open(newdir, 'x') as saving:
            saving.write(str(STATS))
        if os.path.exists(newdir):
            messagebox.showinfo(title, "Stats saved Successful. \n스탯이 성공적으로 저장되었습니다.")
        else:
            messagebox.showerror(title, "An Error occured while saving Stats. \n스탯을 저장하는 중 오류가 발생하였습니다.")

def load(event):
    global STATS
    savedir = filedialog.askopenfilename(initialdir="/", title=title, filetypes=(('PKV files', '*.pkvstat'),('all files', '*.*')))
    if os.path.exists(savedir):
        with open(savedir, 'r') as saving:
            STATS = json.loads(saving.read().replace('\'', '"'))
            for idx in range(len(KEY)):
                update(idx)
        messagebox.showinfo(title, "Stats loaded Successful. \n스탯이 성공적으로 로드되었습니다.")
    else:
        messagebox.showerror(title, "An Error occured while loading Stats. \n스탯을 불러오는 중 오류가 발생하였습니다.")

def Press( key ):
    global isPress
    try: K = key.char
    except: K = "pl-Steve28-lq"
    if K in KEY:
        W = KEY.index(K)
        exec('btn{}.configure(bg="{}", fg="{}")'.format(W, dcy, BG))
        if not isPress[K]: STATS[K] += 1
        isPress[K] = True
        update(W)


def Release( key ):
    global isPress
    try: K = key.char
    except: K = "pl-Steve28-lq"
    if K in KEY:
        W = KEY.index(K)
        exec('btn{}.configure(bg="{}", fg="{}")'.format(W, BG, dcy))
        isPress[K] = False


test.bind('<Button-3>', corner)
test.bind('<Double-Button-1>', exiter)
test.bind('<Control-c>', load)
test.bind('<Control-s>', save)


with Listener(on_press=Press, on_release=Release) as l:
    Window.launch()
    l.join()
    h.join()
