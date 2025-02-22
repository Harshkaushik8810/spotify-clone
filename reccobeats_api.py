import requests
import streamlit as st
import random

# API Request Function
def make_request(endpoint, params=None):
    url = f"https://api.reccobeats.com/v1/{endpoint}"
    headers = {'Accept': 'application/json'}
    proxies = {'http': 'http://127.0.0.1:8888', 'https': 'http://127.0.0.1:8888'}
    
    try:
        response = requests.get(url, headers=headers, params=params, proxies=proxies, verify=False)
        return response.json().get('content')
    except requests.RequestException:
        return None

# API Functions
def track_recommendation():
    return make_request("track/recommendation", {'size': '10', 'seeds': '23'})

def track_details(track_id):
    return make_request(f"track/{track_id}")

def get_multiple_tracks(track_ids):
    return make_request(f"track", {'ids': track_ids})

def get_track_album(track_id):
    return make_request(f"track/{track_id}/album")

def get_artist_detail(artist_id):
    return make_request(f"artist/{artist_id}")

def get_multiple_artists(artist_ids):
    return make_request("artist", {'ids': artist_ids})

def search_artist(query):
    return make_request("artist/search", {'searchText': query})

def get_artist_album(artist_id):
    return make_request(f"artist/{artist_id}/album")

def get_artist_tracks(artist_id):
    return make_request(f"artist/{artist_id}/track")

def get_album_detail(album_id):
    return make_request(f"album/{album_id}")

def get_multiple_album_details(album_ids):
    return make_request("album", {'ids': album_ids})

def get_album_tracks(album_id):
    return make_request(f"album/{album_id}/track")

def search_album(query):
    return make_request("album/search", {'searchText': query})



def artist_list():
    return [
    {'name': 'Taylor Swift', 'id': '9dbc631b-05e5-4bc7-bf79-4fce71e7765d'},
    {'name': 'Ed Sheeran', 'id': '126957af-c257-4484-afa5-f9a000d20073'},
    {'name': 'Ariana Grande', 'id': '320a87e6-a2b9-421f-9b4e-aa44f8c784bb'},
    {'name': 'Billie Eilish', 'id': 'bf2c5ca2-f233-4846-b804-3a0b4a6a9909'},
    {'name': 'Justin Bieber', 'id': 'fce6b855-887c-47c4-a81a-b708cd01f59e'},
    {'name': 'Mick Jagger', 'id': '869ada7e-7b02-4c1b-b013-0f4785cdfb0a'},
    {'name': 'Freddie Mercury', 'id': '618ba6c7-d707-4964-b8cc-b69549d4ef97'},
    {'name': 'Dave Grohl', 'id': '380d0ea8-bfb4-43a1-80bb-def7ef391ba9'},
    {'name': 'Bruce Springsteen', 'id': '7ca7d78d-d824-4553-8fc8-d750c9202741'},
    {'name': 'Eminem', 'id': '6026a0e6-1386-4f01-9dde-0ea943036934'},
    {'name': 'Drake', 'id': 'b34fa5cf-1522-4d95-a261-8ddce52d9e01'},
    {'name': 'Jay-Z', 'id': 'b90ff38f-b12f-4adb-ac27-d02274b782b2'},
    {'name': 'Kendrick Lamar', 'id': 'caa924b3-075d-462a-bc84-b8da4ebb9f38'},
    {'name': 'Bad Bunny', 'id': 'eb33e89c-4cfc-4d89-93eb-da50024b024c'},
    {'name': 'Shakira', 'id': '1a7b21e9-792b-4ddb-beb4-bfce9a912d8e'},
    {'name': 'J Balvin', 'id': 'ff19bfd7-d7e7-4360-9653-e5ef8c3059fb'},
    {'name': 'Beyoncé', 'id': '538dc108-266c-4f12-a046-d835d09868e6'},
    {'name': 'The Weeknd', 'id': '9451b6b2-8746-4d43-abd7-c355ed1e3048'},
    {'name': 'Alicia Keys', 'id': 'de496515-6203-405b-9720-620b222a2221'},
    {'name': 'Bruno Mars', 'id': 'a46a685c-dfd6-48b8-811c-1dd953622918'},
    {'name': 'Luke Combs', 'id': '6b7dd455-2f40-48b7-a30f-84f2129506b3'},
    {'name': 'Dolly Parton', 'id': '496972ce-2ec0-4f1b-9be8-1704e0fb9974'},
    {'name': 'Johnny Cash', 'id': 'a65fc7ea-6927-4eba-9390-733fe3400c50'},
    {'name': 'Carrie Underwood', 'id': '88d3aae5-8fcf-48c8-b4d2-ddc91c18abf6'}
]

def play_song(spotify_url):

    
    st.title("🎵 Play a Song in Streamlit")

    # Input field for Spotify URL
    song_url = spotify_url

    if song_url:
        # Convert open.spotify.com URL to embed.spotify.com
        embed_url = song_url.replace("open.spotify.com", "embed.spotify.com").replace("/track/", "/embed/track/")
        
        # Embed the Spotify player
        st.components.v1.iframe(embed_url, height=80)


if __name__ == "__main__":
    st.set_page_config(layout="wide")

    st.markdown(
        """
        <style>
            .artist-box {
                height: 500px;
                overflow-y: auto;
                border-radius: 10px;
                border: 2px solid #ff4b4b;
                padding: 15px;
                background-color: #1e1e1e;
                color: white;
                box-shadow: 2px 2px 10px rgba(255, 75, 75, 0.5);
            }
            .artist-box a {
                color: white;
                text-decoration: none;
                font-weight: bold;
                display: block;
                padding: 5px 0;
            }
            .artist-box a:hover {
                color: #ff4b4b;
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    col1, col2 = st.columns([1, 4])  
    
    with col1:
        st.markdown("### 📌 Most Streamed Artists")
        artist_links = "".join(
            [f'<a href="?artist_id={artist.get("id")}">{artist.get("name")}</a><br>'
             for artist in artist_list()]
        )
        st.markdown(f'<div class="artist-box">{artist_links}</div>', unsafe_allow_html=True)

    with col2:
        st.title("Hello Streamlit!")
        user_input = st.text_input("Enter Artist Name")

        if user_input:
            searched_artists = search_artist(user_input)
            if searched_artists:
                artist_links = "".join(
                    [f'<a href="?artist_id={artist.get("id")}">{artist.get("name")}</a><br>'
                     for artist in searched_artists]
                )
                st.markdown(f'<div class="artist-box">{artist_links}</div>', unsafe_allow_html=True)
            else:
                st.write("No artist found")

    query_params = st.query_params
    selected_artist = query_params.get("artist_id")
    
    if selected_artist:
        albums = get_artist_tracks(selected_artist)
        if albums:
            album_links = "".join(
                [f'<a href="?artist_id={album.get("href")}">{album.get("trackTitle")}</a><br>'
                 for album in albums]
            )
            st.markdown(f'<div class="artist-box">{album_links}</div>', unsafe_allow_html=True)

        song_url = query_params.get("artist_id")
        if song_url:
            play_song(song_url)


#streamlit run reccobeats_api.py