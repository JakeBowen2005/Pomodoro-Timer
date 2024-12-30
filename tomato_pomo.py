import tkinter
import time
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

timer_after_id = None

check_marks = ""

# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
        global timer_after_id, check_marks
        if timer_after_id:
                window.after_cancel(timer_after_id)
                timer_after_id = None

        
        reset_text = "00:00"
        canvas.itemconfig(text_id, text=reset_text)
        check_marks = ""
        checkmark_label.config(text=check_marks)

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_25(seconds=WORK_MIN*60):
        global check_marks, timer_after_id
        timer = time.strftime("%M:%S", time.gmtime(seconds))
        canvas.itemconfig(text_id, text=timer)
        # widget.after(delay_ms, function, *args)


        if seconds > -1:
                timer_after_id = window.after(1000, start_25, seconds-1)
        else:
                check_marks += "✓"
                checkmark_label.config(text=check_marks)
                five_min()


def five_min(seconds=SHORT_BREAK_MIN*60):
        global timer_after_id
        if len(check_marks) >3:
                long_break()
                return
        timer = time.strftime("%M:%S", time.gmtime(seconds))
        canvas.itemconfig(text_id, text=timer)

        if seconds > -1:
                timer_after_id = window.after(1000, five_min, seconds-1)
        else:
                start_25()

def long_break(seconds=LONG_BREAK_MIN*60):
        global timer_after_id
        timer = time.strftime("%M:%S", time.gmtime(seconds))
        canvas.itemconfig(text_id, text=timer)

        if seconds > -1:
                timer_after_id = window.after(1000, long_break, seconds-1)
        else:
                reset()

        
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Pomo Timer")
window.config(padx=100, pady=100, bg=PINK)

timer_text = tkinter.Label(text="Timer", fg=GREEN, font=(FONT_NAME, 40, "bold"), bg=PINK)
timer_text.grid(row=0, column=1)

tomato_img = tkinter.PhotoImage(file="tomato.png")
canvas = tkinter.Canvas(width=200, height=224, bg=PINK, highlightthickness=0)
canvas.create_image(100, 112, image=tomato_img)
text_id = canvas.create_text(103, 150, text="00:00", font=(FONT_NAME, 35, "bold"), fill="white")
canvas.grid(row=1,column=1)

start_button = tkinter.Button(text="Start", highlightbackground=PINK, command=start_25)
start_button.grid(row=2, column=0)

reset_button = tkinter.Button(text="Reset", highlightbackground=PINK, command=reset)
reset_button.grid(row=2, column=2)

checkmark_label = tkinter.Label(text=check_marks, fg=GREEN, bg=PINK, font=(FONT_NAME, 40, "bold"))
checkmark_label.grid(row=2,column=1)



window.mainloop()