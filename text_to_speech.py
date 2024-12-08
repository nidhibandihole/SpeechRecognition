import speech_recognition as sr
import pyttsx3
import tkinter as tk
from tkinter import messagebox

# Recognizer initialization
r = sr.Recognizer()

# Initialize the pyttsx3 engine
engine = pyttsx3.init()

# Function to convert text to speech
def SpeakText(command):
    engine.say(command)
    engine.runAndWait()

# Function to handle speech recognition and display result
def listen_to_speech():
    try:
        # Use the microphone as source for input
        with sr.Microphone() as source2:
            r.adjust_for_ambient_noise(source2, duration=0.2)  # Adjust for ambient noise
            status_label.config(text="Listening...")
            audio2 = r.listen(source2)  # Using Google to recognize audio
            MyText = r.recognize_google(audio2)
            MyText = MyText.lower()
            print("Did you say: " + MyText)
            result_label.config(text="You said: " + MyText)
            SpeakText(MyText)
            status_label.config(text="Listening completed!")
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
        messagebox.showerror("Error", "Could not request results. Check your internet connection.")
        status_label.config(text="Error occurred.")
    except sr.UnknownValueError:
        print("Speak Again")
        messagebox.showinfo("Unable to Recognize", "Could not understand your speech. Please try again.")
        status_label.config(text="Please speak again.")

# Create the main window
root = tk.Tk()
root.title("Voice User Interface (VUI)")
root.geometry("400x300")

# Label for status
status_label = tk.Label(root, text="Click 'Start Listening' to begin", font=("Arial", 12))
status_label.pack(pady=10)

# Label to display recognized text
result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.pack(pady=10)

# Start listening button
listen_button = tk.Button(root, text="Start Listening", font=("Arial", 12), command=listen_to_speech)
listen_button.pack(pady=20)

# Start the Tkinter event loop
root.mainloop()
