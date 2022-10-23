import tkinter as tk
import datetime
import requests
from bs4 import BeautifulSoup
import sys
import os
import re

def get_icon_path(relative_path):
    try:
        # 一時フォルダのパスを取得
        base_path = sys._MEIPASS
    except Exception:
        # 一時フォルダパスを取得できない場合は実行階層パスを取得
        base_path = os.path.abspath(os.path.dirname(sys.argv[0]))

    # アイコンファイルの絶対パスを作成
    return os.path.join(base_path, relative_path)

root=tk.Tk()
root.title("現在時刻")
root.geometry("400x200")
root.iconbitmap(default=get_icon_path('icon.ico'))
root.resizable(height=False, width=False)

str=tk.StringVar()
str.set("初期表示")
str_news=tk.StringVar()
str_news.set("初期表示")
str_shutoku=tk.StringVar()
str_shutoku.set("初期表示")

def news():
    # ヤフーニュースのトップページ情報を取得する
    URL = "https://www.yahoo.co.jp/"
    rest = requests.get(URL)

    #BeautifulSoupにヤフーニュースのページ内容を読み込ませる
    soup = BeautifulSoup(rest.text, "html.parser")

    # ヤフーニュースの見出しとURLの情報を取得して出力する
    data_list = soup.find_all(href=re.compile("news.yahoo.co.jp/pickup"))
    for data in data_list:
        str_news.set(data.span.string)
        dt_nows=datetime.datetime.now()
        str_shutoku.set(dt_nows.strftime('%H:%M時点のニュース'))
        root.after(1800000, news)

def time_watch():
    dt_now=datetime.datetime.now()
    str.set(dt_now.strftime('%Y年%m月%d日 %H:%M:%S'))
    root.after(1, time_watch)

root.after(1, time_watch)
root.after(1, news)
label=tk.Label(textvariable=str, font=("Arial", 25))
label.pack()
label_news_setsumei=tk.Label(textvariable=str_shutoku, font=("Arial", 20))
label_news_setsumei.pack()
label_news=tk.Label(textvariable=str_news, font=("Arial", 17))
label_news.pack()
label_news_shousai=tk.Label(text="※ニュースは30分ごとに更新されます。\nただし、ネットワークに接続されていない場合、表示されません。")
label_news_shousai.pack(anchor=tk.SE)
root.mainloop()
