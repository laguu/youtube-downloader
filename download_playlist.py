from pytube import Playlist
import time

#link = input('Anna playlistin URL: ')
link = "https://www.youtube.com/playlist?list=PLKrejdAjvmw6KjSPYoHhw_SQuMJUbtWKt"

yt_playlist = Playlist(link)

for video in yt_playlist.videos:
    try:
        video.streams.get_lowest_resolution().download("./downloads/")
        print("Ladattu: ", video.title)
    except:
        print("Lataus epäonnistui: ", video.title)
    
    time.sleep(0.1)


print('Playlistin lataaminen valmis.')
