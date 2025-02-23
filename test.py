import streamlit as st
import requests

import requests
import streamlit as st
import random

# API Request Function
def make_request(endpoint, params=None):
    url = f"https://api.reccobeats.com/v1/{endpoint}"
    headers = {'Accept': 'application/json'}
    # proxies = {'http': 'http://127.0.0.1:8888', 'https': 'http://127.0.0.1:8888'}
    
    try:
        response = requests.get(url, headers=headers, params=params, verify=False)
        return response.json().get('content')
    except requests.RequestException:
        return None

# API Functions
def track_recommendation(query):
    return make_request("track/recommendation", {'size': str(random.randint(5,10)), 'seeds': query})

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

def add_custom_css():
    st.markdown(
        """
        <style>
            body {
                background-color: #121212;
                color: white;
                font-family: Arial, sans-serif;
            }
            .sidebar .sidebar-content {
                background-color: #181818;
            }
            .stButton>button {
                background: #1DB954;
                color: white;
                font-size: 16px;
                border-radius: 20px;
            }
            iframe {
                border-radius: 12px;
            }
            .artist-box {
                height: 400px;
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

            /* Floating Marquee */
            .marquee-container {
                position: fixed;
                right: 20px;
                top: 50%;
                transform: translateY(-50%);
                width: 220px;
                height: 320px;
                background: rgba(0, 0, 0, 0.8);
                padding: 15px;
                border-radius: 10px;
                text-align: center;
                overflow: hidden;
                color: white;
                box-shadow: 2px 2px 10px rgba(255, 255, 255, 0.2);
                display: flex;
                flex-direction: column;
                justify-content: flex-start;
                align-items: center;
            }

            /* Fixed Title */
            .marquee-title {
                font-size: 18px;
                font-weight: bold;
                text-transform: uppercase;
                margin-bottom: 10px;
                border-bottom: 2px solid #ff4b4b;
                padding-bottom: 5px;
                width: 100%;
                text-align: center;
                position: relative;
                z-index: 1;
            }

            /* Marquee Content */
            .marquee-content {
                display: block;
                line-height: 1.8;
                font-size: 16px;
                font-weight: bold;
                text-transform: uppercase;
                height: 250px;
                overflow: hidden;
                position: relative;
            }

            .marquee-inner {
                display: block;
                animation: scroll-up 6s linear infinite;
            }

            @keyframes scroll-up {
                0% { transform: translateY(100%); }
                100% { transform: translateY(-100%); }
            }

            /* Responsive Design for Mobile */
            @media (max-width: 768px) {
                .marquee-container {
                    display: none;
            }

        </style>
        """,
        unsafe_allow_html=True,
    )


def artist_list():
    a= [
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
    random.shuffle(a)
    return a[0:10]


def artist_tracks_exception():
    a= [{'trackTitle': 'Evermore - Piano Cover Version', 'href': 'https://open.spotify.com/track/0EHmjJMnI0ms6jrUlPCnhV'}, {'trackTitle': 'Dorothea - Piano Cover Version', 'href': 'https://open.spotify.com/track/0Z0KAlm3lasJMeHszjFsim'}, {'trackTitle': 'Coney Island - Piano Cover Version', 'href': 'https://open.spotify.com/track/19ue6dEDffDjgoNKrYDUAJ'}, {'trackTitle': 'Tolerate It - Piano Cover Version', 'href': 'https://open.spotify.com/track/1YC8SrYfYcddUxBASQHqaK'}, {'trackTitle': 'Right Where You Left Me - Piano Cover Version', 'href': 'https://open.spotify.com/track/2oS7BEjJ2UhXKdItoBfqTq'}, {'trackTitle': 'Cowboy Like Me - Piano Cover Version', 'href': 'https://open.spotify.com/track/2qDYT7eGdilMYtni2vu0AS'}, {'trackTitle': 'Ivy - Piano Cover Version', 'href': 'https://open.spotify.com/track/3B3JsGSqryeullvzF7ivBt'}, {'trackTitle': 'Marjorie - Piano Cover Version', 'href': 'https://open.spotify.com/track/3Mj89cVCNTgLnwlFhKryzJ'}, {'trackTitle': 'Champagne Problems - Piano Cover Version', 'href': 'https://open.spotify.com/track/4gtLgWwOmEdUOoqZlTKIv8'}, {'trackTitle': 'Willow - Piano Cover Version', 'href': 'https://open.spotify.com/track/4o9HC9hBujF9lL5RiFZ5Wp'}, {'trackTitle': 'Closure - Piano Cover Version', 'href': 'https://open.spotify.com/track/4xupaul9MbVnuj4x6FSefr'}, {'trackTitle': 'Long Story Short - Piano Cover Version', 'href': 'https://open.spotify.com/track/6mrJ0h87Wy6tep0riJuYni'}, {'trackTitle': "It's Time To Go - Piano Cover Version", 'href': 'https://open.spotify.com/track/7d1IwAwULtGDXoIt69FJwX'}, {'trackTitle': 'No Body, No Crime - Piano Cover Version', 'href': 'https://open.spotify.com/track/7DohN1feElp4qXeHOnOWFW'}, {'trackTitle': "'Tis The Damn Season - Piano Cover Version", 'href': 'https://open.spotify.com/track/7egqtxgwxtoFsTnlvq8OuK'}, {'trackTitle': 'Goldrush - Piano Cover Version', 'href': 'https://open.spotify.com/track/7h3EAlXwAdfzNUQebe12wH'}, {'trackTitle': 'The Man', 'href': 'https://open.spotify.com/track/01cCX1iNks6Ob0Ynwwg8tX'}, {'trackTitle': 'Take Me Back to London (feat. Stormzy)', 'href': 'https://open.spotify.com/track/02YbBewhPkI8VJ5GZqzTwM'}, {'trackTitle': 'Boa Me (feat. Ed Sheeran & Mugeez)', 'href': 'https://open.spotify.com/track/03EcqaAMg58r10dgbl0o6y'}, {'trackTitle': 'Galway Girl', 'href': 'https://open.spotify.com/track/042DklXACCB3vsO9ahvlhj'}, {'trackTitle': "I'm a Mess", 'href': 'https://open.spotify.com/track/05AXbdKlVvkT6IJlYAfuap'}, {'trackTitle': 'Amo Soltanto Te', 'href': 'https://open.spotify.com/track/05loQX8IAtgCZB8ObSHhxR'}, {'trackTitle': '2step (feat. Lil Baby)', 'href': 'https://open.spotify.com/track/06aqGQedRowWl0LzbvDFKh'}, {'trackTitle': 'The Great British Bar Off (Instrumental)', 'href': 'https://open.spotify.com/track/07Ts3S2c6UyCz1iODx1MND'}, {'trackTitle': 'I See Fire', 'href': 'https://open.spotify.com/track/0904bzxptKuNiQn6hljK4g'}, {'trackTitle': "You Need Me, I Don't Need You - Live Ustream", 'href': 'https://open.spotify.com/track/09ff09q87IPzIHuUN575vo'}, {'trackTitle': 'Head > Heels - Live from Keira’s Living Room', 'href': 'https://open.spotify.com/track/09RjA5mm3ElFtMXy0f1I25'}, {'trackTitle': 'No Strings', 'href': 'https://open.spotify.com/track/09UTOp33EhOSWzvGL0YOws'}, {'trackTitle': 'Perfect', 'href': 'https://open.spotify.com/track/0aCz5r63zFHVZP3K8hcMjB'}, {'trackTitle': 'Galway Girl', 'href': 'https://open.spotify.com/track/0afhq8XCExXpqazXczTSve'}, {'trackTitle': 'Perfect - Robin Schulz Remix', 'href': 'https://open.spotify.com/track/0AGAlxajK7xQN19o1eplzS'}, {'trackTitle': 'Shivers - Jax Jones Remix', 'href': 'https://open.spotify.com/track/0agfGxNgmzHogvIO8rtJAe'}, {'trackTitle': 'Midnight - Live from John’s Living Room', 'href': 'https://open.spotify.com/track/0aP608S0wKfse1LlDy9aZL'}, {'trackTitle': '2step (feat. Lil Baby)', 'href': 'https://open.spotify.com/track/0ASSuKgBIVfubKQZWVzkJS'}, {'trackTitle': 'Remember The Name (feat. Eminem & 50 Cent)', 'href': 'https://open.spotify.com/track/0AtP8EkGPn6SwxKDaUuXec'}, {'trackTitle': "Raise 'Em Up - Remix", 'href': 'https://open.spotify.com/track/0b3iohAa6fSjxu5ebiGLxW'}, {'trackTitle': 'Sigue', 'href': 'https://open.spotify.com/track/0bBd6K5X4W7t9GyXcaVOA7'}, {'trackTitle': 'Photograph', 'href': 'https://open.spotify.com/track/0bC05BVXzQxhRnUvDa39zN'}, {'trackTitle': 'Borderline', 'href': 'https://open.spotify.com/track/0bCnvkP7PYCJV64sQLl5mm'}, {'trackTitle': 'Toughest - Bonus Track', 'href': 'https://open.spotify.com/track/0C1dOJr5ae2tJSUGxMXTcC'}, {'trackTitle': 'Bad Habits', 'href': 'https://open.spotify.com/track/0c8CFwGepk9hmc4cuRPmXJ'}, {'trackTitle': 'Bed (feat. Ariana Grande)', 'href': 'https://open.spotify.com/track/00RxifQcRC9L0mysLkfmoY'}, {'trackTitle': 'Bed (feat. Ariana Grande)', 'href': 'https://open.spotify.com/track/01EjLX7sEjEfR50CiYps5i'}, {'trackTitle': 'yes, and? - slowed', 'href': 'https://open.spotify.com/track/01LUQUaLPgoADUwIAiVldF'}, {'trackTitle': 'True Love', 'href': 'https://open.spotify.com/track/02E2iNkWn6VTWWfbwrN7tY'}, {'trackTitle': 'pete davidson', 'href': 'https://open.spotify.com/track/02Qo5DFgoGTiBGo4ZUvjXm'}, {'trackTitle': 'Love Me Harder - Live from One Love Manchester', 'href': 'https://open.spotify.com/track/02rafvu0oC1fd7aoyJVhjG'}, {'trackTitle': 'bye', 'href': 'https://open.spotify.com/track/02Y9XQ74VNRFLikRe78nr5'}, {'trackTitle': 'Problem - Wayne G Radio Edit', 'href': 'https://open.spotify.com/track/04R0Qrg37pStX7AtGsn6Jn'}, {'trackTitle': 'Problem - Noodles & Devastator Remix', 'href': 'https://open.spotify.com/track/05iCwrGpNg0bw1x5KR3a0C'}, {'trackTitle': 'Love Me Harder - A Cappella', 'href': 'https://open.spotify.com/track/071IQ2wufBbCpB95z7VU7i'}, {'trackTitle': 'i wish i hated you', 'href': 'https://open.spotify.com/track/07IzLNKVhhGrLQ971uezZ8'}, {'trackTitle': 'Good as Hell (feat. Ariana Grande) - Remix', 'href': 'https://open.spotify.com/track/07Oz5StQ7GRoygNLaXs2pd'}, {'trackTitle': 'i wish i hated you', 'href': 'https://open.spotify.com/track/07SDnkvrBnh0vi44SkN37I'}, {'trackTitle': 'Hands On Me', 'href': 'https://open.spotify.com/track/09FrbOhB1v2VV5MxJd54qm'}, {'trackTitle': 'goodnight n go - live', 'href': 'https://open.spotify.com/track/0ao5xnzWNAt0dZFF6v4Sct'}, {'trackTitle': 'eternal sunshine', 'href': 'https://open.spotify.com/track/0aVv7dkFrfm7vcghTfQ1GQ'}, {'trackTitle': 'Rain On Me - Purple Disco Machine Remix', 'href': 'https://open.spotify.com/track/0b0WJSdPsu531iLWZ0FDqR'}, {'trackTitle': 'Be My Baby', 'href': 'https://open.spotify.com/track/0BFkaHSK8Irpp9KX7XUsvd'}, {'trackTitle': 'Met Him Last Night (feat. Ariana Grande)', 'href': 'https://open.spotify.com/track/0BI0hfbmqybnd3TezrDME3'}, {'trackTitle': 'imperfect for you - acoustic', 'href': 'https://open.spotify.com/track/0blfewz7XXrjsZd5WnHwgE'}, {'trackTitle': 'No One Mourns the Wicked', 'href': 'https://open.spotify.com/track/0br9vcQnqeqp9PKCGsrxAF'}, {'trackTitle': "Lovin' It", 'href': 'https://open.spotify.com/track/0CN72fWya38TPEQzrsr27w'}, {'trackTitle': 'imperfect for you - acoustic', 'href': 'https://open.spotify.com/track/0CtVKn43bnXL7IGnwSihds'}, {'trackTitle': 'Thinking Bout You', 'href': 'https://open.spotify.com/track/0D9w5UiVChw1VTZk1py37x'}, {'trackTitle': 'Only 1', 'href': 'https://open.spotify.com/track/0dIMoAWQxrC2prw2TKNCvw'}, {'trackTitle': 'Your Power', 'href': 'https://open.spotify.com/track/042Sl6Mn83JHyLEqdK7uI0'}, {'trackTitle': 'Bored', 'href': 'https://open.spotify.com/track/04sN26COy28wTXYj3dMoiZ'}, {'trackTitle': "Billie on Halley's Comet", 'href': 'https://open.spotify.com/track/05uGAMhJwz5mQSJAnmT9Ad'}, {'trackTitle': 'Guess featuring billie eilish', 'href': 'https://open.spotify.com/track/0Do1AZJJ03M0g8MmzUXLYf'}, {'trackTitle': 'GOLDWING', 'href': 'https://open.spotify.com/track/0FfqyjhB6Kspvit1oOo7ax'}, {'trackTitle': 'Guess featuring billie eilish', 'href': 'https://open.spotify.com/track/0IsIY8pfu1yaGkPUD7pkDx'}, {'trackTitle': 'NDA', 'href': 'https://open.spotify.com/track/0JdOW3PNgjpMAMNL4qOhe6'}, {'trackTitle': 'Billie on Happier Than Ever', 'href': 'https://open.spotify.com/track/0mduksE2lGkJfNg9QGvoHW'}, {'trackTitle': 'Happier Than Ever', 'href': 'https://open.spotify.com/track/0NtIbxAHcHDVsXSYswok9m'}, {'trackTitle': 'lovely (with Khalid)', 'href': 'https://open.spotify.com/track/0NxgdbKwdArO2TsRDGedbg'}]
    random.shuffle(a)
    return a[random.randint(0, 5):random.randint(10, 15)]


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

    
    # Set page config
    st.set_page_config(page_title="Spotify Clone", layout="wide")


    add_custom_css()

    # Sidebar for navigation & search
    st.sidebar.title("🎵 Search Favourite Artist")
    st.title("Spotify Clone 🎧")

    #----------------------------- Search for an artist -----------------------------#
    artist_name = st.sidebar.text_input("Search for an artist", placeholder="Enter artist name")

    search_button = st.sidebar.button("Search")

    #----------------------------- Search for an artist -----------------------------#
    # Handle artist search
    if search_button and artist_name:
        searched_artists = search_artist(artist_name)
        if searched_artists:
            artist_links = "".join(
                [f'<a href="?artist_id={artist["id"]}">{artist["name"]}</a><br>'
                for artist in searched_artists]
            )
            st.sidebar.markdown(f'<div class="artist-box">{artist_links}</div>', unsafe_allow_html=True)
        else:
            st.sidebar.write("No artist found")


    

    #----------------------------- Search for an artist -----------------------------#

    #----------------------------- Artist songs -----------------------------#

    query_params = st.query_params
    selected_artist = query_params.get("artist_id")

    

    if selected_artist:
        selected_artist=get_artist_tracks(selected_artist)

        tracks = {}
        for i in selected_artist:
            tracks[i.get('trackTitle')]=i.get('href')
        
        col1, col2, col3 = st.columns([1, 4,2])

        with col1:
            st.subheader("Top Tracks")
            for track, track_id in tracks.items():
                if st.button(track):
                    st.session_state["current_track"] = track_id


        with col2:
            st.subheader("Now Playing")
            if "current_track" in st.session_state:
               play_song(st.session_state["current_track"])
            else:
                st.write("Select a track to play")

        with col3:
            st.subheader("Recommended Tracks")
            if "current_track" in st.session_state:
                selected_song=st.session_state["current_track"]
                recommended_tracks = track_recommendation(selected_song.split('track/')[1])
                tracks = {}
                for i in recommended_tracks:
                    tracks[i.get('trackTitle')]=i.get('href')

                if len(tracks) > 0: 
                    try:
                        for track, track_id in tracks.items():
                            print(track, track_id)
                            if st.button(track, key=track_id):
                                st.session_state["current_track_2"] = track_id
                    except:
                        st.write("No recommended tracks found")
                if "current_track_2" in st.session_state:
                    with col2:
                        st.subheader("Now Playing from recommended tracks")
                        if "current_track_2" in st.session_state:
                            play_song(st.session_state["current_track_2"])
                        else:
                            st.write("Select a track to play")

    else:
        if "tracks" not in st.session_state:
            st.session_state["tracks"] = {i.get('trackTitle'): i.get('href') for i in artist_tracks_exception()}  # ✅ Store in session state


        col1, col2,col3 = st.columns([1, 4, 2])

        with col1:
            st.subheader("Top Tracks")
            for track, track_id in st.session_state["tracks"].items():
                if st.button(track):
                    st.session_state["current_track"] = track_id

        with col2:
            st.subheader("Now Playing")
            if "current_track" in st.session_state:
                play_song(st.session_state["current_track"])
            else:
                st.write("Select a track to play")

        with col3:
            st.subheader("Recommended Tracks")
            if "current_track" in st.session_state:
                selected_song=st.session_state["current_track"]
                recommended_tracks = track_recommendation(selected_song.split('track/')[1])
                tracks = {}
                for i in recommended_tracks:
                    tracks[i.get('trackTitle')]=i.get('href')

                if len(tracks) > 0: 
                    try:
                        for track, track_id in tracks.items():
                            print(track, track_id)
                            if st.button(track, key=track_id):
                                st.session_state["current_track_2"] = track_id
                    except:
                        st.write("No recommended tracks found")
                if "current_track_2" in st.session_state:
                    with col2:
                        st.subheader("Now Playing from recommended tracks")
                        if "current_track_2" in st.session_state:
                            play_song(st.session_state["current_track_2"])
                        else:
                            st.write("Select a track to play")
                

    #----------------------------- Artist songs -----------------------------#

    #-----------------------------Most streamed artists -----------------------------#

    if "most_streamed_artists" not in st.session_state:
        st.session_state["most_streamed_artists"] = [i['name'] for i in artist_list()]  # ✅ Store in session state

    marquee_html = f"""
    
    <div class="marquee-container">
    <div class="marquee-title">Most Streamed Artists</div>
        <div class="marquee-content">
        <div class="marquee-inner">
            {'<br>'.join(st.session_state["most_streamed_artists"])}
        </div>
        </div>
    </div>
    """

    st.markdown(marquee_html, unsafe_allow_html=True)
    #-----------------------------Most streamed artists -----------------------------#


