import tkinter as tk
import os
import webbrowser
import subprocess
import pygame

# Initialize Pygame mixer
pygame.mixer.init()

#Functions
def darkrun():
    subprocess.Popen(['python', './apps/DARKARMY.py'])

def dkjr():
    subprocess.Popen(['python', './apps/Jarvis.py'])
    pygame.mixer.music.pause()

def ddos():
    subprocess.Popen(['python', './apps/ddos.py'])

def setup():
    subprocess.Popen(['python', './Setup/setup.py'])

def open_telegram_channel():
    webbrowser.open_new(r'https://t.me/yourchannel')

def play_music():
    pygame.mixer.init()
    pygame.mixer.music.load('title.mp3')
    pygame.mixer.music.play(-1)

root = tk.Tk()
root.title("FHDEREN")

# Add background image
bg_image = tk.PhotoImage(file='bg.png')  # Replace with your image file
bg_label = tk.Label(root, image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

def pause_music():
    if pygame.mixer.music.get_busy():
        pygame.mixer.music.pause()
    else:
        pygame.mixer.music.unpause()

play_music()

# Create a banner
banner = tk.Label(root, text=""" ███████╗██╗░░██╗██████╗░███████╗██████╗░███████╗███╗░░██╗
    ██╔════╝██║░░██║██╔══██╗██╔════╝██╔══██╗██╔════╝████╗░██║
    █████╗░░███████║██║░░██║█████╗░░██████╔╝█████╗░░██╔██╗██║
    ██╔══╝░░██╔══██║██║░░██║██╔══╝░░██╔══██╗██╔══╝░░██║╚████║
    ██║░░░░░██║░░██║██████╔╝███████╗██║░░██║███████╗██║░╚███║
    ╚═╝░░░░░╚═╝░░╚═╝╚═════╝░╚══════╝╚═╝░░╚═╝╚══════╝╚═╝░░╚══╝""")
banner.pack()

button3 = tk.Button(root, text="Setup (INSTALL REQUIRED ITEMS)", command=setup)
button3.pack()

button1 = tk.Button(root, text="DARKARMY TOOLKIT", command=darkrun)
button1.pack()

button2 = tk.Button(root, text="Dark Jarvis", command=dkjr)
button2.pack()

button3 = tk.Button(root, text="DDOS", command=ddos)
button3.pack()

telegram_button = tk.Button(root, text="Join our Telegram Channel", command=open_telegram_channel)
telegram_button.pack(side='top')

credit = tk.Label(root, text="Made with ❤️ by @hxckxe & @Spide_dev", font=("Helvetica", 16))
credit.pack(side='bottom')

music_credit = tk.Label(root, text="Music = Smoke ft. JOEHDAH", font=("Helvetica", 10))
music_credit.pack(side='bottom')

# Add Pause/Resume button with an icon
pause_icon = tk.PhotoImage(file='pause_icon.png')  # replace with your pause icon file
pause_button = tk.Button(root, image=pause_icon, command=pause_music)
pause_button.image = pause_icon  # keep a reference to the image object
pause_button.pack(side='right')  # place the button at the right side of the window

root.mainloop()
