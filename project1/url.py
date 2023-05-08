import pyperclip
import pyshorteners
from tkinter import *

root = Tk()
root.geometry("600x400")
root.title("URL shortener")
root.configure(bg="blue")
url = StringVar()
url_address = StringVar()


def urlshortener():
    long_urladdress = url.get()
    shortened_urladd = pyshorteners.Shortener().tinyurl.short(long_urladdress)
    url_address.set(shortened_urladd)


def copyurl():
    url_short = url_address.get()
    pyperclip.copy(url_short)


Label(root, text="Url Shortener", font="poppins").pack(pady=10)
Entry(root, textvariable=url).pack(pady=5)
Button(root, text="Shortern", command=urlshortener).pack(pady=7)
Entry(root, textvariable=url_address).pack(pady=5)
Button(root, text="Copy", command=copyurl).pack(pady=5)
root.mainloop()
