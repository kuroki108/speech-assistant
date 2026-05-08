import webbrowser

def play(query):
    query = query.replace(" ", "%20")
    url = f"https://open.spotify.com/search/{query}"
    webbrowser.open(url)