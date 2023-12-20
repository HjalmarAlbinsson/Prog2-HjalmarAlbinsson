from tkinter import ttk
from tkinter import *
import random
 
root = Tk()
root.geometry("400x500")
root.title("Wordle")
root.rowconfigure(0,weight=1)
root.columnconfigure(0,weight=1)

bg_img = PhotoImage(file = "C:/Users/Elev/Documents/Programmering 2/Prog2-HjalmarAlbinsson/Övningar/widgets/rsz_original_1.png") 
canvas = Canvas(root, width=400, height=500)
IMAGE = canvas.create_image(400/2, 500/2, image=bg_img, anchor="center")
canvas.grid(column=0, row=0, sticky=N+S+E+W)

last_width = 400
last_height = 500


def load_words():
    complete_word_list = set()
    with open("widgets/words.txt") as word_file:
        complete_word_list = set(word_file.read().split())
    return complete_word_list
complete_word_list = load_words()


def play():
    global frame, word_to_be_guessed, game_stage
    frame.destroy()
    frame = Frame(root)
    frame.grid(column=0, row=0, sticky="n")
    word_to_be_guessed = Chooseword()
    game_stage = 0
    canvas.itemconfigure(warning_text, text="", fill="Green")


def resize(event):
    global last_width, last_height
    canvas.move(IMAGE, (event.width-last_width)/2, (event.height-last_height)/2)
    canvas.move(warning_text, (event.width-last_width)/2, (event.height-last_height)/2)
    last_height = event.height
    last_width = event.width

canvas.bind("<Configure>", resize)

global frame
frame = Frame(root)
frame.grid(column=0, row=0, sticky="n")

mainmenu = Menu()
mainmenu.add_command(label = "Play again", command= play)  
mainmenu.add_command(label = "Exit", command= root.destroy)


def Chooseword():
    wordList = open("widgets\wordBank.txt").readlines()
    return random.choice(wordList).upper()


game_stage = 0
word_to_be_guessed = Chooseword()
print(word_to_be_guessed)

warning_text = canvas.create_text(last_width/2, last_height/2.18, text="", fill="Yellow", font="bold, 11")
running = True

def add_labels(event):
    global game_stage, running
    if not running:
        return
    word = entry.get().upper()
    if len(word) < 5 or word not in complete_word_list:
        canvas.itemconfigure(warning_text, text="Please enter a 5 letter word")
        return
    else:
        canvas.itemconfigure(warning_text, text="")
    game_stage += 1
    for i, letter in enumerate(word):
        if letter == word_to_be_guessed[i]:
            color = "green"
        elif letter in word_to_be_guessed:
            color = "yellow"
        else:
            color = "White"
        label = Label(frame, text = letter, fg=color, bg="#161618")
        label.grid(row=game_stage, column=i, sticky="nsew")
        label.grid_rowconfigure(0, weight=1)
        label.grid_columnconfigure(0, weight=1)

    if word[:4] == word_to_be_guessed[:4]:
        canvas.itemconfigure(warning_text, text="You won!", fill="Green")
        running = False
    elif game_stage >= 6:
        canvas.itemconfigure(warning_text, text=f"You lost! The word was: {word_to_be_guessed}", fill="Red")
        running = False


def validate_entry(text, new_text):
    if len(new_text) > 5:
        return False
    return not text.isdecimal()
entry = ttk.Entry(
    validate="key",
    validatecommand=(root.register(validate_entry), "%S", "%P"),
    justify='center'
)

entry.bind('<Return>', add_labels)
entry.place(relx=0.5, rely=0.5, width=100, anchor="center")

root.config(menu = mainmenu)
root.mainloop()