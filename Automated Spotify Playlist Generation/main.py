import requests,spotipy
from bs4 import BeautifulSoup
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import os

CLIENT_ID=os.getenv("CLIENT_ID")
SECRET=os.getenv("SECRET")
REDIRECT=os.getenv("REDIRECT")
USER_ID=os.getenv("USER_ID")

date=input("Enter the year you wanna travel to? Type the date in this format YYYY-MM-DD:")

header={
    "User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 OPR/122.0.0.0 (Edition std-2)'
}
URL='https://www.billboard.com/charts/hot-100/'+date
response=requests.get(url=URL,headers=header)
response.raise_for_status()

soup=BeautifulSoup(response.text,'html.parser')
title=soup.select('ul li ul li h3')

songs=[item.get_text().strip() for item in title]


with open('Old Songs.txt','w') as file:
    for song in songs:
        file.write(song+'\n')
print('Successful')

sp=spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri=REDIRECT,
        client_id=CLIENT_ID,
        client_secret=SECRET,
        show_dialog=True,
        cache_path="token.txt",
        username='Pranjal Sapkota',
)
)
song_uris=[]
year=date.split('-')[0]
for song in songs:
    result=sp.search(q=f"track:{song} year:{year}",type='track')
    print(result)
    try:
        uri=result['tracks']['items'][0]['uri']
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist!")
playlist = sp.user_playlist_create(user=USER_ID, name=f"{date} Billboard 100", public=False)
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
