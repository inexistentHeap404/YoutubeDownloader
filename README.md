# YoutubeDownloader
Just a terminal way of downloading Youtube Vids on mp3.

Requirements:
modules:
  yt_dlp
  youtube-search-python
  ffmpeg

# Installation
```
$ use the classic git clone
$ sudo python3 setup.py
```

# Run
V1
```
cd YoutubeDownloader
$ python3 ytd.py
How many songs to download?
2
Enter song name separated by a whitespace...
Enter song name 1 blinding lights
Enter song name 2 7 rings
[youtube] Extracting URL: https://www.youtube.com/watch?v=4NRXx6U8ABQ
[youtube] 4NRXx6U8ABQ: Downloading webpage
[youtube] 4NRXx6U8ABQ: Downloading ios player API JSON
[youtube] 4NRXx6U8ABQ: Downloading player d60b0ef9
[youtube] 4NRXx6U8ABQ: Downloading m3u8 information
[info] 4NRXx6U8ABQ: Downloading 1 format(s): 251
[download] Destination: The Weeknd - Blinding Lights (Official Video) [4NRXx6U8ABQ].webm
[download] 100% of    3.91MiB in 00:00:18 at 222.00KiB/s
[ExtractAudio] Destination: The Weeknd - Blinding Lights (Official Video) [4NRXx6U8ABQ].mp3
Deleting original file The Weeknd - Blinding Lights (Official Video) [4NRXx6U8ABQ].webm (pass -k to keep)
[youtube] Extracting URL: https://www.youtube.com/watch?v=QYh6mYIJG2Y
[youtube] QYh6mYIJG2Y: Downloading webpage
[youtube] QYh6mYIJG2Y: Downloading ios player API JSON
[youtube] QYh6mYIJG2Y: Downloading m3u8 information
[info] QYh6mYIJG2Y: Downloading 1 format(s): 251
[download] Destination: Ariana Grande - 7 rings (Official Video) [QYh6mYIJG2Y].webm
[download] 100% of    2.92MiB in 00:00:20 at 147.86KiB/s
[ExtractAudio] Destination: Ariana Grande - 7 rings (Official Video) [QYh6mYIJG2Y].mp3
Deleting original file Ariana Grande - 7 rings (Official Video) [QYh6mYIJG2Y].webm (pass -k to keep)
continue (y/n)
n
```


The previous version needed the user to specify the number of songs to download, but in this version you just keep entering songs until you run out of songs to keep in your playlist and when you wish to end just press enter.

The next update might feature a GUI.

# GUI update

```
Additional Requirements:
Tkkinter, ttkbootstrap
```
## Run is as an App in you Linux machine
```
Feature coming soon!!
```

Here's the next Update, This update features a Tkinter GUI with ttkbootstrap plugin for a more morden Tkinter Experience.
Enter the Video name and the path to install it and it does it.



