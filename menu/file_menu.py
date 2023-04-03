from tkinter import *
from tkinter.filedialog import asksaveasfilename, askopenfile
import tkinter.messagebox as msgbox
import os

# exist_file_path: str # 이미 있는 파일 위치
# create_file_path: str # 만들어진 파일 위치
file_path: str
is_create: bool # 만들어진 파일인지
is_exist: bool # 열어진 파일인지
is_save: bool # 저장됬는지 확인
title: str # 파일 제목

is_create = False
is_exist = False
is_save = False


def file_rename(root: Tk):
    if is_save:
        rename_window = Tk()
        rename_window.geometry("300x100")
        rename_window.title("이름 변경")
        rename_window.resizable(False, False)

        # 창을 가운데로 옮기는 코드
        screen_width = rename_window.winfo_screenwidth()
        screen_height = rename_window.winfo_screenheight()

        x = (screen_width / 2) - (300 / 2)
        y = (screen_height / 2) - (100 / 2)

        rename_window.geometry("+%d+%d" % (x, y))

        rename_entry = Entry(rename_window, width=30, highlightthickness=0)
        rename_entry.pack()

        rename_entry.insert(0, title)

        def handle_rename():
            global file_path, title

            print("리네임")

            new_path = file_path[0:len(file_path) - len(title)] + rename_entry.get()
            os.rename(file_path, new_path)

            file_path = new_path

            path_split = new_path.split('/')
            title = path_split[len(path_split) - 1]

            root.title(f"{title}(저장 안됨) - Memo.py")

            rename_window.destroy()

        rename_btn = Button(rename_window, padx=130, text="확인", command=handle_rename)
        rename_btn.pack(side="bottom")
    else:
        msgbox.showwarning("경고", "파일을 저장해주세요")
        return


def file_create(root: Tk, text: Text):
    global is_create, is_exist, is_save

    if len(text.get("1.0", END)) == 1: # 파일에 내용이 없다면
        is_create = True
        is_exist = False
        is_save = False

        root.title("제목 없음(저장 안됨) - Memo.py")
    else: # 파일에 내용이 있다면
        choose = msgbox.askyesno("경고", "작성한 상태에서 파일을 열면 작성한 데이터가 다 날아갑니다.\n그래도 하시겠습니까?")

        if choose:
            is_create = True
            is_exist = False
            is_save = False

            root.title("제목 없음(저장 안됨) - Memo.py")

            text.delete("1.0", END)


def file_save(root: Tk, text: Text):
    global file_path, title, is_save

    if is_create: # 만들어진 파일이라면
        path = asksaveasfilename() # 파일 저장 ui를 띄우기

        file = open(path, 'w')
        file.write(text.get("1.0", END))
        file.close()

        file_path = path

        path_split = file_path.split('/')
        title = path_split[len(path_split) - 1]

    elif is_exist: # 열어진 파일이라면
        file = open(file_path, 'w')
        file.write(text.get("1.0", END))
        file.close()

    else: # 파일이 만들어진 것도 아니고 연것도 아닐 경우
        msgbox.showwarning(title="저장 오류", message="파일을 생성하거나 파일을 열어주세요")

        return

    root.title(f"{title} - Memo.py")

    is_save = True


def file_open(root: Tk, text: Text):
    global is_exist, is_create, file_path, title, is_save

    if len(text.get("1.0", END)) == 1: # 파일에 내용이 없다면
        Tk().withdraw()

        file = askopenfile()

        path_split = file.name.split('/')
        title = path_split[len(path_split) - 1]

        root.title(f"{title}(저장 안됨) - Memo.py")
        text.insert(END, file.read())

        is_exist = True
        is_create = False
        is_save = False

        file_path = file.name
    else: # 파일에 내용이 있다면
        choose = msgbox.askyesno("경고", "작성한 상태에서 파일을 열면 작성한 데이터가 다 날아갑니다.\n그래도 하시겠습니까?")

        if choose: # msgbox에서 "네"를 선택
            Tk().withdraw()

            file = askopenfile()

            path_split = file.name.split('/') # 파일 경로를 /로 자르고
            title = path_split[len(path_split) - 1] # 경로 마지막 제목 가져오기

            root.title(f"{title}(저장 안됨) - Memo.py")
            text.delete("1.0", END)
            text.insert(END, file.read())

            is_exist = True
            is_create = False
            is_save = False

            file_path = file.name # 열어진 파일 경로 넣기
