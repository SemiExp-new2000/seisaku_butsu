import tkinter as tk
import tkinter.ttk as ttk
import tkinter.font as tkfont
from tkinter import messagebox as mb

root=tk.Tk()
root.geometry("820x100")
root.resizable(height=False, width=False)
root.title("駅の電光掲示板シミュレータ")

str=tk.StringVar(value=1)

font = tkfont.Font(family="JFドットKappa20 Regular", size=60)

def fontsizechange30():
    font.configure(family="JFドットKappa20 Regular", size=50)

def fontsizechange60():
    font.configure(family="JFドットKappa20 Regular", size=60)

def Hashimoto_Nakamura():

    str=cmb.get()

    if str == "1":
        root.after(1, lambda: var_label_2_for.set("ただいま"))
        root.after(1, lambda: var_label_1_for.set("橋　　本"))
        root.after(3000, lambda: var_label_2_for.set("Current"))
        root.after(3000, lambda: var_label_1_for.set("Hashimoto"))
        root.after(6000, Hashimoto_Nakamura)

    elif str == "2":
        root.after(1, fontsizechange60)
        root.after(1, lambda: var_label_2_for.set("　次は　"))
        root.after(1, lambda: var_label_1_for.set("橋 本 園"))
        root.after(3000, lambda: var_label_2_for.set("　Next"))
        root.after(3000, lambda: var_label_1_for.set("Hashimotoen"))
        root.after(6000, fontsizechange30)
        root.after(6000, lambda: var_label_2_for.set("　次は　"))
        root.after(6000, lambda: var_label_1_for.set("ハシモトエン"))
        root.after(9000, Hashimoto_Nakamura)

    elif str == "3":
        root.after(1, fontsizechange60)
        root.after(1, lambda: var_label_2_for.set("まもなく"))
        root.after(1, lambda: var_label_1_for.set("橋 本 園"))
        root.after(3000, lambda: var_label_2_for.set("　Soon"))
        root.after(3000, lambda:var_label_1_for.set("Hashimotoen"))
        root.after(6000, Hashimoto_Nakamura)

    elif str == "4":
        root.after(1, fontsizechange60)
        root.after(1, lambda: var_label_2_for.set("ただいま"))
        root.after(1, lambda: var_label_1_for.set("橋 本 園"))
        root.after(3000, lambda: var_label_2_for.set("Current"))
        root.after(3000, lambda: var_label_1_for.set("Hashimotoen"))
        root.after(6000, Hashimoto_Nakamura)

    elif str == "5":
        root.after(1, fontsizechange60)
        root.after(1, lambda: var_label_2_for.set("まもなく"))
        root.after(1, lambda: var_label_1_for.set("終点中村"))
        root.after(3000, lambda: var_label_2_for.set("　Soon"))
        root.after(3000, lambda:var_label_1_for.set("Nakamura"))
        root.after(6000, Hashimoto_Nakamura)

    elif str =="6":
        root.after(1, fontsizechange60)
        root.after(1, lambda: var_label_2_for.set("ただいま"))
        root.after(1, lambda: var_label_1_for.set("終点中村"))
        root.after(3000, lambda: var_label_2_for.set("Current"))
        root.after(3000, lambda: var_label_1_for.set("Nakamura"))
        root.after(6000, Hashimoto_Nakamura)

    else:
        root.after(1, fontsizechange60)
        root.after(1, lambda: var_label_2_for.set("ただいま"))
        root.after(1, lambda: var_label_1_for.set("終点中村"))
        return

def Nakamura_Hashimoto():
    str=cmb.get()

    if str == "6":
        root.after(1, fontsizechange60)
        root.after(1, lambda: var_label_2_for.set("ただいま"))
        root.after(1, lambda: var_label_1_for.set("中　　村"))
        root.after(3000, lambda: var_label_2_for.set("Current"))
        root.after(3000, lambda: var_label_1_for.set("Nakamura"))
        root.after(6000, lambda: var_label_2_for.set("この電車は"))
        root.after(6000, lambda: var_label_1_for.set("橋本ゆき"))
        root.after(9000, fontsizechange30)
        root.after(9000, lambda: var_label_2_for.set("This Train For"))
        root.after(9000, lambda: var_label_1_for.set("Hashimoto"))
        root.after(12000, Nakamura_Hashimoto)

    elif str == "5":
        root.after(1, fontsizechange60)
        root.after(1, lambda: var_label_2_for.set("まもなく"))
        root.after(1, lambda: var_label_1_for.set("橋 本 園"))
        root.after(3000, lambda: var_label_2_for.set("　Soon"))
        root.after(3000, lambda:var_label_1_for.set("Hashimotoen"))
        root.after(6000, Nakamura_Hashimoto)

    elif str == "4":
        root.after(1, fontsizechange60)
        root.after(1, lambda: var_label_2_for.set("ただいま"))
        root.after(1, lambda: var_label_1_for.set("橋 本 園"))
        root.after(3000, lambda: var_label_2_for.set("Current"))
        root.after(3000, lambda: var_label_1_for.set("Hashimotoen"))
        root.after(6000, lambda: var_label_2_for.set("この電車は"))
        root.after(6000, lambda: var_label_1_for.set("橋本ゆき"))
        root.after(9000, fontsizechange30)
        root.after(9000, lambda: var_label_2_for.set("This Train For"))
        root.after(9000, lambda: var_label_1_for.set("Hashimoto"))
        root.after(12000, Nakamura_Hashimoto)

    elif str == "3":
        root.after(1, fontsizechange60)
        root.after(1, lambda: var_label_2_for.set("　次は　"))
        root.after(1, lambda: var_label_1_for.set("終点橋本"))
        root.after(3000, lambda: var_label_2_for.set("　Next"))
        root.after(3000, lambda: var_label_1_for.set("Hashimoto"))
        root.after(6000, fontsizechange30)
        root.after(6000, lambda: var_label_2_for.set("　次は　"))
        root.after(6000, lambda: var_label_1_for.set("ハシモト"))
        root.after(9000, Nakamura_Hashimoto)


    elif str == "2":
        root.after(1, fontsizechange60)
        root.after(1, lambda: var_label_2_for.set("まもなく"))
        root.after(1, lambda: var_label_1_for.set("終点橋本"))
        root.after(3000, lambda: var_label_2_for.set("　Soon"))
        root.after(3000, lambda:var_label_1_for.set("Hashimoto"))
        root.after(6000, Nakamura_Hashimoto)

    elif str == "1":
        root.after(1, fontsizechange60)
        root.after(1, lambda: var_label_2_for.set("ただいま"))
        root.after(1, lambda: var_label_1_for.set("終点橋本"))
        root.after(3000, lambda: var_label_2_for.set("Current"))
        root.after(3000, lambda: var_label_1_for.set("Hashimoto"))
        root.after(6000, lambda: var_label_2_for.set("ただいま"))
        root.after(6000, lambda: var_label_1_for.set("終点橋本"))
        root.after(9000, lambda: var_label_2_for.set("Current"))
        root.after(9000, lambda: var_label_1_for.set("Hashimoto"))
        root.after(12000, lambda: var_label_2_for.set("この電車は"))
        root.after(12000, lambda: var_label_1_for.set("橋本ゆき"))
        root.after(12000, fontsizechange30)
        root.after(15000, lambda: var_label_2_for.set("This Train For"))
        root.after(15000, lambda: var_label_1_for.set("Hashimoto"))
        root.after(18000, lambda: var_label_2_for.set("ただいま"))
        root.after(18000, lambda: var_label_1_for.set("終点橋本"))
        return


var_label_1_for=tk.StringVar()
var_label_1_for.set("行先表示")
var_label_2_for=tk.StringVar()
var_label_2_for.set("次駅/接近")

system_menu=tk.Toplevel()
system_menu.geometry("350x30")
system_menu.resizable(height=False, width=False)
system_menu.title("表示設定")

button1=tk.Button(system_menu, text="1401", command=Hashimoto_Nakamura)
button1.pack(side=tk.LEFT, pady=5)
button2=tk.Button(system_menu, text="1405", command=Nakamura_Hashimoto)
button2.pack(side=tk.LEFT, pady=5)
cmb=ttk.Spinbox(system_menu, textvariable=str, from_=0, to=7, increment=1)
cmb.pack(side=tk.LEFT, pady=5)

frame_1danme=tk.Frame(pady=5, padx=5, relief=tk.RAISED, bg="black")
label_1_kinds=tk.Label(frame_1danme, textvariable=var_label_2_for, font=font, fg="orange", bg="black")
label_1_for=tk.Label(frame_1danme, textvariable=var_label_1_for, font=font, fg="lightgreen", bg="black")
frame_1danme.pack(fill=tk.X)
label_1_kinds.pack(side=tk.LEFT, padx=5)
label_1_for.pack(side=tk.LEFT, padx=5)

root.configure(bg="black")
root.mainloop()
