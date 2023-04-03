from tkinter import *
from menu.menu import menu

root = Tk()
root.title("Memo.py")
root.geometry("600x500")
# root.resizable(False, False)

# root을 가운데로 옮기는 코드
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = (screen_width / 2) - (600 / 2)
y = (screen_height / 2) - (500 / 2)

root.geometry("+%d+%d" % (x, y))


text = Text(root, width=600, height=500, highlightthickness=0, padx=5, pady=5)

root.config(menu=menu(root, text))

text.pack()

root.mainloop()
