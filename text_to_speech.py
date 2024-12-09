#pip install tkinter
#pip install gTTS
#pip install playsound


from tkinter import *
from gtts import gTTS
from playsound import playsound

root = Tk()
root.geometry("400x400")
root.configure(bg='pink')
root.title("TEXT TO SPEECH")

Msg = StringVar()
Label(root,text ="Your Text Please", font = 'arialblack 15 bold', bg ='white').place(x=20,y=60)
entry_field = Entry(root, textvariable = Msg ,width ='100')
entry_field.place(x=10,y=100)

def Text_to_speech():
    Message = entry_field.get()
    speech = gTTS(text = Message)
    speech.save('sound.mp4')
    playsound('sound.mp4')

def Exit():
    root.destroy()

Button(root, text = "PLAY", font = 'arialblck 15 bold' , command = Text_to_speech ,width = '4').place(x=25,y=140)

Button(root, font = 'arialblack 15 bold',text = 'EXIT', width = '4' , command = Exit).place(x=100 , y = 140)

root.mainloop()


