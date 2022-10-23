import tkinter as tk
import tkinter.ttk as ttk
from sshtunnel import SSHTunnelForwarder
import MySQLdb as mydb
import re
from tkinter import messagebox as mb

root=tk.Tk()
root.geometry("700x200")
root.resizable(height=False, width=False)
root.title("駅の電光掲示板シミュレータ")

var_label_1_for=tk.StringVar()
var_label_1_for.set("行先表示")
var_label_2_for=tk.StringVar()
var_label_2_for.set("行先表示")
var_label_time_1=tk.StringVar(value=" 9:37")
var_label_time_2=tk.StringVar(value=" 9:43")

time_hour_no1str=tk.IntVar()
time_min_no1str=tk.IntVar()
time_hour_no2str=tk.IntVar()
time_min_no2str=tk.IntVar()
item = tk.StringVar()
kari_var = tk.StringVar()

var_label_1_for_system=tk.StringVar()

def shutoku():
    var_label_1_for.set(cmb_for_1.get())
    var_label_2_for.set(cmb_for_2.get())
    var_label_time_1.set(time_hour_no1.get())
    var_label_time_2.set(time_hour_no2.get())

    with SSHTunnelForwarder(
    ("raspberrypi", 22),
    ssh_username = "pi",
    ssh_password = "ray123",
    ssh_pkey = None,
    remote_bind_address=("localhost", 3306)
    ) as server:
        conn = mydb.connect(host = '127.0.0.1',
                          port = server.local_bind_port,
                          user = "root",
                          passwd = "ray123",
                          db = "for_station",
                          charset = 'utf8')

        cursor = conn.cursor()
        cursor.execute("SELECT 行先 FROM MatonakaLine_for;")
        rows = cursor.fetchall()
        conn.close()
        for rows in item:
            kari_var = item[0]
            print(kari_var)
        for kari_var in var_label_1_for:
            var_label_1_for.set(kari_var)
            print("処理完了")

system_menu=tk.Toplevel()
system_menu.geometry("600x600")
system_menu.resizable(height=False, width=False)
system_menu.title("表示設定")

frameee=tk.Frame(system_menu)
frameee.pack()
frameee2=tk.Frame(system_menu)
frameee2.pack()
cmb_for_select_1=('各停　中　村', '各停　橋　本', '臨時　列　車')
cmb_for_1=ttk.Combobox(system_menu, values=cmb_for_select_1, width=20)
cmb_for_1.pack(side=tk.LEFT, padx=5)
cmb_for_select_2=('各停　中　村', '各停　橋　本', '臨時　列　車')
cmb_for_2=ttk.Combobox(system_menu, values=cmb_for_select_2, width=20)
cmb_for_2.pack(side=tk.LEFT, padx=5)
time_hour_no1=ttk.Entry(frameee)
time_hour_no1.pack(side=tk.LEFT, padx=5, pady=5)
time_hour_no1.insert(0, "時刻入力")
time_hour_no2=ttk.Entry(frameee2)
time_hour_no2.pack(side=tk.LEFT, padx=5, pady=10)
time_hour_no2.insert(0, "時刻入力")
ok_button=tk.Button(system_menu, text="決定", command=shutoku)
ok_button.pack(side=tk.LEFT, padx=5)

frame_1danme=tk.Frame(pady=5, padx=5, relief=tk.RAISED, bg="black")
label_1_time=tk.Label(frame_1danme, textvariable=var_label_time_1, font=("JFドットKappa20 Regular",60), fg="lightgreen", bg="black")
label_1_for=tk.Label(frame_1danme, textvariable=var_label_1_for, font=("JFドットKappa20 Regular",60), fg="orange", bg="black")
frame_2danme=tk.Frame(pady=5, padx=5, relief=tk.RAISED, bg="black")
label_2_time=tk.Label(frame_2danme, textvariable=var_label_time_2, font=("JFドットKappa20 Regular",60), fg="lightgreen", bg="black")
label_2_for=tk.Label(frame_2danme, textvariable=var_label_2_for, font=("JFドットKappa20 Regular",60), fg="orange", bg="black")
frame_1danme.pack(fill=tk.X)
label_1_time.pack(side=tk.LEFT)
label_1_for.pack(side=tk.LEFT, padx=5)
frame_2danme.pack(fill=tk.X)
label_2_time.pack(side=tk.LEFT)
label_2_for.pack(side=tk.LEFT, padx=5)

root.configure(bg="black")
root.mainloop()
