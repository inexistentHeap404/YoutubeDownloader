from youtubesearchpython import *

y = {}
sr = VideosSearch("Naan naan mahaan", limit = 1).result()
val = [j for j in sr.values()]
print(val[0][0])
