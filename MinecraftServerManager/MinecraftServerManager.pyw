import tkinter as tk
import datetime
import sys
from tkinter import messagebox as mb
import paramiko
from tkinter import ttk

root = tk.Tk()
root.title("MinecraftServerManager")
root.iconbitmap("icon.ico")
root.geometry("854x480")
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
        wakaran()

def version():
    mb.showinfo('バージョン', 'バージョン:Beta 1.3')

def quit():
    quit_menu = mb.askyesno('MinecraftServerManager', '終了してもよろしいですか？')
    if quit_menu == True:
        root.destroy()

def login_kakuritsu():

    IP_val = IP_form.get()
    User_val = User_form.get()
    Password_val = Password_form.get()

    if IP_val == "IP":
        mb.showinfo("MinecraftServerManager", "有効なIPアドレスではありません")

    elif User_val == "User Name":
        mb.showinfo("MinecraftServerManager", "有効なユーザー名ではありません")

    elif Password_val == "Password":
        mb.showinfo("MinecraftServerManager", "有効なパスワードではありません。")

    else:

        fuka_frame = tk.Frame(root)
        fuka_frame.pack(anchor=tk.NW)

        frame_right.destroy()

        menu.destroy()

        int_var=tk.StringVar(value=5)

        sub=tk.Toplevel()
        sub.title("処理中")
        progress=ttk.Progressbar(sub, orient="horizontal", length=200, mode="determinate", variable=int_var)
        progress.pack()
        client1 = paramiko.SSHClient()
        int_var.set("10")
        client1.set_missing_host_key_policy(paramiko.WarningPolicy())
        int_var.set("20")

        client1.connect(""+IP_val+"", username=""+User_val+"", password=""+Password_val+"")
        int_var.set("30")

        stdin, stdout, stderr = client1.exec_command('ps')
        int_var.set("40")

        for client1 in stdout:
            if not client1:
                int_var.set("100")
                mb.showinfo("エラー", "サーバー”"+IP_val+"”に接続できませんでした。ネットワークに接続されていないか、IPアドレスが違う可能性があります。")

            else:
                int_var.set("50")
                dt_now=datetime.datetime.now()

                shousai_frame=tk.Frame(root)
                shousai_frame.pack(anchor=tk.NE)
                setsumei=tk.Label(shousai_frame, text="詳細一覧")
                IP_shousai=tk.Label(shousai_frame, text="サーバーIP:"+IP_val+"")
                User_shousai=tk.Label(shousai_frame, text="ユーザー名:"+User_val+"")
                Password_shousai=tk.Label(shousai_frame, text="パスワード:"+Password_val+"")
                time_shousai=tk.Label(shousai_frame, text=(dt_now.strftime('%Y年%m月%d日　%H:%M:%S秒取得')))
                setsumei.pack()
                IP_shousai.pack()
                User_shousai.pack()
                Password_shousai.pack()
                time_shousai.pack()
                int_var.set("60")

                kekka_fuka_process=tk.Label(fuka_frame, text=""+client1+"")
                kekka_fuka_process.pack(padx=5, pady=5, anchor=tk.SW)
                int_var.set("70")

                client2 = paramiko.SSHClient()
                client2.set_missing_host_key_policy(paramiko.WarningPolicy())
                client2.connect(""+IP_val+"", username=""+User_val+"", password=""+Password_val+"")
                int_var.set("80")

                stdin, stdout, stderr = client2.exec_command('free -g')
                for client2 in stdout:

                    int_var.set("90")
                    kekka_fuka_memory=tk.Label(fuka_frame, text=""+client2+"")
                    kekka_fuka_memory.pack(padx=5, pady=5, anchor=tk.SW)
                    int_var.set("100")

                    if int_var == "100":
                        sub.destroy()

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
