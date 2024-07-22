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
def dlod(s,sn):
    if sn == 1:
        y = {}
        sr = VideosSearch(str(s), limit = 1).result()
        val = [i for i in sr.values()]
        link = val[0][0].get("link")
        cwrite("python3 -m yt_dlp -x " + link + " --audio-format mp3 --audio-quality 0")
    else:
        for i in slis:
            y = {}
            sr = VideosSearch(str(i), limit = 1).result()
            val = [j for j in sr.values()]
            link = val[0][0].get("link")
            cwrite("python3 -m yt_dlp -x " + link + " --audio-format mp3 --audio-quality 0")
def start():
    print("How many songs to download?")
    num = int(input())
    if num != 0 and num == 1:
        print("song name : ")
        song = input()
        dlod(song,1)
    else:
        print("Enter song name separated by a whitespace...")
        global slis
        slis = []
        for i in range(num):
            slis.append(input(f"Enter song name {i + 1}"))
        dlod(slis, num)
    print("continue (y/n)")
    des = input()
    if des.lower() == "y":
        start()
    else:
        return None
start()
