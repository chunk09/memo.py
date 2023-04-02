from tkinter import *
from tkinter.filedialog import asksaveasfilename, askopenfile
import tkinter.messagebox as msgbox

exist_file_path: str # 이미 있는 파일 위치
is_create: bool # 만들어진 파일인지
is_exist: bool # 열어진 파일인지
title: str # 파일 제목

is_create = False
is_exist = False


def file_create(root: Tk, text: Text):
    global is_create
    global is_exist

    if len(text.get("1.0", END)) == 1: # 파일에 내용이 없다면
        is_create = True
        is_exist = False

        root.title("제목 없음(저장 안됨) - Memo.py")
    else: # 파일에 내용이 있다면
        choose = msgbox.askyesno("경고", "작성한 상태에서 파일을 열면 작성한 데이터가 다 날아갑니다.\n그래도 하시겠습니까?")

        if choose:
            is_create = True
            is_exist = False

            root.title("제목 없음(저장 안됨) - Memo.py")

            text.delete("1.0", END)


def file_save(root: Tk, text: Text):
    if is_create: # 만들어진 파일이라면
        path = asksaveasfilename() # 파일 저장 ui를 띄우기

        file = open(path, 'w')
        file.write(text.get("1.0", END))
        file.close()

    elif is_exist: # 열어진 파일이라면
        file = open(exist_file_path, 'w')
        file.write(text.get("1.0", END))
        file.close()
    else: # 파일이 만들어진 것도 아니고 연것도 아닐 경우
        msgbox.showwarning(title="저장 오류", message="파일을 생성하거나 파일을 열어주세요")

        return

    if is_create:
        root.title("제목 없음 - Memo.py")
    elif is_exist:
        root.title(f"{title} - Memo.py")


def file_open(root: Tk, text: Text):
    global is_exist
    global is_create
    global exist_file_path
    global title

    if len(text.get("1.0", END)) == 1: # 파일에 내용이 없다면
        Tk().withdraw()

        file = askopenfile()

        path_split = file.name.split('/')
        title = path_split[len(path_split) - 1]

        root.title(f"{title}(저장 안됨) - Memo.py")
        text.insert(END, file.read())

        is_exist = True
        is_create = False

        exist_file_path = file.name
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

            exist_file_path = file.name # 열어진 파일 경로 넣기
