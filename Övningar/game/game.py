from tkinter import ttk
from tkinter import *
from PIL import ImageTk
from functools import partial
import math
import random

themes = ["#ffffff", "#008033", "#00451b", "#f0e400", "#1a1a1a", "#ffffff"]
themes2 = ["#003545", "#002910", "#00210d", "#4f4b00", "#dedede", "#300010"]
themes3 = ["#009ac9", "#c7c000", "#593000", "#cf00a9", "#4f4c7d", "#4d0019"]
theme = themes[0]
theme2 = themes2[0]
theme3 = themes3[0]
shop_lst = [[["Jesse", 1, 50, 3, None, None, None, None], ["Badger", 3, 150, 5, None, None, None, None], ["S Pete", 5, 300, 15, None, None, None, None], ["Walt Jr", 10, 1000, 50, None, None, None, None], ["H berg", 15, 1500, 75, None, None, None, None], ["Gus F", 30, 3000, 90, None, None, None, None]], [["Rocket", 500, 30000, 3, None, None, None, None], ["Moon", 550, 40000, 5, None, None, None, None], ["Meth TP", 650, 80000, 15, None, None, None, None], ["Planet", 800, 100000, 50, None, None, None, None]], [], []]
#upgrades_lst = []

root = Tk()
root.geometry("1000x562")
root.title("Crystal Clicker")
root.rowconfigure(0,weight=1)
root.columnconfigure(0,weight=1)
root.config(bg="black")

canvas = Canvas(root, bg=theme, bd=0,  borderwidth=0, highlightthickness=0)
text_image_1 = PhotoImage(file = "game/crystal_clicker.png") 
text_image_2 = PhotoImage(file = "game/its_time_to_cook.png") 
IMAGE_2 = canvas.create_image(1000/2, 562/10, image=text_image_1, anchor="center")
IMAGE_3 = canvas.create_image(1000/2, 562/5, image=text_image_2, anchor="center")
canvas.grid(column=0, row=0, sticky=N+S+E+W) 

last_width = 1000
last_height = 562
meth = 0
xp = 0
level = 0
maximum = 100
meth_p_c = 1
cpc_perc = 100
label_lst = []
button_lst = []
auto_clicks = 0
time_to_click = 60000
xp_perc = 100

pstyle = ttk.Style()
pstyle.theme_use("clam")
pstyle.configure("design.Horizontal.TProgressbar",
                background=theme3,
                troughcolor=theme,
                bordercolor=theme3,
                lightcolor=theme3,
                darkcolor=theme3)
progress = IntVar()
progressbar = ttk.Progressbar(style="design.Horizontal.TProgressbar",variable=progress, orient=HORIZONTAL, length=160)
progressbar.place(relx = 0.5, rely = 0.89, anchor="n")

class create_label:
    def __init__(self, text="", relx=0, rely=0, anchor="nw", image=None, font=("System", "7")):
        self.color = theme
        self.color2 = theme2
        self.relx = relx
        self.rely = rely
        self.anchor = anchor
        self.image = image
        self.text = text
        self.font = font

        if image is not None:
            label = Label(root, image=image, bg=self.color)
        else:
            label = Label(root, text=text, font=font, bg=self.color, fg=self.color2)

        label.place(relx=relx, rely=rely, anchor=anchor)
        label_lst.append(self)
        self.label = label

class create_button(create_label):
    def __init__(self, text="", relx=0, rely=0, anchor="nw", image=None, font=("System", "7"), cost=0, qty=0, ulevel=0, inc_factor=1.1, button_type = 0, production_inc = None, total_prodction = None, command = None):
        super().__init__(text="", relx=0, rely=0, anchor="nw", image=None, font=("System", "7"))
        self.activebackground = theme
        self.cost = cost
        self.qty = qty
        self.ulevel = ulevel
        self.inc_factor = inc_factor
        self.button_type = button_type
        self.production_inc = production_inc
        self.total_prodction = total_prodction
        self.color = theme
        self.color2 = theme2

        if command is None:
            if image is not None:
                button = Button(root, image = image, command=self.clicked_button, activebackground=self.activebackground, borderwidth=0, bg=theme, fg=theme2)
            else:
                button = Button(root, text=text, font=font, command=self.clicked_button, bg=theme, fg=theme2, activebackground=self.activebackground, borderwidth=0)
        else:
            if image is not None:
                button = Button(root, image = image, command=command, activebackground=self.activebackground, borderwidth=0, bg=theme, fg=theme2)
            else:
                button = Button(root, text=text, font=font, command=command, bg=theme, fg=theme2, activebackground=self.activebackground, borderwidth=0)

        button.place(relx=relx, rely=rely, anchor=anchor)
        self.button = button
        button_lst.append(self)

    def clicked_button(self):
        global meth_p_c, meth, cpc_perc, time_to_click, xp_perc, xp
        if self.button_type == 0:
            if meth >= self.cost:
                meth_p_c += self.production_inc
                meth -= self.cost
                self.cost = math.ceil(self.cost*self.inc_factor)
                self.qty += 1
        elif self.button_type is None:
            xp += math.ceil(5 * xp_perc/100)
            meth += math.ceil(meth_p_c * cpc_perc/100)
        else:
            if meth >= self.cost:
                if self.button_type == 1:
                    cpc_perc += self.production_inc
                if self.button_type == 2:
                    if self.qty == 0:
                        auto_click()
                    else:
                        time_to_click = math.ceil(60000/self.qty)
                if self.button_type == 3:
                    xp_perc += self.production_inc
                meth -= self.cost
                self.cost = math.ceil(self.cost * self.inc_factor)
                self.qty += 1
        game_update()

def resize(event):
    global last_width, last_height
    canvas.move(IMAGE_2, (event.width-last_width)/2, (event.height-last_height)/2)
    canvas.move(IMAGE_3, (event.width-last_width)/2, (event.height-last_height)/2)
    last_height = event.height
    last_width = event.width

canvas.bind("<Configure>", resize)

def gamestage_update(game_stage):
    global walter_img, canvas, theme, theme2, theme3
    walter_talk_destroy()
    theme = themes[game_stage]
    theme2 = themes2[game_stage]
    theme3 = themes3[game_stage]
    walter_img = PhotoImage(file=f"C:/Users/Elev/Documents/Programmering 2/Prog2-HjalmarAlbinsson/Övningar/game/bulk-image-crop (3)/walter{str(game_stage+1)}-removebg-preview.png")
    walter_label.label.config(image=walter_img)
    canvas.config(bg=theme)
    pstyle.configure("design.Horizontal.TProgressbar",
                background=theme3,
                troughcolor=theme,
                bordercolor=theme3,
                lightcolor=theme3,
                darkcolor=theme3)
    for button in button_lst:
        button.button.config(bg=theme, fg=theme2, activebackground=theme)
    for label in label_lst:
        label.label.config(bg=theme, fg=theme2)

game_stage = 0

def game_update():
    global xp, level, maximum, game_stage
    if xp >= maximum:
        xp = 0
        level += 1
        maximum = math.ceil(maximum*1.01)
        if level >= 100:
            game_stage += 1
            level = 0
            gamestage_update(game_stage)

    label_lst[4].label.config(text=f"Meth: {meth}")
    label_lst[3].label.config(text=f"Level: {level}")
    label_lst[1].label.config(text=f"Cpc: {math.ceil(meth_p_c * cpc_perc/100)}")
    label_lst[2].label.config(text=f"Xp/c: {math.ceil(5 * xp_perc/100)}")
    for i in shop_lst[game_stage]:
        if i[4] is not None:
            i[5].label.config(text=f"Cpc: {i[4].production_inc}")
            i[6].label.config(text=f"Cost: {i[4].cost}")
            i[7].label.config(text=f"Qty: {i[4].qty}")
    #for i in upgrades_lst:
    #    i[1].label.config(text=f"+{button_lst[0].production_inc} % cpc")
    #    i[2].label.config(text=f"{button_lst[0].total_prodction} %")
    #    i[3].label.config(text=f"Cost: {button_lst[0].cost}")
    intro_label.config(bg=theme, fg=theme2)
    progressbar.config(maximum=maximum)
    progress.set(xp)
    add_shop_buttons(game_stage, level)

def auto_click():
    CLICK_BUTTON.clicked_button()
    root.after(time_to_click, auto_click)

def random_text(num):
    w_list = [["I Prefer To See It As \n The Study Of Change", "Stop It", "I Love My Family", "You Need To Study More"],["Smoking Marijuana \n Eating Cheetos \n And Masturbating Do Not \n Constitute Plans In My Book", "Because I Say So", "I'm In The \n Empire Business", "F**k You And \n Your Eyebrows"],["I Only Had You \n In My Heart", "Run", "I Could Have Saved Her", "If You Believe \n That There's A Hell"],["We Need To Cook!", "Stay Out Of \n My Territory", "Say My Name", "My Crystals Are Superior"],["You're An Insane \n Degenerate Piece Of Filth \n And You Deserve To Die", "I Sleep Just Fine", "I Am The One \n Who Knocks!", "I Am The One Who Knocks!"],["I Did It FOR ME!", "Jessie Was Never \n The Driving Force In \n This Arrangement", "I Won", "Tread Lightly"]]
    ran = random.randint(0, 3)
    return w_list[num-1][ran]

def walter_talk_destroy():
    walter_talk_label.destroy()

def walter_talk_create():
    global walter_talk_label
    walter_talk_label = Label(root, text=random_text(game_stage), font=("System", "7"), bg=theme,fg=theme2)
    walter_talk_label.place(relx=0.2, rely=0.8, anchor="nw")
    root.after(10000, walter_talk_create)
    root.after(5000, walter_talk_destroy)

walter_talk_create()

Y_pos = 0.25
def add_shop_buttons(game_stage, level):
    global Y_pos
    if Y_pos >= 0.85:
        Y_pos = 0.25
    if level == 0 and xp == 0:
        Y_pos = 0.25
        for i in shop_lst[game_stage-1]:
            if i[4] is not None:
                i[4].button.destroy()
                del button_lst[button_lst.index(i[4])]
            if i[5] is not None:
                i[5].label.destroy()
                del label_lst[label_lst.index(i[5])]
            if i[6] is not None:
                i[6].label.destroy()
                del label_lst[label_lst.index(i[6])]
            if i[7] is not None:
                i[7].label.destroy()
                del label_lst[label_lst.index(i[7])]

    for i in shop_lst[game_stage]:
        if i[3] <= level and i[4] is None:
            b = create_button(text=i[0], relx = 0.99, rely=Y_pos, anchor = "ne", production_inc=i[1], cost=i[2], ulevel=i[3], font=("System",18))
            i[4] = b
            b = create_label(text=f"Cpc: {button_lst[-1].production_inc}", relx=0.80, rely=Y_pos-0.002)
            i[5] = b
            b = create_label(text=f"Cost: {button_lst[-1].cost}", relx=0.80, rely=Y_pos+0.03)
            i[6] = b
            b = create_label(text="Qty: 0", relx=0.80, rely=Y_pos+0.06)
            i[7] = b
            Y_pos += 0.1

tkImage = ImageTk.PhotoImage(file = "game/meth.png")
CLICK_BUTTON = create_button(image=tkImage, relx=0.502, rely=0.687, anchor="center", button_type=None)
create_label(text = "Cpc: 1", font=("System","8"), relx=0.47, rely=0.75)
create_label(text = "Xp/c: 5", font=("System","8"), relx=0.47, rely=0.92)
create_label(text = f"Level: {level}", relx=0.5, rely=0.82, anchor="n", font=("System",18))
create_label("Meth: ", relx=0.5, rely=0.3, anchor="n", font=("System",18))

#create_label(text="Upgrades", relx=0, rely=0.26, font=("System",18))
#b = create_button(text="Meth Plant", relx=0, rely=0.36, font=("System",18), button_type=1, production_inc=1)
#upgrades_lst.append([b])
#b = create_button(text="Click Plant", relx = 0, rely = 0.46, font=("System",18), button_type=2, production_inc=1)
#upgrades_lst.append([b])
#b = create_button(text="Xp Plant", relx=0, rely=0.56, font=("System",18), button_type=3, production_inc=1)
#upgrades_lst.append([b])

#l = create_label(text=f"+{button_lst[0].production_inc} % cpc", relx=0.16, rely=0.36)
#upgrades_lst[0].append(l)
#l = create_label(text=f"{button_lst[0].total_prodction} %", relx = 0.16, rely = 0.39)
#upgrades_lst[0].append(l)
#l = create_label(text=f"Cost: {button_lst[0].cost}", relx = 0.16, rely = 0.42)
#upgrades_lst[0].append(l)

#l = create_label(text=f"+{button_lst[1].production_inc}", relx=0.16, rely=0.46)
#upgrades_lst[1].append(l)
#l = create_label(text=f"{button_lst[1].total_prodction}", relx = 0.16, rely = 0.49)
#upgrades_lst[1].append(l)
#l = create_label(text=f"Cost: {button_lst[1].cost}", relx = 0.16, rely = 0.52)
#upgrades_lst[1].append(l)

#l = create_label(text=f"+{button_lst[2].production_inc}%", relx=0.16, rely=0.56)
#upgrades_lst[2].append(l)
#l = create_label(text=f"{button_lst[2].total_prodction} %", relx = 0.16, rely = 0.59)
#upgrades_lst[2].append(l)
#l = create_label(text=f"Cost: {button_lst[2].cost}", relx = 0.16, rely = 0.62)
#upgrades_lst[2].append(l)

#image1 = PhotoImage(file="C:/Users/Elev/Documents/Programmering 2/Prog2-HjalmarAlbinsson/Övningar/game/plant1.png")
#create_label(relx=0.22, rely=0.35, image=image1)
#image2 = PhotoImage(file="C:/Users/Elev/Documents/Programmering 2/Prog2-HjalmarAlbinsson/Övningar/game/plant2.png")
#create_label(relx = 0.22, rely=0.45, image=image2)
#image3 = PhotoImage(file="C:/Users/Elev/Documents/Programmering 2/Prog2-HjalmarAlbinsson/Övningar/game/plant3.png")
#create_label(relx = 0.22, rely=0.55, image=image3)
walter_img = PhotoImage(file=f"game/bulk-image-crop (3)/walter{str(game_stage+1)}-removebg-preview.png")
walter_label = create_label(relx = 0.05, rely=0.75, image=walter_img)

intro_label = Label(root, text="Clicka på kristallen för att generera meth. \n Vid LVL: 3, 5, 15, 50, 75, 90 \n Adderas gubbar i shoppen. \n Vid LVL 100, startar en ny stage, max 5. \n (Har bara programmerat SHOPPEN till stage 2)", font=("System", "7"), bg=theme,fg=theme2)
intro_label.place(relx=0.5, rely=0.4, anchor="n")

#root.config(menu = mainmenu)
root.mainloop()
