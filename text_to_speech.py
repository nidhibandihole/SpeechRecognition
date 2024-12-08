#importing libraries

from tkinter import*
from gtts import gTTS
from playsound import playsound

root = Tk()
root.geometry("400x400")
root.configure(bg = '#FFDAB9')
root.title("text to speech")

msg = StringVar()
Label(root,text = "enter the text : ",font = ('Arial',20),fg = 'black').place(x=20,y=60)
input = Entry(root,textvariable = msg,width = '100')
input.place(x=10,y=100)

def Text_to_Speech():
    message = input.get()
    speech = gTTS(text = message)
    speech.save("sound.mp4")
    playsound("sound.mp4")

def exit():
    root.destroy()

Button(root,text = "PLAY" , font = ('arialblack 15 bold'),command =Text_to_Speech,width='4').place(x=25,y=140)
Button(root,font = 'arialblack 15 bold', text = 'EXIT', width = '4',command = exit).place(x=100,y=140)

root.mainloop()
