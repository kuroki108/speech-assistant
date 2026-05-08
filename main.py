from listener import listen
from config import WAKE_WORD

from modules import spotify, browser, system

def handle_command(text):
    print("Befehl:", text)

    if "spiele" in text:
        query = text.replace("spiele", "").strip()
        spotify.play(query)

    elif "suche" in text:
        query = text.replace("suche", "").strip()
        browser.search(query)

    elif "spotify öffnen" in text:
        spotify.open_spotify()

    elif "herunterfahren" in text:
        system.shutdown()

    elif "beenden" in text:
        exit()

    else:
        print("Unbekannter Befehl")


while True:
    text = listen()

    if WAKE_WORD in text:
        print("Wake Word erkannt!")

        command = text.replace(WAKE_WORD, "").strip()

        if command:
            handle_command(command)