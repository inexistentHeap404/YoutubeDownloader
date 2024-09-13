## Imports ##

import tkinter as tk
import ttkbootstrap as ttk
from youtubesearchpython import *
import yt_dlp as dl
from os import system
from os import listdir

## Download functions ##
def Download():
    video_name_display_var.set(video_name_entry_string.get())
    video_name = video_name_entry_string.get()
    video_type = video_type_variable.get()
    print(video_type)
    ald = False
    directory = [j.lower() for j in listdir()]
    for k in directory:
        if video_name in k:
            ald = True
            video_download_status_var.set("Downlod Failed: given file already exists in the directory")
            return None
    y = {}
    sr = VideosSearch(video_name, limit = 1).result()
    val = [j for j in sr.values()]
    link = val[0][0].get("link")
    title = val[0][0].get("title")
    code = val[0][0].get("id")
    if video_type == "0":
        downloadmp3(video_name, link)
    else:
        downloadmp4(video_name, link)

def downloadmp3(video_name, link):
    video_download_status_var.set("Download in progress")
    system("python3 -m yt_dlp -x " + link + " --audio-format mp3 --audio-quality 0")
    status = system("echo $?")
    if status == 0:
        video_download_status_var.set("mp3 Download of video " + video_name + " is successful")
    else:
        video_download_status_var.set("Download Failed: Unable to download video, try running the script setup.py and try again")
def downloadmp4(video_name, link):
    video_download_status_var.set("Download in progress")
    system("python3 -m yt_dlp --merge-output-format mp4 -f 137+bestaudio " + link)
    status = system("echo $?")
    if status == 0:
        video_download_status_var.set("mp4 Download of video " + video_name + " is successful")
    else:
        video_download_status_var.set("Download Failed: Unable to download video, try running the script setup.py and try again")



## YTD SCREEN ##
window = ttk.Window(themename = "darkly")
window.title("Youtube Downloader")
window.geometry("1000x700")


## Title Label ##
title_label = ttk.Label(
        master = window,
        text = "Youtube Downloader",
        font = "Calibri 30 bold"
        )
title_label.pack(
        pady = 20
        )

## Video Name input frame field and button ##
input_frame = ttk.Frame(
        master = window
        )
video_name_entry_string = tk.StringVar()
video_entry = ttk.Entry(
        master = input_frame,
        textvariable = video_name_entry_string
        )
video_type_variable = tk.StringVar()
video_type_values = {
        "mp3" : "0",
        "mp4" : "1"
        }
for (text, value) in video_type_values.items():
    tk.Radiobutton(
            master = window, 
            text = text,
            variable = video_type_variable,
            value = value
            ).pack(pady = 5, padx = 10)
video_submit_button = ttk.Button(
        master = input_frame, 
        text = "Download",
        command = Download
        )
video_entry.pack(
        side = "left", 
        padx = 10
        )
video_submit_button.pack(
        side = "left", 
        padx = 10
        )
input_frame.pack()

## video name display ##
video_name_display_var = tk.StringVar()
video_name_display = ttk.Label(
        master = window,
        text = "Video Name",
        font = "Calibri 20",
        textvariable = video_name_display_var
        )
video_name_display.pack(
        pady = 20
        )


## video download status display ##
video_download_status_var = tk.StringVar()
video_download_status_display = ttk.Label(
        master = window, 
        text = "Video Download status",
        font = "Calibri 22 bold",
        textvariable = video_download_status_var
        )
video_download_status_display.pack(
        pady = 40
        )

## mainloop ##
window.mainloop()
