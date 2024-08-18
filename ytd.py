'''
REQ :

-> youtube_search_python module, for installation : windows -> " py -m pip install youtube-search-python "
                                                    linux -> " sudo apt install youtube-search-python "

-> yt_dlp module, for installation : windows -> " py -m pip install yt_dlp"
                                     linux -> " sudo apt install yt_dlp "

-> os module, inbuilt module

-> install or move this file to the location you want to download any song.

'''
from youtubesearchpython import *
import yt_dlp as dl
from os import system as cwrite
from os import getcwd as pwd
from os import listdir  as ls
def dlod(s,sn):
    ald = False
    directory = [j.lower() for j in ls()]
    for i in slis:
        ald = False
        for k in directory:
            if i in k:
                print(f"Song {i} already found in directory skipping {i}")
                ald = True
                break
        if ald:
            pass
        else:
            y = {}
            sr = VideosSearch(str(i), limit = 1).result()
            val = [j for j in sr.values()]
            link = val[0][0].get("link")
            cwrite("python3 -m yt_dlp -x " + link + " --audio-format mp3 --audio-quality 0")
def start():
    print("Enter song names")
    global slis
    slis = []
    i = 1
    while True:
        s_name = input(f"Enter song number {i}: ")
        i += 1
        if s_name == "":
            break
        else:
            slis.append(s_name)
    dlod(slis, len(slis))
    print("continue (y/n)")
    des = input()
    if des.lower() == "y":
        start()
    else:
        return None
start()
