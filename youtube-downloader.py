from tkinter import *
from tkinter import ttk
from pytube import YouTube

def download(*args):
    
    yt = YouTube(url.get())
    ytvideodownload = yt.streams.get_highest_resolution()
    ytvideodownload.download("./downloads/")
    print('Video ladattu.')



root = Tk()
root.title("Youtube downloader")
frm = ttk.Frame(root, padding=10)
frm.grid()

url=StringVar()
url_entry = ttk.Entry(frm, textvariable=url, width=60).grid(column=1, row=0)
ttk.Label(frm, text="Enter Url: ").grid(column=0, row=0)
ttk.Button(frm, text="Download", command=download).grid(column=2, row=0)

ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=1)
root.mainloop()