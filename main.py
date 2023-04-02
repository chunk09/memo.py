from tkinter import *
from menu.function import file_create, file_open, file_save

root = Tk()
root.title("Memo.py")
root.geometry("600x500")
root.resizable(False, False)

menu = Menu(root)
text = Text(root, width=600, height=500, highlightthickness=0, padx=5, pady=5)

# 메뉴 파일
menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label="만들기", command=lambda: file_create(root, text))
menu_file.add_command(label="열기", command=lambda: file_open(root, text))
menu_file.add_command(label="저장", command=lambda: file_save(root, text))
menu_file.add_separator()
menu_file.add_command(label="끝내기", command=root.quit)

# 메뉴 편집
menu_edit = Menu(menu, tearoff=0)
menu_edit.add_command(label="편집", state="disable")

# 메뉴 서식
menu_format = Menu(menu, tearoff=0)
menu_format.add_command(label="서식", state="disable")

# 메뉴 보기
menu_view = Menu(menu, tearoff=0)
menu_view.add_command(label="보기", state="disable")

# 메뉴 등록
menu.add_cascade(label="파일", menu=menu_file)
menu.add_cascade(label="편집", menu=menu_edit)
menu.add_cascade(label="서식", menu=menu_format)
menu.add_cascade(label="보기", menu=menu_view)

root.config(menu=menu)

text.pack()

root.mainloop()
