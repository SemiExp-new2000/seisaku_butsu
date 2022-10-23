import tkinter as tk

root = tk.Tk()
root.geometry("560x160")
root.title("行先表示器")
root.resizable(height=False, width=False)

kinds=tk.StringVar(value="ワン\n マン")
for_station=tk.StringVar(value="中村\n Nakamura")

def start_Num():
    NumNum=Number.get()
    if NumNum == "1401":
        kinds.set("ワン\n マン")
        label_kinds['fg'] = 'white'
        label_kinds['bg'] = 'green'
        for_station.set("中村\n Nakamura")
        label_for['fg'] = 'white'
        label_for['bg'] = 'black'
    elif NumNum == "1405":
        kinds.set("ワン\n マン")
        label_kinds['fg'] = 'white'
        label_kinds['bg'] = 'green'
        for_station.set("橋本\nHashimoto")
        label_for['fg'] = 'white'
        label_for['bg'] = 'black'
    elif NumNum == "9999":
        kinds.set("　　\n 　　")
        label_kinds['bg'] = 'green'
        for_station.set("回送\nOutOfSer")
        label_for['fg'] = 'white'
        label_for['bg'] = 'black'
    elif NumNum =="0000":
        kinds.set("　　\n 　　")
        label_kinds['bg'] = 'green'
        for_station.set("　臨時\n  Extra")
        label_for['fg'] = 'white'
        label_for['bg'] = 'black'

def command_kinds_OneMan():
    kinds.set("ワン\n マン")
    label_kinds['fg'] = 'white'
    label_kinds['bg'] = 'green'

def command_kinds_Local():
    kinds.set("各駅\n 停車")
    label_kinds['fg'] = 'white'
    label_kinds['bg'] = 'green'

def NoHyoji():
    kinds.set("　　\n 　　")
    label_kinds['bg'] = 'green'

def command_for_Nakamura():
    for_station.set("中村\n Nakamura")
    label_for['fg'] = 'white'
    label_for['bg'] = 'black'

def command_for_Hashimoto():
    for_station.set("橋本\nHashimoto")
    label_for['fg'] = 'white'
    label_for['bg'] = 'black'

frame=tk.Frame(root)
frame.pack(anchor="sw")

label_kinds = tk.Label(frame, textvariable=kinds, font=("JFドットKappa20 Regular",60), fg="white", bg="green")
label_kinds.pack(side=tk.LEFT)
label_for = tk.Label(frame, textvariable=for_station, font=("JFドットKappa20 Regular",60), fg="white", bg="black")
label_for.pack(side=tk.LEFT)

subsc=tk.Toplevel()
subsc.geometry("400x200")
subsc.resizable(height=False, width=False)
kinds_btn_OneMan=tk.Button(subsc, text="ワンマン", command=command_kinds_OneMan)
kinds_btn_OneMan.pack()
kinds_btn_local=tk.Button(subsc, text="各駅停車", command=command_kinds_Local)
kinds_btn_local.pack()
kinds_btn_No=tk.Button(subsc, text="無表示", command=NoHyoji)
kinds_btn_No.pack()
for_btn_Nakamura=tk.Button(subsc, text="中村行き", command=command_for_Nakamura)
for_btn_Nakamura.pack()
for_btn_Hashimoto=tk.Button(subsc, text="橋本行き", command=command_for_Hashimoto)
for_btn_Hashimoto.pack()
Number=tk.Entry(subsc)
Number.pack()
Number.insert(tk.END, u'運用番号')
OK=tk.Button(subsc, text="決定", command=start_Num)
OK.pack()
root.configure(bg='black')
root.mainloop()
