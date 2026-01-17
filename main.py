import tkinter as tk

# window
win = tk.Tk()
win.title("Simple Calculator")
win.geometry("300x400")

# display
screen = tk.Entry(win, font=("Arial", 18), justify="right")
screen.pack(fill="x", padx=10, pady=10)

# button function
def press(num):
    screen.insert(tk.END, num)

# clear screen
def clear():
    screen.delete(0, tk.END)

# result
def equal():
    try:
        ans = eval(screen.get())
        screen.delete(0, tk.END)
        screen.insert(0, ans)
    except:
        screen.delete(0, tk.END)
        screen.insert(0, "Error")

# frame
f = tk.Frame(win)
f.pack()

# buttons
btns = [
    '7','8','9','/',
    '4','5','6','*',
    '1','2','3','-',
    '0','.','=','+'
]

r = 0
c = 0

for b in btns:
    if b == '=':
        tk.Button(f, text=b, width=10, height=2, command=equal).grid(row=r, column=c)
    else:
        tk.Button(f, text=b, width=5, height=2,
                  command=lambda x=b: press(x)).grid(row=r, column=c)

    c += 1
    if c == 4:
        c = 0
        r += 1

# clear button
tk.Button(win, text="Clear", width=20, command=clear).pack(pady=10)

win.mainloop()
