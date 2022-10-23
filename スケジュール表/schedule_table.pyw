import tkinter as tk
import tkinter.ttk as ttk
from sshtunnel import SSHTunnelForwarder
import MySQLdb as mydb
from tkinter import messagebox as mb

root = tk.Tk()
root.geometry("854x480")

def schedule():

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


        conn.close()
schedule()
root.mainloop()
