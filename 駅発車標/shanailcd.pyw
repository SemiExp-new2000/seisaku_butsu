import tkinter as tk
from tkinter import ttk as ttk
import datetime
import pygame

root=tk.Tk()
root.geometry("1000x800")
root.title("車内LCD")
root.resizable(height=False, width=False)

kinds=tk.StringVar()
kinds.set("ワンマン")

forsta=tk.StringVar()
forsta.set("中村行")

Next = tk.StringVar()
Next.set("　ただいま")

Next_station = tk.StringVar()
Next_station.set("橋　本")

str_forNakamura = 1
bell_ATC_str = 0
hassha_switch_var = 1

news_title = tk.StringVar()
news_main = tk.StringVar()

next_station_variable=tk.StringVar(value="橋　本")
time=tk.StringVar()
time_consoleng=tk.StringVar()
kinds_console_var=tk.StringVar(value="ワンマン")
forsta_console_var=tk.StringVar(value="中村行")

pygame.mixer.init()

def next_station_stop():
    pygame.mixer.music.load("C:/Users/rei/AppData/自作アプリ/駅発車標/halt.wav")
    pygame.mixer.music.play()

def hassha_melody():
    global hassha_switch_var
    hassha_switch_var = hassha_switch_var +1

    def hassha_melody_off():
        pygame.mixer.music.stop()
        hassha_switch_var = 1
        pygame.mixer.music.load("C:/Users/rei/AppData/自作アプリ/駅発車標/door.wav")
        pygame.mixer.music.play()
        return

    def hassha_melody_on():
        pygame.mixer.music.load("C:/Users/rei/AppData/自作アプリ/駅発車標/siello_2.mid")
        pygame.mixer.music.play()
        if hassha_switch_var == 3:
            hassha_melody_off()
            print("正常な証。")
            print(hassha_switch_var)
            return
        root.after(15000, hassha_melody_on)

    hassha_melody_on()
    return

def ATS():
    global str_forNakamura
    str_forNakamura = str_forNakamura + 1
    pygame.mixer.init()
    pygame.mixer.music.load("C:/Users/rei/AppData/自作アプリ/駅発車標/atcding.wav")
    pygame.mixer.music.play()

def what_time():
    dt_now=datetime.datetime.now()
    time.set(dt_now.strftime('%H:%M'))
    time_consoleng.set(dt_now.strftime('%H:%M:%S'))
    root.after(200, what_time)

def system_forNakamura():
    global str_forNakamura
    str_forNakamura = 1

    def for_Nakamura():
        global str_forNakamura
        kinds_console_var.set("ワンマン")
        forsta_console_var.set("中村行")
        kinds.set("ワンマン")
        forsta.set("中村行")
        root.after(3500, lambda: kinds.set("One man"))
        root.after(3500, lambda: forsta.set("for Nakamura"))

        if str_forNakamura == 1:
            next_sta_console.config(text="停車中:")
            next_station_variable.set("橋　本")
            root.after(1, lambda: Next.set("　ただいま"))
            root.after(1, lambda: Next_station.set("橋　本"))
            root.after(3000, lambda: Next.set("Now Stopping at"))
            root.after(3000, lambda: Next_station.set("Hashimoto"))
            root.after(6000, lambda: Next.set("　ただいま"))
            root.after(6000, lambda: Next_station.set("はしもと"))
            root.after(9000, for_Nakamura)

        elif str_forNakamura == 2:
            next_sta_console.config(text="次　駅:")
            next_station_variable.set("橋本園")
            root.after(1, lambda: Next.set("　次は　"))
            root.after(1, lambda: Next_station.set("橋本園"))
            root.after(3000, lambda: Next.set("　Next"))
            root.after(3000, lambda: Next_station.set("Hashimotoen"))
            root.after(6000, lambda: Next.set("つぎは"))
            root.after(6000, lambda: Next_station.set("はしもとえん"))
            root.after(9000, for_Nakamura)

        elif str_forNakamura == 3:
            next_sta_console.config(text="接近駅:")
            next_station_variable.set("橋本園")
            root.after(1, lambda: Next.set("　まもなく"))
            root.after(1, lambda: Next_station.set("橋本園"))
            root.after(3000, lambda: Next.set("Arving at"))
            root.after(3000, lambda: Next_station.set("Hashimotoen"))
            root.after(6000, lambda: Next.set("　まもなく"))
            root.after(6000, lambda: Next_station.set("はしもとえん"))
            root.after(9000, for_Nakamura)

        elif str_forNakamura == 4:
            next_sta_console.config(text="停車中:")
            next_station_variable.set("橋本園")
            root.after(1, lambda: Next.set("　ただいま"))
            root.after(1, lambda: Next_station.set("橋本園"))
            root.after(3000, lambda: Next.set("Now Stopping at"))
            root.after(3000, lambda: Next_station.set("Hashimotoen"))
            root.after(6000, lambda: Next.set("　ただいま"))
            root.after(6000, lambda: Next_station.set("はしもとえん"))
            root.after(9000, for_Nakamura)

        elif str_forNakamura == 5:
            next_sta_console.config(text="次駅:")
            next_station_variable.set("中　村")
            root.after(1, lambda: Next.set("　次は終点"))
            root.after(1, lambda: Next_station.set("中　村"))
            root.after(3000, lambda: Next.set("　Next"))
            root.after(3000, lambda: Next_station.set("Nakamura ter."))
            root.after(6000, lambda: Next.set("つぎは終点"))
            root.after(6000, lambda: Next_station.set("なかむら"))
            root.after(9000, for_Nakamura)

        elif str_forNakamura == 6:
            next_sta_console.config(text="接近駅:")
            next_station_variable.set("中　村")
            root.after(1, lambda: Next.set("　まもなく終点"))
            root.after(1, lambda: Next_station.set("中　村"))
            root.after(3000, lambda: Next.set("Arving at"))
            root.after(3000, lambda: Next_station.set("Nakamura ter."))
            root.after(6000, lambda: Next.set("　まもなく終点"))
            root.after(6000, lambda: Next_station.set("なかむら"))
            root.after(9000, for_Nakamura)

        elif str_forNakamura == 7:
            next_sta_console.config(text="停車中:")
            next_station_variable.set("中　村")
            kinds_console_var.set("ワンマン")
            forsta_console_var.set("橋本行")
            kinds.set("ワンマン")
            forsta.set("橋本行")
            root.after(3500, lambda: kinds.set("One man"))
            root.after(3500, lambda: forsta.set("for Hashimoto"))
            root.after(1, lambda: Next.set("　ただいま終点"))
            root.after(1, lambda: Next_station.set("中　村"))
            root.after(3000, lambda: Next.set("Now Stopping at"))
            root.after(3000, lambda: Next_station.set("Nakamura"))
            root.after(6000, lambda: Next.set("　ただいま終点"))
            root.after(6000, lambda: Next_station.set("なかむら"))
            return

    for_Nakamura()

def system_forHashimoto():
    global str_forNakamura
    str_forNakamura = 1

    def for_Hashimoto():
        global str_forNakamura
        kinds_console_var.set("ワンマン")
        forsta_console_var.set("橋本行")
        kinds.set("ワンマン")
        forsta.set("橋本行")
        root.after(3500, lambda: kinds.set("One man"))
        root.after(3500, lambda: forsta.set("for Hashimoto"))

        if str_forNakamura == 1:
            next_sta_console.config(text="停車中:")
            next_station_variable.set("中　村")
            root.after(1, lambda: Next.set("　ただいま"))
            root.after(1, lambda: Next_station.set("中　村"))
            root.after(3000, lambda: Next.set("Now Stopping at"))
            root.after(3000, lambda: Next_station.set("Nakamura"))
            root.after(6000, lambda: Next.set("　ただいま"))
            root.after(6000, lambda: Next_station.set("なかむら"))
            root.after(9000, for_Hashimoto)

        elif str_forNakamura == 2:
            next_sta_console.config(text="次駅:")
            next_station_variable.set("橋本園")
            root.after(1, lambda: Next.set("　次は　"))
            root.after(1, lambda: Next_station.set("橋本園"))
            root.after(3000, lambda: Next.set("　Next"))
            root.after(3000, lambda: Next_station.set("Hashimotoen"))
            root.after(6000, lambda: Next.set("つぎは"))
            root.after(6000, lambda: Next_station.set("はしもとえん"))
            root.after(9000, for_Hashimoto)

        elif str_forNakamura == 3:
            next_sta_console.config(text="接近駅:")
            next_station_variable.set("橋本園")
            root.after(1, lambda: Next.set("　まもなく"))
            root.after(1, lambda: Next_station.set("橋本園"))
            root.after(3000, lambda: Next.set("Arving at"))
            root.after(3000, lambda: Next_station.set("Hashimotoen"))
            root.after(6000, lambda: Next.set("　まもなく"))
            root.after(6000, lambda: Next_station.set("はしもとえん"))
            root.after(9000, for_Hashimoto)

        elif str_forNakamura == 4:
            next_sta_console.config(text="接近駅:")
            next_station_variable.set("橋本園")
            root.after(1, lambda: Next.set("　ただいま"))
            root.after(1, lambda: Next_station.set("橋本園"))
            root.after(3000, lambda: Next.set("Now Stopping at"))
            root.after(3000, lambda: Next_station.set("Hashimotoen"))
            root.after(6000, lambda: Next.set("　ただいま"))
            root.after(6000, lambda: Next_station.set("はしもとえん"))
            root.after(9000, for_Hashimoto)

        elif str_forNakamura == 5:
            next_sta_console.config(text="次　駅:")
            next_station_variable.set("橋　本")
            root.after(1, lambda: Next.set("　次は終点"))
            root.after(1, lambda: Next_station.set("橋　本"))
            root.after(3000, lambda: Next.set("　Next"))
            root.after(3000, lambda: Next_station.set("Hashimoto ter."))
            root.after(6000, lambda: Next.set("つぎは終点"))
            root.after(6000, lambda: Next_station.set("はしもと"))
            root.after(9000, for_Hashimoto)

        elif str_forNakamura == 6:
            next_sta_console.config(text="接近駅:")
            next_station_variable.set("橋　本")
            root.after(1, lambda: Next.set("　まもなく終点"))
            root.after(1, lambda: Next_station.set("橋　本"))
            root.after(3000, lambda: Next.set("Arving at"))
            root.after(3000, lambda: Next_station.set("Hashimoto"))
            root.after(6000, lambda: Next.set("　まもなく終点"))
            root.after(6000, lambda: Next_station.set("はしもと"))
            root.after(9000, for_Hashimoto)

        elif str_forNakamura == 7:
            next_station_variable.set("橋　本")
            kinds_console_var.set("ワンマン")
            forsta_console_var.set("中村行")
            kinds.set("ワンマン")
            forsta.set("中村行")
            next_sta_console.config(text="停車中:")
            root.after(3500, lambda: kinds.set("One man"))
            root.after(3500, lambda: forsta.set("for Nakamura"))
            root.after(1, lambda: Next.set("　ただいま終点"))
            root.after(1, lambda: Next_station.set("橋　本"))
            root.after(3000, lambda: Next.set("Now Stopping at"))
            root.after(3000, lambda: Next_station.set("Hashimoto"))
            root.after(6000, lambda: Next.set("　ただいま終点"))
            root.after(6000, lambda: Next_station.set("はしもと"))
            return
    for_Hashimoto()

def get_news():
    news_title.set(entry.get())
    news_main.set(entry_2.get())

frameleft=tk.Frame(root, bg="lightgreen")
frameleft.pack(side=tk.LEFT, anchor=tk.NW)

label_kinds=tk.Label(frameleft, textvariable=kinds, font=("Arial", 40, ), bg="lightgreen")
label_kinds.pack()
label_kinds.config(fg="gray")

label_for=tk.Label(frameleft, textvariable=forsta, font=("Arial", 40), bg="lightgreen")
label_for.pack()

label_time=tk.Label(frameleft, textvariable=time, font=("Arial, 40"), bg="lightgreen")
label_time.pack()

frametopcenter=tk.Frame(root, bg="lightblue")
frametopcenter.pack(side=tk.TOP, anchor=tk.CENTER)

next=tk.Label(frametopcenter, textvariable=Next, font=("Arial, 40"), bg="lightblue")
next.pack()

next_station=tk.Label(frametopcenter, textvariable=Next_station, font=("Arial, 60"), bg="lightblue")
next_station.pack()

shousai_menu = tk.Toplevel()
shousai_menu.geometry("854x480")
shousai_menu.resizable(height=False, width=False)

spinbox_forNakamura=tk.Button(shousai_menu, text="ATC\n 出発/停車時に押下", fg="red", command=ATS)
spinbox_forNakamura.pack(side=tk.LEFT, pady=5, anchor="se")

label=tk.Label(textvariable=news_title,  font=("Arial, 30"))
label.place(x = 300, y = 250)
label_2=tk.Label(textvariable=news_main, font=("Arial, 25"))
label_2.place(x = 200, y = 300)

hasshamelody_switch=tk.Button(shousai_menu, text="発車メロディー\nスイッチON/OFF", command=hassha_melody)
hasshamelody_switch.place(x=50, y=150)

what_time()
frame_top_left_console=tk.Frame(shousai_menu)
frame_top_left_console.pack(side=tk.LEFT)
next_sta_console=tk.Label(shousai_menu, text="停車中:", font=("Arial", 40))
next_sta_console.place(x=50, y=50)
next_sta_station_console=tk.Label(shousai_menu, textvariable=next_station_variable, font=("Arial", 40))
next_sta_station_console.place(x=240, y=50)
time_console = tk.Label(shousai_menu, textvariable=time_consoleng, font=("Arial", 40))
time_console.pack(side=tk.RIGHT, anchor="center")
label_kinds_console=tk.Label(shousai_menu, textvariable=kinds_console_var, font=("Arial", 40))
label_kinds_console.place(x=370, y=400)
label_for_console=tk.Label(shousai_menu, textvariable=forsta_console_var, font=("Arial", 40))
label_for_console.place(x=600, y=400)
entry=tk.Entry(shousai_menu)
entry.pack(anchor="center", side=tk.TOP)

entry_2=tk.Entry(shousai_menu)
entry_2.pack(anchor="center", side=tk.TOP)

button=tk.Button(shousai_menu, text="1401中村行き", command=system_forNakamura)
button.place(x=150, y=440)

button2=tk.Button(shousai_menu, text="1405橋本行き", command=system_forHashimoto)
button2.place(x=250, y=440)

shutoku = tk.Button(shousai_menu, text="文字更新", command=get_news)
shutoku.pack(anchor="ne", side=tk.RIGHT)

root.mainloop()
