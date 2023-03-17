# from playsound import playsound
# playsound("C:/Users/user/Desktop/yt1s.com.mp3")

# import vlc
# import time
#
# p = vlc.MediaPlayer("C:/Users/user/Desktop/yt1s.com.mp3")
# p.play()
# time.sleep(40)

import webbrowser
import requests

pageurl1 = input('Podaj pierwszy URL strony internetowej: ')
date1 = input("Podaj date: ")
pageurl2 = input('Podaj drugi URL strony internetowej: ')
date2 = input("Podaj date: ")
pageurl3 = input('Podaj trzeci URL strony internetowej: ')
date3 = input("Podaj date: ")

url1 ="http://archive.org/wayback/available?url="+pageurl1+"&timestamp="+str(date1)
url2 ="http://archive.org/wayback/available?url="+pageurl2+"&timestamp="+str(date2)
url3 ="http://archive.org/wayback/available?url="+pageurl3+"&timestamp="+str(date3)

response = requests.get(url1)
d = response.json()
page = d["archived_snapshots"]["closest"]["url"]
webbrowser.open(page)

response = requests.get(url2)
d = response.json()
page = d["archived_snapshots"]["closest"]["url"]
webbrowser.open(page)

response = requests.get(url3)
d = response.json()
page = d["archived_snapshots"]["closest"]["url"]
webbrowser.open(page)