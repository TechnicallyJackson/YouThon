# Import the goodies
import tkinter, customtkinter, time, os
from pytube import YouTube
print("Imported tkinter, customtkinter, os, time, and YouTube (from pytube)")

# Download Functions
def downloadMP4Start():
    try:
        print("MP4 Button Pressed")
        ytLink = link.get()
        ytObj = YouTube(ytLink)
        video = ytObj.streams.get_highest_resolution()
        video.download()
    except:
        print("Link Invalid!")
def downloadMP3Start():
    try:    
        print("MP3 Button Pressed")
        ytLink = link.get()
        ytObj = YouTube(ytLink)
        audio = ytObj.streams.get_audio_only()
        audio.download()
        print("Change file extention to mp3 if not invalid")
    except:
        print("Invalid Link")

# System settings
customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("green")
print("Set system settings")

# The app window
app = customtkinter.CTk()
app.geometry("720x480")
app.title("YouThon Downloader")
print("Made window")

#UI Elements
title = customtkinter.CTkLabel(app, text="YouThon Downloader")
title.pack(padx=10, pady=10)
title = customtkinter.CTkLabel(app, text="Files will download without Success information :(")
title.pack(padx=10, pady=10)
print("Made Label")

# input 
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack()
print("Made link input")

# Party on!
downloadMP4 = customtkinter.CTkButton(app, text="Download MP4", command=downloadMP4Start)
downloadMP3 = customtkinter.CTkButton(app, text="Download MP3", command=downloadMP3Start)
downloadMP3.pack(padx=10, pady=10)
downloadMP4.pack(padx=10, pady=10)
print("Made Buttons")

# Lets run it!
print("Starting...")
time.sleep(0.5)
app.mainloop()
