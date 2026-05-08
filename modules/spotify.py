import os
import subprocess

def open_spotify():
    try:
        os.startfile("spotify")
    except:
        try:
            pass
            #path = r"C:\Users\DEIN_NAME\AppData\Roaming\Spotify\Spotify.exe"
            #subprocess.Popen(path)
        except Exception as e:
            print("Spotify konnte nicht geöffnet werden:", e)



#Spotify API Einbindung
