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

pageurl = input('Podaj URL strony internetowej: ')
date1 = input("Podaj pierwsza date (rrrrmmdd): ")
date2 = input("Podaj pierwsza druga (rrrrmmdd): ")
date3 = input("Podaj pierwsza trzecia (rrrrmmdd): ")

url1 ="http://archive.org/wayback/available?url="+pageurl+"&timestamp="+str(date1)
url2 ="http://archive.org/wayback/available?url="+pageurl+"&timestamp="+str(date2)
url3 ="http://archive.org/wayback/available?url="+pageurl+"&timestamp="+str(date3)

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