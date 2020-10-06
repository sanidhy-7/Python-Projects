import tkinter as tk
from PIL import ImageTk,Image
import os

def clear():
    url.delete(first=0,last=0)

def red():
    try:
        url=tk.Entry(box,width=32,font=("Calibri",15),bg="Red",justify="center")
        url.pack(padx=5,pady=5,ipady=10)

    except Exception as e:
        print(e)





def blue():
    try:
        url=tk.Entry(box,width=32,font=("Calibri",15),bg="Blue",justify="center")
        url.pack(padx=5,pady=5,ipady=10)

    except Exception as e:
        print(e)


def green():
    try:
        url=tk.Entry(box,width=32,font=("Calibri",15),bg="Green",justify="center")
        url.pack(padx=5,pady=5,ipady=10)

    except Exception as e:
        print(e)







box=tk.Tk()
box.title("Color changing")
box.geometry("500x600")
box.iconbitmap("youtube_icon.ico")
# width, height = window.winfo_screenwidth(), window.winfo_screenheight()

message = tk.Label(box, text="Change Color", bg="aqua", fg="black", width=25,height=2, font=('times', 15, 'italic bold '))
message.place(x=140, y=100)
message.pack(padx=5,pady=5)
# m = tk.Label(box, text="Enter URL of Video", bg="aqua", fg="black", width=20,height=2, font=('times', 15, 'italic bold '))
# m.pack(padx=5,pady=5)

url=tk.Entry(box,width=32,font=("Calibri",15),justify="center")
url.pack(padx=5,pady=5,ipady=10)


r =tk.Button(box,text="Red",command=red,fg="Red"  ,bg="white"  ,width=15  ,height=2, activebackground = "Red" ,font=('times', 15, ' bold '))

r.pack(padx=5,pady=5)

b = tk.Button(box, text="Blue",command=blue,fg="Black"  ,bg="white"  ,width=10  ,height=1 ,activebackground = "Red" ,font=('times', 15, ' bold '))
b.pack(padx=5,pady=5)

g = tk.Button(box, text="Green",command=green,fg="Black"  ,bg="white"  ,width=10  ,height=1 ,activebackground = "Red" ,font=('times', 15, ' bold '))
g.pack(padx=5,pady=5)

clearButton = tk.Button(box, text="clear",command=clear,fg="Black"  ,bg="white"  ,width=10  ,height=1 ,activebackground = "Red" ,font=('times', 15, ' bold '))
clearButton.pack(padx=5,pady=5)

button_quit =tk.Button(box,text="Exit",font=("verdana",20),relief='ridge',command=box.quit,fg="Black"  ,bg="white"  ,width=10  ,height=1 ,activebackground = "Red" )
button_quit.pack(padx=5,pady=5)




box.mainloop()