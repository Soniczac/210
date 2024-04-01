import socket
from threading import Thread
from tkinter import *
from tkinter import ttk
import ftplib
import os
import ntpath #This is used to extract filename from path
import time 

from tkinter import filedialog
from pathlib import Path


from playsound import playsound
import pygame
from pygame import mixer

for file in os.listdir('shared_files'):
    filename = os.filecode(file)
    listbox.insert(song_counter, filename)
    song_counter = song_counter + 1

def play():
    global song_selected
    song_slected = listbox.get(ANCHOR)

    pygame
    mixer.init()
    mixer.music.load('shared_files/' + song_slected)
    mixer.music.play()
    if(song_slected != "") :
        infoLable.configure(text="Now Playing:" +song_slected)
    else:
        infoLable.configure(text="")
    
PlayButton=Button(window,text="play", width=10,bd=1,bg='skyblue',font=(Calibri,10), command = play)
PlayButton.place(x=30,y=200)

def stope():
    global song_selected
    pygame
    mixer.init()
    mixer.music.load('shared_files/'+song_selected)
    mixer.music.pause()
    infoLabel.configure(text="")

    Stop-Button(window.text-"Stop",bd=1,width=10,bg='SkyBlue', font = ("Calibri",10), command = stop)
    Stop.place(x=200, y=200)

