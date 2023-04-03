from tkinter import *
from menu.file_menu import file_create, file_open, file_save, file_rename


def menu(root: Tk, text: Text) -> Menu:
    menu = Menu(root)

    # 메뉴 파일
    menu_file = Menu(menu, tearoff=0)
    menu_file.add_command(label="만들기", command=lambda: file_create(root, text))  # 인수를 사용해야하므로 람다 사용
    menu_file.add_command(label="열기", command=lambda: file_open(root, text))
    menu_file.add_separator()
    menu_file.add_command(label="저장", command=lambda: file_save(root, text))
    menu_file.add_command(label="이름 변경", command=lambda: file_rename(root))
    menu_file.add_separator()
    menu_file.add_command(label="끝내기", command=root.quit)

    # 메뉴 등록
    menu.add_cascade(label="파일", menu=menu_file)

    return menu
