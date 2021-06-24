import tkinter
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
FONT = ("Arial", 20, "bold")
STATUS_FONT = ("Arial", 20, "bold")
reps = 0
cycle = ''
checks = ''
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 


def reset_timer():
    global checks
    global reps
    global cycle
    checks = ''
    reps = 0
    cycle = ''

    window.after_cancel(timer)
    canva.itemconfig(timer_text, text="00:00")

    timer_header.config(text="TIMER")
    checkmarks.config(text=checks)
    cycle_number.config(text=f"{cycle}")


# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    global checks
    global cycle
    box = "☐"
    mark = "✅"
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 2 != 0:
        count_down(work_sec)
        timer_header.config(text="WORK", fg=GREEN, font=STATUS_FONT)
        checks += box
        checkmarks.config(text=checks)
    elif reps % 8 == 0:
        count_down(long_break_sec)
        timer_header.config(text="LONG BREAK", fg=RED, font=STATUS_FONT)
        checks = checks[:-1]
        checks += mark
        checkmarks.config(text=checks)
        checks = ''
        cycle += "🍅"
        cycle_number.config(text=f"{cycle}")
        if cycle == "🍅🍅🍅🍅🍅":
            cycle += "\n"
        elif cycle == "🍅🍅🍅🍅🍅\n🍅🍅🍅🍅🍅":
            cycle += "\n"
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_header.config(text="SHORT BREAK", fg=PINK, font=STATUS_FONT)
        checks = checks[:-1]
        checks += mark
        checkmarks.config(text=checks)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 


def count_down(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canva.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canva = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = tkinter.PhotoImage(file="tomato.png")
canva.create_image(100,112, image=tomato_img)

timer_header = tkinter.Label(text="TIMER", font=FONT, fg=GREEN, bg=YELLOW)
timer_header.grid(column=1, row=0)
timer_header.config(padx=10, pady=10)

timer_text = canva.create_text(103,130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canva.grid(column=1, row=1)

cycle_number = tkinter.Label(text=f"{cycle}", font=FONT, fg=RED, bg=YELLOW)
cycle_number.grid(column=1, row=3)
# cycle_number.config()

button_start = tkinter.Button(text="Start", command=start_timer, highlightthickness=0)
button_start.grid(column=0, row=3)
button_start.config(padx=10, pady=10)

button_reset = tkinter.Button(text="Reset", command=reset_timer, highlightthickness=0)
button_reset.grid(column=2, row=3)
button_reset.config(padx=10, pady=10)

checkmarks = tkinter.Label(font=FONT, fg=GREEN, bg=YELLOW)
checkmarks.grid(column=1, row=2)
checkmarks.config(padx=10, pady=20)


window.mainloop()