import tkinter as tk
from tkinter import filedialog
import pygame
import os

# Create the main window
window = tk.Tk()
window.title("Music Player")

# Initialize Pygame mixer
pygame.init()

# Function to select and play a music file
def play_music():
    file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3")])
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

# Function to stop the music
def stop_music():
    pygame.mixer.music.stop()

# Function to load and display a playlist
def load_playlist():
    playlist = filedialog.askdirectory()
    if playlist:
        os.chdir(playlist)
        files = os.listdir(playlist)
        for file in files:
            if file.endswith(".mp3"):
                playlist_box.insert(tk.END, file)

# Add a button to select and play music
play_button = tk.Button(window, text="Play Music", command=play_music)
play_button.pack()

# Add a button to stop the music
stop_button = tk.Button(window, text="Stop Music", command=stop_music)
stop_button.pack()

# Add a playlist box to display loaded songs
playlist_box = tk.Listbox(window)
playlist_box.pack()

# Add a button to load a playlist
load_button = tk.Button(window, text="Load Playlist", command=load_playlist)
load_button.pack()

# Start the main event loop
window.mainloop()
