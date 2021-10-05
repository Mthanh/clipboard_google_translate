import logging
import threading

root_time_loop = 500

# from google_trans_new import google_translator
# translator = google_translator()

from googletrans import Translator

translator = Translator()

# translated = translator.translate(line, dest="ja");

data_get = "start"
old_data_get = "XXXXXX"
new_result = "XXXXXX"

SRC_trans = "en"
DES_trans = "vi"

import time
import pyperclip

from tkinter import *
import tkinter as tk

root = tk.Tk()


def remove_newline(data_clipboard):
    data_clipboard = data_clipboard.replace("\r\n", " ")
    data_clipboard = data_clipboard.replace("\n\r", " ")
    data_clipboard = data_clipboard.replace("\r", " ")
    data_clipboard = data_clipboard.replace("\n", " ")

    return data_clipboard


text_before = ""


def get_clipboard():
    global REMOVE_ENTER, text_before
    data_clipboard = text_before
    try:
        data_clipboard = root.clipboard_get()

        if REMOVE_ENTER == True:
            text_before_Remove_enter = data_clipboard
            data_clipboard = remove_newline(data_clipboard)

            REMOVE_ENTER = False
            set_clipboard(data_clipboard)
    except Exception as e:
        # print(str(e))
        pass

    text_before = data_clipboard
    return data_clipboard


def set_clipboard(text_set):
    try:
        root.clipboard_clear()
        root.clipboard_append(text_set)
    except Exception as e:
        # print(str(e))
        pass


def change_des(src):
    global DES_trans, old_data_get
    DES_trans = src

    root.title('Translate to ' + DES_trans + "; Log : " + Log_name_only)
    old_data_get = "X321njid1n21hoxz x x x"


REMOVE_ENTER = True


# REMOVE_ENTER = True
def change_REMOVE_ENTER():
    global REMOVE_ENTER, old_data_get, new_result
    REMOVE_ENTER = not REMOVE_ENTER

    old_data_get = "XXXXXX3_old_data_get REMOVE_ENTER"
    new_result = "XXXXXX4_new_result REMOVE_ENTER"

    root.title('Translate to ' + DES_trans + "; Log : " + Log_name_only)


import os
from pathlib import Path

PATH_FILE_WIN = Path(__file__).absolute()

PATH_FILE = str(PATH_FILE_WIN).replace('\\', '/')
PATH_FILE_SPLIT = str(PATH_FILE).split("/")

PATH_FILE_SPLIT.pop(len(PATH_FILE_SPLIT) - 1)

PATH_FOLDER = ("/").join(PATH_FILE_SPLIT)

PATH_SAVE = PATH_FOLDER + "/LOG/"

if not os.path.isdir(PATH_SAVE):
    os.makedirs(PATH_SAVE)

from datetime import datetime

today = datetime.today()
d0 = today.strftime("%y-%m-%d")
d1 = today.strftime('%Y-%m-%d-%H-%M-%S')
Log_name_only = d1 + "_log.csv"
Log_name = PATH_SAVE + Log_name_only
print("Log_name = ", Log_name)
# f = open(Log_name, "w", encoding='utf8', errors='replace')
# f.close()

from tkinter.messagebox import showinfo


def popup_showinfo(title, text):
    showinfo(title, text)


previous_save = ""


def save_log():
    global previous_save
    if previous_save == old_data_get:
        return

    f = open(Log_name, "a", encoding='utf-8-sig', errors='replace')

    save_old_data_get = remove_newline(old_data_get).replace(",", ";")
    save_new_result = remove_newline(new_result).replace(",", ";")

    new_line = save_old_data_get + "," + save_new_result + "\n"

    f.write(new_line)
    f.close()

    previous_save = old_data_get


import subprocess

FILEBROWSER_PATH = os.path.join(os.getenv('WINDIR'), 'explorer.exe')

PATH_FILE_WIN_LOG = PATH_SAVE.replace("/", "\\")


def open_log():
    print(PATH_FILE_WIN_LOG)
    # subprocess.run([FILEBROWSER_PATH, "C:/thanh/translate_py/LOG"])
    subprocess.Popen(f'explorer "{PATH_FILE_WIN_LOG}"')


def is_all_space(input_text):
    for i in range(len(input_text)):
        if input_text[i] != ' ':
            return 1
    return 0


def changeText(Text_in_or_out, text_change):
    Text_in_or_out.delete(1.0, "end")
    Text_in_or_out.insert(1.0, text_change)
    return ()


def changeText_input(Text_in_or_out, text_change):
    Text_in_or_out.insert(END, text_change)
    return ()


def changeText_clear(Text_in_or_out):
    Text_in_or_out.delete(1.0, "end")
    return ()


def translate_api(text):
    try:
        translated = translator.translate(text, dest=DES_trans)
        result = translated.text

    except Exception as e:
        result = str(e)

    return result


def translate_by_line(text):
    return_text = ""
    changeText_clear(output_text)
    for line in text.splitlines():
        if is_all_space(line) == 1:
            line_result = translate_api(line) + "\n"
            return_text += line_result
        else:
            line_result = "\n"
            return_text += line_result

        changeText_input(output_text, line_result)
    return return_text


def translate(text):
    global old_data_get, new_result, input_text, result

    # translate
    result = translate_api(text)
    changeText(output_text, result)

    old_data_get = text
    new_result = result

    root.call('wm', 'attributes', '.', '-topmost', '1')
    root.after_idle(root.call, 'wm', 'attributes', '.', '-topmost', False)
    return ()


THREAD = True


def task1_thread():
    while THREAD == True:
        global old_data_get, new_result, input_text, result

        # neu ma text bi thay doi boi clipboard
        data_get = get_clipboard()

        if is_all_space(data_get) == 1 and data_get != old_data_get and data_get != new_result and data_get != "":
            changeText(input_text, data_get)
            translate(data_get)
            continue

        # neu text bi thay doi boi chinh sua
        new_input_text = input_text.get("1.0", 'end-1c')
        if is_all_space(data_get) == 1 and new_input_text != old_data_get and new_input_text != "":
            translate(new_input_text)
            set_clipboard(new_input_text)
            continue

        time.sleep(1 / 50)


root.title('Translate to ' + DES_trans + "; Log : " + Log_name_only)

input_text = Text(width=35, height=15, wrap=WORD, font=("Arial", 11))
input_text.grid(row=1, column=0, pady=0, padx=0, columnspan=100, sticky=W)

output_text = Text(width=35, height=15, wrap=WORD, font=("Arial", 11))
output_text.grid(row=1, column=101, columnspan=100, pady=0, padx=0, sticky=W)

# button
buttonvi = Button(root, text="VI", command=lambda: change_des("vi"))
buttonvi.config(font=("NSimSun", 11))
buttonvi.grid(row=0, column=0, sticky=W)

buttonja = Button(root, text="JA", command=lambda: change_des("ja"))
buttonja.config(font=("NSimSun", 11))
buttonja.grid(row=0, column=1, sticky=W)

buttonen = Button(root, text="EN", command=lambda: change_des("en"))
buttonen.config(font=("NSimSun", 11))
buttonen.grid(row=0, column=2, sticky=W)

buttonlog = Button(root, text="Save_Log", command=lambda: save_log())
buttonlog.config(font=("NSimSun", 11))
buttonlog.grid(row=0, column=3, sticky=W)

buttoncp = Button(root, text="Open_Log", command=lambda: open_log())
buttoncp.config(font=("NSimSun", 11))
buttoncp.grid(row=0, column=4, sticky=W)

# button
buttoncp = Button(root, text="CP_ONE", command=lambda: set_clipboard(new_result))
buttoncp.config(font=("NSimSun", 11))
buttoncp.grid(row=0, column=101, sticky=W)

buttoncp = Button(root, text="CLEAR", command=lambda: input_text.delete(1.0, "end"))
buttoncp.config(font=("NSimSun", 11))
buttoncp.grid(row=0, column=102, sticky=W)

buttoncp = Button(root, text="REMOVE_ENTER_PDF", command=lambda: change_REMOVE_ENTER())
buttoncp.config(font=("NSimSun", 11))
buttoncp.grid(row=0, column=103, sticky=W)

# root.minsize(570, 100)
# root.maxsize(570, 900)


x = threading.Thread(target=task1_thread, args=())
logging.info("Main    : before running thread")
x.start()

# root.after(root_time_loop, task)
root.mainloop()

THREAD = False
x.join()
print("EXIT")
