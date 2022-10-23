import tkinter as tk
import datetime
import sys
from tkinter import messagebox as mb
import paramiko
import cv2
import os
import time

root = tk.Tk()
root.title("MinecraftServerManager Special Edition")
root.geometry("854x480")
root.iconbitmap("icon.ico")
root.resizable(height=False, width=False)

def ui_1():
    root.geometry("854x480")
    root.resizable(height=False, width=False)
def ui_2():
    root.geometry("1280x720")
    root.resizable(height=False, width=False)
def ui_3():
    root.geometry("1920x1080")
    root.resizable(height=False, width=False)

def ui_4():
    root.resizable(height=True, width=True)

def gui_setting():
    gui_setting_menu=tk.Toplevel()
    gui_setting_menu.title("設定 | GUIの大きさ")
    gui_setting_menu.geometry("300x150")
    gui_setting_menu.resizable(height=False, width=False)
    gui_setting_menu.iconbitmap("icon.ico")

    label1=tk.Label(gui_setting_menu, text="※このツールは720P,および1080PにはUIの対応がされていません。\n公式推奨外です。　　　　　　　　　　　　　 　　　　")
    label1.pack()
    radio_button1 = tk.Radiobutton(gui_setting_menu, text="854x480(推奨)", value=1, variable=ui, command=ui_1)
    radio_button2 = tk.Radiobutton(gui_setting_menu, text="1280x720(準推奨)", value=2, variable=ui, command=ui_2)
    radio_button3 = tk.Radiobutton(gui_setting_menu, text="1920x1080(非推奨)", value=3, variable=ui, command=ui_3)
    radio_button4 = tk.Radiobutton(gui_setting_menu, text="カスタム", value=4, variable=ui, command=ui_4)

    radio_button1.pack()
    radio_button2.pack()
    radio_button3.pack()
    radio_button4.pack()

def on_closing():
    close_message=mb.askyesno("終了", "終了してもよろしいですか?")
    if close_message == True:
        sys.exit()

def readme():
    readme=tk.Toplevel()
    readme.title("ReadMe")
    readme.geometry("400x300")
    readme.resizable(height=False, width=False)
    readme.iconbitmap("icon.ico")

    readme_label=tk.Label(readme,text="©2022 Rays-Soft\n本ツールをダウンロードしていただき、誠にありがとうございます。\n本ツールは、いつも使われているマイサーバーの負荷の確認のために作成いたしました。\nぜひ皆様のお役にたてたらと思います。\nこの場で利用規約を定めたいと思います。\n・このツールのコピーは禁止とさせていただきます。\n・バグなどございましたらGitHubの方までよろしくお願いします。\n・また、「自分が作った」発言もおやめください。\n・なお、このツールは既存のMinecraftServerManagerとは一切関係ございません。\n・このツールにはアップデート通知機能がありませんので、定期的にGitHubをご覧ください\n・Beta版なので、少々のバグはご了承ください\n")
    readme_label.pack()

def wakaran():
    mb.showinfo("ヘルプ", "使い方:\n一番上の「IP」と書かれた部分の、\n「IP」を消し、お使いのサーバーのIPを入れてください。\n上から2番目の「UserName」の所には、ユーザー名を入れてください。(ここもUserNameは消してください)\n3行目はパスワードです。(IPと同じなので端折ります)")
    ok=mb.askyesno("ヘルプ", "使い方は分かっていただけたでしょうか?")
    if ok == False:
        command=wakaran()

def version():
    mb.showinfo('バージョン', 'バージョン:Beta 1.3')

def quit():
    quit_menu = mb.askyesno('MinecraftServerManager', '終了してもよろしいですか？')
    if quit_menu == True:
        sys.exit()

def login_kakuritsu():

    frame_right.destroy()
    menu.destroy()
    time.sleep(4)
    root.destroy()
    time.sleep(2.5)
    cap=cv2.VideoCapture(r'C:\Users\rei\Videos\python.mp4')

    if (cap.isOpened()== False):
        print("ビデオファイルが再生できませんでした")

    while(cap.isOpened()):

        ret, frame = cap.read()
        if ret == True:

            cv2.imshow("Video", frame)

            if cv2.waitKey(25) & 0xFF == ord('q'):
                break
        else:
            break
    cap.release()
    cv2.destroyAllWindows()

ui=tk.IntVar(value=1)

menu = tk.Menu(root)
root.config(menu=menu)
setting_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label='設定', menu=setting_menu)
setting_menu.add_command(label='GUIの大きさ', command=gui_setting)
setting_menu.add_command(label='バージョン', command=version)
login_menu=tk.Menu(menu, tearoff=0)
menu.add_cascade(label='実行', menu=login_menu)
login_menu.add_cascade(label='終了', command=quit)
help=tk.Menu(setting_menu, tearoff=0)
setting_menu.add_cascade(label="ヘルプ", menu=help)
help.add_cascade(label="ReadMe", command=readme)
help.add_cascade(label="使い方が分からない", command=wakaran)

# 右カラム
frame_right = tk.Frame(root, pady=5, padx=5)
IP_form = tk.Entry(frame_right, font=("Ubuntu"))
IP_form.insert(0, "IP")
User_form = tk.Entry(frame_right, font=("Ubuntu"))
User_form.insert(0, "User Name")
Password_form = tk.Entry(frame_right, font=("Ubuntu"))
Password_form.insert(0, "Password")
shashin_load = tk.PhotoImage(file="MinecraftServerManager.png")
login_kakuritsu=tk.Button(frame_right, text="ログインを確立", command=login_kakuritsu)

l_image = tk.Label(frame_right, image=shashin_load,  borderwidth = 5, width = 400, relief="ridge")
l_image.pack(anchor=tk.CENTER)
frame_right.tkraise()

# ウィジェットの配置
frame_right.pack(anchor=tk.CENTER)
IP_form.pack()
User_form.pack()
Password_form.pack()
login_kakuritsu.pack()

root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()
