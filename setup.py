import os
def setup():
    require = ["ffmpeg", "yt_dlp", "youtube-search-python"]
    for i in require:
        if os.system(f"pip show {i} > /dev/null 2>&1") == 0:
            print(f"Found install {i}")
        else:
            print(f"Unable to find a install for {i}, Download? (y/n)")
            des = input()
            if des == "y":
                os.system(f"pip install {i}")
            else:
                print("terminating program... Reason : Unable to download required resources.")
    print("All installation done (or) availible. Get started with ytd.py")
setup()
