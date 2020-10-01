from pynput.keyboard import Listener, Key
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import tkinter.font as Font
from Utils.winoverlay import Window
import sys, os, time, base64, json, pyglet, base64

#Import Font
pyglet.font.add_file('./Utils/NanumSquare_acB.ttf')

#Setup Constants
VERSION = '1.0'
WIDTH = 400
HEIGHT = 170
btnW = 50
btnH = 50
KEY = list('sdfjkl')
STATS = {i:0 for i in KEY}
isPress = {i:False for i in KEY}
cfb = '#6495ed'
dcy = '#008b8b'
BG = 'black'
transparent = '#000001'
verybigFONT = Font.Font(family='나눔스퀘어_ac bold', size=40)
bigFONT = Font.Font(family='나눔스퀘어_ac bold', size=20)
smallFONT = Font.Font(family='나눔스퀘어_ac bold', size=13)
title = 'PyKeyViewer {} [Steve28]'.format(VERSION)
btnplace = [10, 70, 130, WIDTH-btnW-130, WIDTH-btnW-70, WIDTH-btnW-10]
isChoose = False
keychindex = 0

#Setup WIndows
window = Window(size=(WIDTH, HEIGHT))
test = window.root
keychoose = Window(size=(200,200))
asdf = keychoose.root
keychoose.hide()

test.configure(bg=BG)
asdf.configure(bg=BG)
screen_width = test.winfo_screenwidth()
screen_height = test.winfo_screenheight()
window.position = (0, screen_height-HEIGHT)
keychoose.position = window.position


#Exit Function
def exiter(event):
    isexit = messagebox.askokcancel(title, 'Quit? \n종료하시겠습니까?')
    if isexit:
        test.destroy()
        sys.exit()

#Corner Move Function
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

#Key Changing Function
def keychange(idx, new):
    def asdf():
        KEY[idx] = new
        STATS[new] = 0
        isPress[new] = False
        exec('btn{}.configure(text=new.upper())'.format(idx))
        exec('lbl{}.configure(text=STATS[new])'.format(idx))
    return asdf

#Key Change Cancel
def keyCancel():
    global isChoose
    keychoose.hide()
    window.show()
    isChoose = False

#Key Change OK
def keyOK():
    global keychindex
    A = keych.cget('text')
    if A=="?": messagebox.showerror(title, "Input a Key!!! \n키를 입력하세요!!!")
    elif A=="": messagebox.showerror(title, "Input a Alphabetic Key, not Special Key\n특수키가 아닌 알파벳을 입력해주세요")
    elif A.lower() in KEY: messagebox.showerror(title, "The Key is Already registered.\n그 키는 이미 등록되었습니다.")
    else:
        keychange(keychindex, A.lower())()
        keyCancel()

#Ask Key Change
def keyask(ind):
    def qwer():
        global isChoose, keychindex
        keychindex = ind
        keychoose.position = window.position
        keychoose.show()
        window.hide()
        isChoose = True
    return qwer

#Setup Key Change Window
choose = Label(asdf, text="키를 입력하세요!", font=bigFONT, bg=BG, fg=dcy)
enchoose = Label(asdf, text="Input a Key!", font=bigFONT, bg=BG, fg=dcy)
keych = Label(asdf, text="?", font=verybigFONT, bg=BG, fg=cfb)
ok = Button(asdf, text="Yes", font=bigFONT, command=keyOK)
No = Button(asdf, text="Cancel", font=smallFONT, command=keyCancel)
choose.pack()
enchoose.pack()
keych.pack()
ok.place(x=20, y=135, width=70, height=50)
No.place(x=110, y=135, width=70, height=50)

#Setup Main Window
btn0 = Button(test, text="S", bg=BG, fg=dcy, font=bigFONT, relief="flat", command=keyask(0))
btn1 = Button(test, text="D", bg=BG, fg=dcy, font=bigFONT, relief="flat", command=keyask(1))
btn2 = Button(test, text="F", bg=BG, fg=dcy, font=bigFONT, relief="flat", command=keyask(2))
btn3 = Button(test, text="J", bg=BG, fg=dcy, font=bigFONT, relief="flat", command=keyask(3))
btn4 = Button(test, text="K", bg=BG, fg=dcy, font=bigFONT, relief="flat", command=keyask(4))
btn5 = Button(test, text="L", bg=BG, fg=dcy, font=bigFONT, relief="flat", command=keyask(5))

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

total = Label(test, text="Total : {}".format(sum(STATS.values())), bg=BG, fg=dcy, font=bigFONT)

lbl0.place(x=btnplace[0], y=80, width=btnW, height=btnH)
lbl1.place(x=btnplace[1], y=80, width=btnW, height=btnH)
lbl2.place(x=btnplace[2], y=80, width=btnW, height=btnH)
lbl3.place(x=btnplace[3], y=80, width=btnW, height=btnH)
lbl4.place(x=btnplace[4], y=80, width=btnW, height=btnH)
lbl5.place(x=btnplace[5], y=80, width=btnW, height=btnH)

total.place(x=145, y=120)

#Stat Update Function
def update(idx):
    exec('lbl{}.configure(text=STATS["{}"])'.format(idx, KEY[idx]))

#Total Update Function
def updatetotal():
    d= 8
    total.configure(text="Total : {}".format(sum(STATS.values())))
    total.place(x=145+9*d-d*len(total.cget("text")))

#Stat Saving Function
def save(event):
    savedir = filedialog.asksaveasfilename(initialdir="/", title=title, filetypes=(('PKV files', '*.pkvstat'),('all files', '*.*')))
    newdir = savedir + '.pkvstat'
    if savedir != "":
        with open(newdir, 'x') as saving:
            info = ''.join(KEY) + "|" + str(STATS)
            saving.write(base64.b64encode(info.encode('utf-8')[::-1]).decode('utf-8'))
        if os.path.exists(newdir):
            messagebox.showinfo(title, "Stats saved Successful. \n정보가 성공적으로 저장되었습니다.")
        else:
            messagebox.showerror(title, "An Error occured while saving Stats. \n정보를 저장하는 중 오류가 발생하였습니다.")

#Stat Loading Function
def load(event):
    global STATS
    savedir = filedialog.askopenfilename(initialdir="/", title=title, filetypes=(('PKV files', '*.pkvstat'),('all files', '*.*')))
    if os.path.exists(savedir):
        with open(savedir, 'r') as saving:
            info = base64.b64decode(saving.read().encode('utf-8')).decode('utf-8')[::-1].split("|")
            KEY = list(info[0])
            STATS = json.loads(info[1].replace('\'', '"'))
            for idx in range(len(KEY)):
                update(idx)
            updatetotal()
        messagebox.showinfo(title, "Stats loaded Successful. \n스탯이 성공적으로 로드되었습니다.")
    else:
        messagebox.showerror(title, "An Error occured while loading Stats. \n스탯을 불러오는 중 오류가 발생하였습니다.")

#Key Hooking Function
def Press( key ):
    global isPress, isChoose
    try: K = key.char
    except: K = "pl-Steve28-lq" if not isChoose else ""
    if not isChoose and K in KEY:
        W = KEY.index(K)
        exec('btn{}.configure(bg="{}", fg="{}")'.format(W, dcy, BG))
        if not isPress[K]: STATS[K] += 1
        isPress[K] = True
        update(W)
        updatetotal()
    if isChoose:
        keych.configure(text=K.upper())

def Release( key ):
    global isPress
    try: K = key.char
    except: K = "pl-Steve28-lq"
    if K in KEY:
        W = KEY.index(K)
        exec('btn{}.configure(bg="{}", fg="{}")'.format(W, BG, dcy))
        isPress[K] = False

#Window Function Bindings
test.bind('<Button-3>', corner)
test.bind('<Double-Button-1>', exiter)
test.bind('<Control-c>', load)
test.bind('<Control-s>', save)

#Start Window, and Key Listener
with Listener(on_press=Press, on_release=Release) as l:
    Window.launch()
    l.join()
