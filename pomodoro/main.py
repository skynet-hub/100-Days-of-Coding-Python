from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 2
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    window.after_cancel(timer)
    text.config(text="Timer", fg=GREEN)
    check.config(text='')
    canvas.itemconfig(timer_text, text="00:00")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        text.config(text="LONG BREAK", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        text.config(text="SHORT BREAK", fg=PINK)
    else:
        count_down(work_sec)    
        text.config(text='Work', fg=GREEN)
      

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60 

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text= f"{count_min}: {count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()   
        work_sessions = math.floor(reps / 2)
        marks = ''
        for _ in range(work_sessions):
            marks += "✔"

        check.config(text=marks)     
        

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


canvas = Canvas()
canvas.config(width=200, height=224, bg=YELLOW, highlightthickness= 0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 140, text="00:00", fill="white", font=(FONT_NAME, 32, "bold"))
canvas.grid(column=1, row=1)


text = Label(text="Timer")
text.config(bg=YELLOW, font=(FONT_NAME, 36, 'bold'), fg=GREEN, pady=10)
text.grid(column=1, row=0)

start_btn = Button(text='Start', command=start_timer)
start_btn.grid(column=0, row=2)
start_btn.config(pady=10, padx=5, highlightthickness=0)


reset_btn = Button(text='Reset', command=reset_timer)
reset_btn.grid(column=2, row=2)
reset_btn.config(pady=10, padx=5, highlightthickness=0)

check = Label()
check.config(fg=GREEN, bg=YELLOW)
check.grid(column=1, row=3)



window.mainloop()