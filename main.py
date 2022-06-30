from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #


BEIDGE = "#E0C097"
RED = "#FF7878"
GREEN = "#CEE5D0"
YELLOW = "#F3F0D7"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
check = "✔"
timer = None
# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    window.after_cancel(timer)
    name.config(text="TIMER", fg='black')
    canvas.itemconfig(timer_text, text="00:00")
    checkmark.config(text="")

# ---------------------------- TIMER MECHANISM ------------------------------- #

    
def start_timer():
    global reps
    reps += 1

    
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    #Check if it's 8th for going to long break time
    if reps % 8 == 0:
        count_down(long_break_sec)
        name.config(text="Break", fg=RED)

    #if its the 2nd/4th/6th for going to short break time
    elif reps % 2 == 0:
        count_down(short_break_sec)
        name.config(text="Break", fg=GREEN)
    #if odd number for going to work time
    else:
        count_down(work_sec)
        name.config(text="WORK TIME!", fg=YELLOW)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    global check
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec == 0:
        count_sec = "00"
    elif count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        # timer set to 1s
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        if (reps % 2) == 0:
            checkmark.config(text=check)
            check += "✔"

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("TimeGress")
window.config(padx=50, pady=50, bg=BEIDGE)


canvas = Canvas(width=334 ,height=334, bg=BEIDGE, highlightthickness=0)
image = PhotoImage(file="clock.png")
canvas.create_image(167, 167, image=image)
timer_text = canvas.create_text(168,190, text="00:00", font=(FONT_NAME, 25, "bold"), fill=RED)
canvas.grid(column=2,row=1)

#Label
name = Label(text="TIMER", font=(FONT_NAME, 26, "bold"))
name.config(fg="black", bg=BEIDGE)
name.grid(column=2, row=0)


checkmark = Label(font=(FONT_NAME, 16))
checkmark.config(fg=GREEN, bg=BEIDGE)
checkmark.grid(column=2, row=3)

#Buttons
start_button = Button(text="START", command=start_timer)
start_button.grid(column=1, row=2)


reset_button = Button(text="RESET", command=reset_timer)
reset_button.grid(column=3, row=2)




window.mainloop()
