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
    a= [{'trackTitle': 'Evermore - Piano Cover Version', 'href': 'https://open.spotify.com/track/0EHmjJMnI0ms6jrUlPCnhV'}, {'trackTitle': 'Dorothea - Piano Cover Version', 'href': 'https://open.spotify.com/track/0Z0KAlm3lasJMeHszjFsim'}, {'trackTitle': 'Coney Island - Piano Cover Version', 'href': 'https://open.spotify.com/track/19ue6dEDffDjgoNKrYDUAJ'}, {'trackTitle': 'Tolerate It - Piano Cover Version', 'href': 'https://open.spotify.com/track/1YC8SrYfYcddUxBASQHqaK'}, {'trackTitle': 'Right Where You Left Me - Piano Cover Version', 'href': 'https://open.spotify.com/track/2oS7BEjJ2UhXKdItoBfqTq'}, {'trackTitle': 'Cowboy Like Me - Piano Cover Version', 'href': 'https://open.spotify.com/track/2qDYT7eGdilMYtni2vu0AS'}, {'trackTitle': 'Ivy - Piano Cover Version', 'href': 'https://open.spotify.com/track/3B3JsGSqryeullvzF7ivBt'}, {'trackTitle': 'Marjorie - Piano Cover Version', 'href': 'https://open.spotify.com/track/3Mj89cVCNTgLnwlFhKryzJ'}, {'trackTitle': 'Champagne Problems - Piano Cover Version', 'href': 'https://open.spotify.com/track/4gtLgWwOmEdUOoqZlTKIv8'}, {'trackTitle': 'Willow - Piano Cover Version', 'href': 'https://open.spotify.com/track/4o9HC9hBujF9lL5RiFZ5Wp'}, {'trackTitle': 'Closure - Piano Cover Version', 'href': 'https://open.spotify.com/track/4xupaul9MbVnuj4x6FSefr'}, {'trackTitle': 'Long Story Short - Piano Cover Version', 'href': 'https://open.spotify.com/track/6mrJ0h87Wy6tep0riJuYni'}, {'trackTitle': "It's Time To Go - Piano Cover Version", 'href': 'https://open.spotify.com/track/7d1IwAwULtGDXoIt69FJwX'}, {'trackTitle': 'No Body, No Crime - Piano Cover Version', 'href': 'https://open.spotify.com/track/7DohN1feElp4qXeHOnOWFW'}, {'trackTitle': "'Tis The Damn Season - Piano Cover Version", 'href': 'https://open.spotify.com/track/7egqtxgwxtoFsTnlvq8OuK'}, {'trackTitle': 'Goldrush - Piano Cover Version', 'href': 'https://open.spotify.com/track/7h3EAlXwAdfzNUQebe12wH'}, {'trackTitle': 'The Man', 'href': 'https://open.spotify.com/track/01cCX1iNks6Ob0Ynwwg8tX'}, {'trackTitle': 'Take Me Back to London (feat. Stormzy)', 'href': 'https://open.spotify.com/track/02YbBewhPkI8VJ5GZqzTwM'}, {'trackTitle': 'Boa Me (feat. Ed Sheeran & Mugeez)', 'href': 'https://open.spotify.com/track/03EcqaAMg58r10dgbl0o6y'}, {'trackTitle': 'Galway Girl', 'href': 'https://open.spotify.com/track/042DklXACCB3vsO9ahvlhj'}, {'trackTitle': "I'm a Mess", 'href': 'https://open.spotify.com/track/05AXbdKlVvkT6IJlYAfuap'}, {'trackTitle': 'Amo Soltanto Te', 'href': 'https://open.spotify.com/track/05loQX8IAtgCZB8ObSHhxR'}, {'trackTitle': '2step (feat. Lil Baby)', 'href': 'https://open.spotify.com/track/06aqGQedRowWl0LzbvDFKh'}, {'trackTitle': 'The Great British Bar Off (Instrumental)', 'href': 'https://open.spotify.com/track/07Ts3S2c6UyCz1iODx1MND'}, {'trackTitle': 'I See Fire', 'href': 'https://open.spotify.com/track/0904bzxptKuNiQn6hljK4g'}, {'trackTitle': "You Need Me, I Don't Need You - Live Ustream", 'href': 'https://open.spotify.com/track/09ff09q87IPzIHuUN575vo'}, {'trackTitle': 'Head > Heels - Live from Keira’s Living Room', 'href': 'https://open.spotify.com/track/09RjA5mm3ElFtMXy0f1I25'}, {'trackTitle': 'No Strings', 'href': 'https://open.spotify.com/track/09UTOp33EhOSWzvGL0YOws'}, {'trackTitle': 'Perfect', 'href': 'https://open.spotify.com/track/0aCz5r63zFHVZP3K8hcMjB'}, {'trackTitle': 'Galway Girl', 'href': 'https://open.spotify.com/track/0afhq8XCExXpqazXczTSve'}, {'trackTitle': 'Perfect - Robin Schulz Remix', 'href': 'https://open.spotify.com/track/0AGAlxajK7xQN19o1eplzS'}, {'trackTitle': 'Shivers - Jax Jones Remix', 'href': 'https://open.spotify.com/track/0agfGxNgmzHogvIO8rtJAe'}, {'trackTitle': 'Midnight - Live from John’s Living Room', 'href': 'https://open.spotify.com/track/0aP608S0wKfse1LlDy9aZL'}, {'trackTitle': '2step (feat. Lil Baby)', 'href': 'https://open.spotify.com/track/0ASSuKgBIVfubKQZWVzkJS'}, {'trackTitle': 'Remember The Name (feat. Eminem & 50 Cent)', 'href': 'https://open.spotify.com/track/0AtP8EkGPn6SwxKDaUuXec'}, {'trackTitle': "Raise 'Em Up - Remix", 'href': 'https://open.spotify.com/track/0b3iohAa6fSjxu5ebiGLxW'}, {'trackTitle': 'Sigue', 'href': 'https://open.spotify.com/track/0bBd6K5X4W7t9GyXcaVOA7'}, {'trackTitle': 'Photograph', 'href': 'https://open.spotify.com/track/0bC05BVXzQxhRnUvDa39zN'}, {'trackTitle': 'Borderline', 'href': 'https://open.spotify.com/track/0bCnvkP7PYCJV64sQLl5mm'}, {'trackTitle': 'Toughest - Bonus Track', 'href': 'https://open.spotify.com/track/0C1dOJr5ae2tJSUGxMXTcC'}, {'trackTitle': 'Bad Habits', 'href': 'https://open.spotify.com/track/0c8CFwGepk9hmc4cuRPmXJ'}, {'trackTitle': 'Bed (feat. Ariana Grande)', 'href': 'https://open.spotify.com/track/00RxifQcRC9L0mysLkfmoY'}, {'trackTitle': 'Bed (feat. Ariana Grande)', 'href': 'https://open.spotify.com/track/01EjLX7sEjEfR50CiYps5i'}, {'trackTitle': 'yes, and? - slowed', 'href': 'https://open.spotify.com/track/01LUQUaLPgoADUwIAiVldF'}, {'trackTitle': 'True Love', 'href': 'https://open.spotify.com/track/02E2iNkWn6VTWWfbwrN7tY'}, {'trackTitle': 'pete davidson', 'href': 'https://open.spotify.com/track/02Qo5DFgoGTiBGo4ZUvjXm'}, {'trackTitle': 'Love Me Harder - Live from One Love Manchester', 'href': 'https://open.spotify.com/track/02rafvu0oC1fd7aoyJVhjG'}, {'trackTitle': 'bye', 'href': 'https://open.spotify.com/track/02Y9XQ74VNRFLikRe78nr5'}, {'trackTitle': 'Problem - Wayne G Radio Edit', 'href': 'https://open.spotify.com/track/04R0Qrg37pStX7AtGsn6Jn'}, {'trackTitle': 'Problem - Noodles & Devastator Remix', 'href': 'https://open.spotify.com/track/05iCwrGpNg0bw1x5KR3a0C'}, {'trackTitle': 'Love Me Harder - A Cappella', 'href': 'https://open.spotify.com/track/071IQ2wufBbCpB95z7VU7i'}, {'trackTitle': 'i wish i hated you', 'href': 'https://open.spotify.com/track/07IzLNKVhhGrLQ971uezZ8'}, {'trackTitle': 'Good as Hell (feat. Ariana Grande) - Remix', 'href': 'https://open.spotify.com/track/07Oz5StQ7GRoygNLaXs2pd'}, {'trackTitle': 'i wish i hated you', 'href': 'https://open.spotify.com/track/07SDnkvrBnh0vi44SkN37I'}, {'trackTitle': 'Hands On Me', 'href': 'https://open.spotify.com/track/09FrbOhB1v2VV5MxJd54qm'}, {'trackTitle': 'goodnight n go - live', 'href': 'https://open.spotify.com/track/0ao5xnzWNAt0dZFF6v4Sct'}, {'trackTitle': 'eternal sunshine', 'href': 'https://open.spotify.com/track/0aVv7dkFrfm7vcghTfQ1GQ'}, {'trackTitle': 'Rain On Me - Purple Disco Machine Remix', 'href': 'https://open.spotify.com/track/0b0WJSdPsu531iLWZ0FDqR'}, {'trackTitle': 'Be My Baby', 'href': 'https://open.spotify.com/track/0BFkaHSK8Irpp9KX7XUsvd'}, {'trackTitle': 'Met Him Last Night (feat. Ariana Grande)', 'href': 'https://open.spotify.com/track/0BI0hfbmqybnd3TezrDME3'}, {'trackTitle': 'imperfect for you - acoustic', 'href': 'https://open.spotify.com/track/0blfewz7XXrjsZd5WnHwgE'}, {'trackTitle': 'No One Mourns the Wicked', 'href': 'https://open.spotify.com/track/0br9vcQnqeqp9PKCGsrxAF'}, {'trackTitle': "Lovin' It", 'href': 'https://open.spotify.com/track/0CN72fWya38TPEQzrsr27w'}, {'trackTitle': 'imperfect for you - acoustic', 'href': 'https://open.spotify.com/track/0CtVKn43bnXL7IGnwSihds'}, {'trackTitle': 'Thinking Bout You', 'href': 'https://open.spotify.com/track/0D9w5UiVChw1VTZk1py37x'}, {'trackTitle': 'Only 1', 'href': 'https://open.spotify.com/track/0dIMoAWQxrC2prw2TKNCvw'}, {'trackTitle': 'Your Power', 'href': 'https://open.spotify.com/track/042Sl6Mn83JHyLEqdK7uI0'}, {'trackTitle': 'Bored', 'href': 'https://open.spotify.com/track/04sN26COy28wTXYj3dMoiZ'}, {'trackTitle': "Billie on Halley's Comet", 'href': 'https://open.spotify.com/track/05uGAMhJwz5mQSJAnmT9Ad'}, {'trackTitle': 'Guess featuring billie eilish', 'href': 'https://open.spotify.com/track/0Do1AZJJ03M0g8MmzUXLYf'}, {'trackTitle': 'GOLDWING', 'href': 'https://open.spotify.com/track/0FfqyjhB6Kspvit1oOo7ax'}, {'trackTitle': 'Guess featuring billie eilish', 'href': 'https://open.spotify.com/track/0IsIY8pfu1yaGkPUD7pkDx'}, {'trackTitle': 'NDA', 'href': 'https://open.spotify.com/track/0JdOW3PNgjpMAMNL4qOhe6'}, {'trackTitle': 'Billie on Happier Than Ever', 'href': 'https://open.spotify.com/track/0mduksE2lGkJfNg9QGvoHW'}, {'trackTitle': 'Happier Than Ever', 'href': 'https://open.spotify.com/track/0NtIbxAHcHDVsXSYswok9m'}, {'trackTitle': 'lovely (with Khalid)', 'href': 'https://open.spotify.com/track/0NxgdbKwdArO2TsRDGedbg'}, {'trackTitle': 'Lo Vas A Olvidar (with ROSALÍA)', 'href': 'https://open.spotify.com/track/0psS4i5YooJrXfDnGvWRLi'}, {'trackTitle': 'bad guy', 'href': 'https://open.spotify.com/track/0RhAhZlVAtFaRKMatXGcGi'}, {'trackTitle': '!!!!!!!', 'href': 'https://open.spotify.com/track/0rQtoQXQfwpDW0c7Fw1NeM'}, {'trackTitle': 'listen before i go', 'href': 'https://open.spotify.com/track/0tMSssfxAL2oV8Vri0mFHE'}, {'trackTitle': 'lovely', 'href': 'https://open.spotify.com/track/0TXFPRpO93GAm0uId8A6b7'}, {'trackTitle': 'lovely (with Khalid)', 'href': 'https://open.spotify.com/track/0u2P5u6lvoDfwTYjAADbn4'}, {'trackTitle': 'Bored', 'href': 'https://open.spotify.com/track/0uYxzqOAA2bXuSql3WJgVR'}, {'trackTitle': 'lovely', 'href': 'https://open.spotify.com/track/0vcjJIvWHZlJA1EREg6jkC'}, {'trackTitle': 'Billie on my future', 'href': 'https://open.spotify.com/track/0vo3z41Zg9Pi0ZEvNtWFwu'}, {'trackTitle': 'lovely (with Khalid)', 'href': 'https://open.spotify.com/track/0VZiLtiD8C4hA18WXaZTUv'}, {'trackTitle': 'hotline (edit)', 'href': 'https://open.spotify.com/track/0WFryfbNKPXVtVQlz5dZ8H'}, {'trackTitle': 'Billie on Billie Bossa Nova', 'href': 'https://open.spotify.com/track/17J0PiLFsGkeC4W7SeTMgm'}, {'trackTitle': 'Billie on Therefore I Am', 'href': 'https://open.spotify.com/track/1ccqLEH05B5kJXpYcX6l9S'}, {'trackTitle': 'SKINNY', 'href': 'https://open.spotify.com/track/1CsMKhwEmNnmvHUuO5nryA'}, {'trackTitle': 'Final Ascent - from "No Time to Die"', 'href': 'https://open.spotify.com/track/1E9Ko2AuCQDUepxp7Wx6iB'}, {'trackTitle': 'Where Are Ü Now (with Justin Bieber) - Kaskade Remix', 'href': 'https://open.spotify.com/track/00hlIlc6Ezzm0KABuxulgW'}, {'trackTitle': 'Trust', 'href': 'https://open.spotify.com/track/00IH8ZjI9ZGB51WRX1Oesj'}, {'trackTitle': 'Deja Vu', 'href': 'https://open.spotify.com/track/00YtwqiHf6mMy2RNXLuyb8'}, {'trackTitle': 'Peaches (Remix) feat. Ludacris, Usher & Snoop Dogg', 'href': 'https://open.spotify.com/track/010basloOyV7QxUPzYx7IC'}, {'trackTitle': 'Never Let You Go', 'href': 'https://open.spotify.com/track/01BlGnXpLuC0BjgUxVYZFb'}, {'trackTitle': '#thatPOWER', 'href': 'https://open.spotify.com/track/01TuObJVd7owWchVRuQbQw'}, {'trackTitle': 'Love Yourself', 'href': 'https://open.spotify.com/track/024TnKqCfXkkWImGRcJXcs'}, {'trackTitle': 'No Brainer (feat. Justin Bieber, Chance the Rapper & Quavo)', 'href': 'https://open.spotify.com/track/03nPEoQOYMuDe7KmGljpmd'}, {'trackTitle': 'Deja Vu', 'href': 'https://open.spotify.com/track/04rxhNRD9t4SxNVWHqEO8u'}, {'trackTitle': 'What You See (feat. Justin Bieber)', 'href': 'https://open.spotify.com/track/068vr9bgcrpLvE3csD10hg'}, {'trackTitle': "I Can't Be Myself (feat. Jaden)", 'href': 'https://open.spotify.com/track/08QMeVBL0buwazKq0mqMFz'}, {'trackTitle': 'Sorry', 'href': 'https://open.spotify.com/track/09CtPGIpYB4BrO8qb1RGsF'}, {'trackTitle': 'That Should Be Me', 'href': 'https://open.spotify.com/track/0aPZbnkMoWJaJ5CNVLCj8S'}, {'trackTitle': "Let Me Love You - Tiësto's AFTR:HRS Mix", 'href': 'https://open.spotify.com/track/0B0JXBDiAt4ewf1iyZLtCq'}, {'trackTitle': 'Hold On', 'href': 'https://open.spotify.com/track/0B0Wu4Srj7z7NtIIwwBMVq'}, {'trackTitle': 'Out Of Town Girl', 'href': 'https://open.spotify.com/track/0b1L4GuHRY7jLzcMdek3fP'}, {'trackTitle': 'up at night (feat. justin bieber)', 'href': 'https://open.spotify.com/track/0B3hRuQLvogv6InPAtI31H'}, {'trackTitle': 'Falling for You with Justin Bieber', 'href': 'https://open.spotify.com/track/0BVHCFgcB0CyOyPLmAoncB'}, {'trackTitle': 'E.T.A.', 'href': 'https://open.spotify.com/track/0C1xSrOo29uKo51JnvVXx8'}, {'trackTitle': 'Beauty And A Beat - DJ Laszlo Body Rock Instrumental', 'href': 'https://open.spotify.com/track/0CekEfkSD8hZUBTnY4XeAE'}, {'trackTitle': 'What You See (feat. Justin Bieber)', 'href': 'https://open.spotify.com/track/0dBhTtcsWHN85PvpOQ92Oa'}, {'trackTitle': 'All I Want Is You', 'href': 'https://open.spotify.com/track/0E4rAAAzRPE8I7tYzNq99p'}, {'trackTitle': 'Cold Water - Ocular Remix', 'href': 'https://open.spotify.com/track/0EMOMwbSpEc4cAIwL8grIO'}, {'trackTitle': 'Runaway Love - Kanye West Remix', 'href': 'https://open.spotify.com/track/0esMJjir6P5YsfQinJANmm'}, {'trackTitle': 'Bigger', 'href': 'https://open.spotify.com/track/0ffOWJVrYmtKcmQJbPWuhc'}, {'trackTitle': 'God Gave Me Everything', 'href': 'https://open.spotify.com/track/020X55mawvXGASoewg14Dj'}, {'trackTitle': 'Standing In The Rain', 'href': 'https://open.spotify.com/track/027OM9xL88L8LxM0iQ6kI1'}, {'trackTitle': 'Jack The Lad', 'href': 'https://open.spotify.com/track/02AfbLoxedlsGgibS3ptEi'}, {'trackTitle': 'Dancing in the Street - 2014 Remaster', 'href': 'https://open.spotify.com/track/03TgsqfeJDuAUCjIkomnV5'}, {'trackTitle': 'Gun', 'href': 'https://open.spotify.com/track/05FL9cCi2Y7kq27YMxaddC'}, {'trackTitle': 'Strange Game', 'href': 'https://open.spotify.com/track/05TrrXoqoI17WhDCP2mX19'}, {'trackTitle': 'Strange Game - From The ATV+ Original Series "Slow Horses”', 'href': 'https://open.spotify.com/track/0AOwMIY6XB78tGUDu37wXY'}, {'trackTitle': 'Angie (feat. Mick Jagger)', 'href': 'https://open.spotify.com/track/0buTv7Vv4xqNwaXwQ0kCp8'}, {'trackTitle': 'Paint It Black (Arr. J Reed for String Orchestra) [Live]', 'href': 'https://open.spotify.com/track/0BZrEcA6vcBR8xhecpWnQN'}, {'trackTitle': 'Paint It Black', 'href': 'https://open.spotify.com/track/0EfXlU8TjDLZyiySjDrIR5'}, {'trackTitle': 'Memo From Turner - "Mick Jagger" Version', 'href': 'https://open.spotify.com/track/0EsONXUbL4EzKW4Uoyymjq'}, {'trackTitle': 'Interview (2017 Remaster)', 'href': 'https://open.spotify.com/track/0HaWguk1IPhdad57w1HPw5'}, {'trackTitle': 'Take A Stroll', 'href': 'https://open.spotify.com/track/0jSxDVVAi6U1RYSSm973I6'}, {'trackTitle': 'Angel In My Heart', 'href': 'https://open.spotify.com/track/0KUA8ceRepWy7AissTOCKh'}, {'trackTitle': 'Lonely Without You (This Christmas)', 'href': 'https://open.spotify.com/track/0mQYdLzSu6k6nYy5Rb12Pd'}, {'trackTitle': 'Lucky In Love', 'href': 'https://open.spotify.com/track/0NTk9120h5oAiJPuR9GRcY'}, {'trackTitle': 'Doo Doo Doo Doo Doo (Heartbreaker)', 'href': 'https://open.spotify.com/track/0owGTle1xBp2AZIchl6fp6'}, {'trackTitle': 'Throwaway', 'href': 'https://open.spotify.com/track/0QCj7ygKQB5LiMVqNvZuKM'}, {'trackTitle': 'Jack The Lad', 'href': 'https://open.spotify.com/track/0RG3oIMbAC19mSfyspT6Wr'}, {'trackTitle': 'I Saw Her Standing There', 'href': 'https://open.spotify.com/track/0Tq21Bqg7aNNOGAERZUD5x'}, {'trackTitle': "Let's Make It Up", 'href': 'https://open.spotify.com/track/0uGOlj5sZWq6xVZXuvVcEY'}, {'trackTitle': 'Hide Away', 'href': 'https://open.spotify.com/track/0wcLrvE84uqVyc4XRZWi5t'}, {'trackTitle': "Mick Jagger's Introduction Of Rock And Roll Circus - Remastered 2018", 'href': 'https://open.spotify.com/track/0wTfqzrNDa2Oqtu1VwsOYm'}, {'trackTitle': "State of Shock / It's Only Rock 'N' Roll - Live at John F. Kennedy Stadium, 13th July 1985", 'href': 'https://open.spotify.com/track/1472rY0UUF0UU3E6MGrVxO'}, {'trackTitle': 'Lucky In Love', 'href': 'https://open.spotify.com/track/15HV13b7bpwz8yVOtRz5PY'}, {'trackTitle': 'Jealousy - Instrumental Piano', 'href': 'https://open.spotify.com/track/1Penoc9i5slOtatbmKJcjm'}, {'trackTitle': 'Love Of My Life - Instrumental Piano', 'href': 'https://open.spotify.com/track/2RdUeHlctA4A10lyVWxjKB'}, {'trackTitle': 'Love of my Life', 'href': 'https://open.spotify.com/track/5pSjmaLFx4rDgzpXuqQa2b'}, {'trackTitle': 'Run Rudolph Run', 'href': 'https://open.spotify.com/track/03RgPktGm7z3FOItOWPVmC'}, {'trackTitle': 'Play', 'href': 'https://open.spotify.com/track/17ph16tqpAIoPl82eODJJU'}, {'trackTitle': 'Overture', 'href': 'https://open.spotify.com/track/1IB79rbV1CpkXbVH4YjyaA'}, {'trackTitle': 'Little Drummer Boy', 'href': 'https://open.spotify.com/track/1jkMoafFyhEyZEY7Z3PoKY'}, {'trackTitle': 'Smells Like Teen Spirit (Arr. for Harp by Kristan Toczko)', 'href': 'https://open.spotify.com/track/1RlpNE5RqnL5dwPxSIxel3'}, {'trackTitle': 'Watch This (feat. Dave Grohl and Duff McKagan)', 'href': 'https://open.spotify.com/track/1wG9NacpTMP7AJrLo0xFO5'}, {'trackTitle': 'Razor (with Dave Grohl) (From “Norah Jones is Playing Along” Podcast)', 'href': 'https://open.spotify.com/track/2lyV1LeFzdV4xkoVMPaFbL'}, {'trackTitle': 'Smells Like Teen Spirit', 'href': 'https://open.spotify.com/track/36cVL96QwoNbXOtcxbZ2BK'}, {'trackTitle': 'Play', 'href': 'https://open.spotify.com/track/3ATAV8kiC5wg7U0eSMHlQp'}, {'trackTitle': 'Sex in Cars: Road Angel Project', 'href': 'https://open.spotify.com/track/3J6jWhwcjA9CzbTz5nIhyW'}, {'trackTitle': 'Times Like These - Piano Version', 'href': 'https://open.spotify.com/track/3JiCknRi0MUgTbL7ShQr4N'}, {'trackTitle': 'All Apologies (with Annie Clark, Kim Gordon, Joan Jett, Lorde & Pat Smear) - Live', 'href': 'https://open.spotify.com/track/3oQD3dLuLPTiX8mv8PkivB'}, {'trackTitle': 'Bitch - Live At The Honda Center, Anaheim', 'href': 'https://open.spotify.com/track/3tsl5n0xUlsI7JiTXk7IOK'}, {'trackTitle': 'Watch This (feat. Dave Grohl and Duff McKagan)', 'href': 'https://open.spotify.com/track/3uCHRtwAC94uaYNILcvKPn'}, {'trackTitle': 'Nausea', 'href': 'https://open.spotify.com/track/4AKAZGuK5rSiDQwayUQwDT'}, {'trackTitle': 'Aneurysm (with Kim Gordon & Pat Smear) - Live', 'href': 'https://open.spotify.com/track/4dLu4ewrvxu8gSlMcLEB02'}, {'trackTitle': 'Tie Your Mother Down', 'href': 'https://open.spotify.com/track/4M0xRnpmmPWbkCk2NpdHww'}, {'trackTitle': 'Everlong', 'href': 'https://open.spotify.com/track/4Q1Er9TrugkKROvSMbF5gE'}, {'trackTitle': 'Here We Go! (feat. Dave Grohl)', 'href': 'https://open.spotify.com/track/4XBzwf30aPQjRew5QkTGyf'}, {'trackTitle': 'Cut Me Some Slack', 'href': 'https://open.spotify.com/track/5CMTxPpruecKvEQCpNGIJb'}, {'trackTitle': 'Smells Like Teen Spirit - Arr. for Harp by Alexander Boldachev', 'href': 'https://open.spotify.com/track/5ih2m2fxZwLDSxnTGPlJRb'}, {'trackTitle': 'Times Like These', 'href': 'https://open.spotify.com/track/5IsOJSOdqkUSGFpb3O4gqg'}, {'trackTitle': 'Smells Like Teen Spirit', 'href': 'https://open.spotify.com/track/5l1gAoRwJ3ZnBI5uJQrV7u'}, {'trackTitle': 'Smells Like Teen Spirit (From "Black Widow") - Piano Version', 'href': 'https://open.spotify.com/track/5PnLygEc4ploPxUVxyNFq8'}, {'trackTitle': 'Wardance - 2003', 'href': 'https://open.spotify.com/track/5YiaQ6kXLT2CJ46v9QKr19'}, {'trackTitle': 'Better to Have and Not Need', 'href': 'https://open.spotify.com/track/2v3sH37cT6qQKtZgjygKPd'}, {'trackTitle': 'Lush Life 2021', 'href': 'https://open.spotify.com/track/02EpaVCV3sHXHFRfkfValW'}, {'trackTitle': 'Kompis 2020', 'href': 'https://open.spotify.com/track/10C6Yc5ftvbDCigdSQM1Eo'}, {'trackTitle': 'Chuggs 2024 (Hjemmesnekk)', 'href': 'https://open.spotify.com/track/10XA97aWseXhn3kmarIUMk'}, {'trackTitle': 'Merano 2023 (Hjemmesnekk)', 'href': 'https://open.spotify.com/track/2deVeq0PLlX3Ldq7FBDljd'}, {'trackTitle': 'Praise The Lord 2021', 'href': 'https://open.spotify.com/track/4gO7qZEk3tqt4Vq06kGauG'}, {'trackTitle': 'Böhmen 2024', 'href': 'https://open.spotify.com/track/4l1tnulcci4CJo0fYRRcun'}, {'trackTitle': 'Chuggington 2025 (Hjemmesnekk)', 'href': 'https://open.spotify.com/track/6n3O0KgdxaKDAClyJfmeh1'}, {'trackTitle': 'Chuggington 2025', 'href': 'https://open.spotify.com/track/6R4Qno9UuZ0FCFunJIMkBd'}, {'trackTitle': 'The Streets 2023', 'href': 'https://open.spotify.com/track/78IEhd2NrVhSuReypvqdUG'}, {'trackTitle': 'Gratitude', 'href': 'https://open.spotify.com/track/04sPzW7YjYRJH3z2zszGs0'}, {'trackTitle': 'Invocation', 'href': 'https://open.spotify.com/track/09KorSiJIrVgBVtjXuM8hA'}, {'trackTitle': 'WY Funk', 'href': 'https://open.spotify.com/track/2OZgCxRt9N4lOrxGnhgZQH'}, {'trackTitle': 'Bad Uncle John!', 'href': 'https://open.spotify.com/track/3x5vMKAYBMWAY44PQncNrZ'}, {'trackTitle': '2DC STREET LIFE (feat. JAY-ZO)', 'href': 'https://open.spotify.com/track/0K0lcj0NxdnJdbYfN5Ouak'}, {'trackTitle': 'Look Over Your Shoulder (feat. Kendrick Lamar)', 'href': 'https://open.spotify.com/track/00R0fEFZGb5hyTgF1nrRCq'}, {'trackTitle': 'Buy The World', 'href': 'https://open.spotify.com/track/01A7PEPSnmtixFPfB2UTal'}, {'trackTitle': "Don't Wanna Know - Fareoh Remix", 'href': 'https://open.spotify.com/track/03razZbZkx1pUvKrmcd14L'}, {'trackTitle': 'King Kunta', 'href': 'https://open.spotify.com/track/043Rs5H7XAV2soPAy88x02'}, {'trackTitle': 'Power Circle (feat. Kendrick Lamar, Rick Ross, Meek Mill, Wale & Stalley)', 'href': 'https://open.spotify.com/track/06eGuTsphGedNQ2SmpfuF6'}, {'trackTitle': 'LUST.', 'href': 'https://open.spotify.com/track/06FCvd7rrRcF3DdvWH5Isp'}, {'trackTitle': 'A1 Everything', 'href': 'https://open.spotify.com/track/07gbvH9nMYyZr92vbiicCi'}, {'trackTitle': 'The Heart Pt 3 (feat. Kendrick Lamar, Ab-Soul & Jay Rock)', 'href': 'https://open.spotify.com/track/097e3OID9lx9sBTZvMvmcm'}, {'trackTitle': 'Alright', 'href': 'https://open.spotify.com/track/09aetZ3AsciHWEPR9gR7aq'}, {'trackTitle': 'LA (feat. Kendrick Lamar, Brandy & James Fauntleroy)', 'href': 'https://open.spotify.com/track/09LlYzOV4SPLUNKNZ661fB'}, {'trackTitle': 'Really Be (Smokin N Drinkin)', 'href': 'https://open.spotify.com/track/09WkOmmVBwqii0dT7SdRTQ'}, {'trackTitle': 'Memories Back Then (feat. B.o.B, Kendrick Lamar & Kris Stephens)', 'href': 'https://open.spotify.com/track/0A2lJqfi04TKDTJYoKBxa9'}, {'trackTitle': 'tv off (feat. lefty gunplay)', 'href': 'https://open.spotify.com/track/0aB0v4027ukVziUGwVGYpG'}, {'trackTitle': 'All The Stars', 'href': 'https://open.spotify.com/track/0AH1MUoemTn74WfnSP9bKI'}, {'trackTitle': 'Backseat Freestyle', 'href': 'https://open.spotify.com/track/0B24oF0g3z0fkIQHLwnzHj'}, {'trackTitle': 'H.O.C', 'href': 'https://open.spotify.com/track/0bP9mtOuBLMQ7L0DP2wPwj'}, {'trackTitle': '2 Presidents (feat. Kendrick Lamar)', 'href': 'https://open.spotify.com/track/0c32tUwm5G3qdqS566wEBx'}, {'trackTitle': 'United In Grief', 'href': 'https://open.spotify.com/track/0c4GMGeJpWFYOBGuumrU3e'}, {'trackTitle': 'Momma', 'href': 'https://open.spotify.com/track/0CjJqkWOpIUXdem5hUcxAk'}, {'trackTitle': 'LOVE. FEAT. ZACARI.', 'href': 'https://open.spotify.com/track/0cWKiVsmXdtp2aeSelbmx8'}, {'trackTitle': 'Kali Love (feat. Kendrick Lamar)', 'href': 'https://open.spotify.com/track/0D3Myb8AY4siH5migv1lDg'}, {'trackTitle': 'man at the garden', 'href': 'https://open.spotify.com/track/0d9BfcBk5iBUC78VmTXGgY'}, {'trackTitle': 'Mona Lisa (feat. Kendrick Lamar)', 'href': 'https://open.spotify.com/track/0dbTQYW3Ad1FTzIA9t90E8'}, {'trackTitle': 'Two Presidents', 'href': 'https://open.spotify.com/track/0DlmsJPhJYSOKB4Ox8Sshh'}, {'trackTitle': 'Black Hippy - Shadow of Death (Bonus)', 'href': 'https://open.spotify.com/track/0dvC6ZkCTdQ9CPJEGpA34w'}, {'trackTitle': 'TELEFONO NUEVO', 'href': 'https://open.spotify.com/track/01ppKlDRCmPpusO3yNrSRY'}, {'trackTitle': 'Krippy Kush (feat. 21 Savage & Rvssian) - Remix', 'href': 'https://open.spotify.com/track/038kavjqUaGIYZL5lYocvX'}, {'trackTitle': 'El Amante (feat. Ozuna & Bad Bunny) - Remix', 'href': 'https://open.spotify.com/track/04f13iELcsYpY2yeLiAcfq'}, {'trackTitle': 'Lo Siento BB:/', 'href': 'https://open.spotify.com/track/04x1x0L8BYyIv1XlcJxWfi'}, {'trackTitle': 'Una Velita', 'href': 'https://open.spotify.com/track/059qzhNaJb8tsqpdl2bHfF'}, {'trackTitle': 'AM Remix', 'href': 'https://open.spotify.com/track/05bfbizlM5AX6Mf1RRyMho'}, {'trackTitle': 'Hasta Que Dios Diga', 'href': 'https://open.spotify.com/track/06s3QtMJVXw1AJX3UfvZG1'}, {'trackTitle': 'Dime', 'href': 'https://open.spotify.com/track/08wJw4VdkKImX4t1vL6MsO'}, {'trackTitle': 'TRELLAS', 'href': 'https://open.spotify.com/track/09WAnxdBuebQopKhJT3oZS'}, {'trackTitle': 'Mala y Peligrosa (feat. Bad Bunny)', 'href': 'https://open.spotify.com/track/0afpbPmRHldjP59YRslQz9'}, {'trackTitle': 'Ahora Me Llama', 'href': 'https://open.spotify.com/track/0alSPoUfrGb0RdVVG4Lf3n'}, {'trackTitle': 'Estamos Arriba', 'href': 'https://open.spotify.com/track/0bCPJsVGDxPYwQMDZMi4NW'}, {'trackTitle': 'Yo Perreo Sola', 'href': 'https://open.spotify.com/track/0d0qUYlS2zyba3jfxgHLrC'}, {'trackTitle': 'Otro Atardecer', 'href': 'https://open.spotify.com/track/0E0DRHf5PfMeor0ZCwB3oT'}, {'trackTitle': 'ADIVINO', 'href': 'https://open.spotify.com/track/0eeX8L0DWvGth1F6xVkvv7'}, {'trackTitle': 'UN DIA (ONE DAY) (Feat. Tainy)', 'href': 'https://open.spotify.com/track/0EhpEsp4L0oRGM0vmeaN5e'}, {'trackTitle': 'LA CANCIÓN', 'href': 'https://open.spotify.com/track/0fea68AdmYNygeTGI4RC18'}, {'trackTitle': 'P FKN R', 'href': 'https://open.spotify.com/track/0fgsKar6uBO08vzHXkTjWi'}, {'trackTitle': 'BYE ME FUI', 'href': 'https://open.spotify.com/track/0FktnzDqjClqU6iqOZVEs2'}, {'trackTitle': 'Volando - Remix', 'href': 'https://open.spotify.com/track/0G2zPzWqVjR68iNPmx2TBe'}, {'trackTitle': 'Vuelve', 'href': 'https://open.spotify.com/track/0gCPvo1GkbtPhMqg5Gbx1K'}, {'trackTitle': 'Desde El Corazón', 'href': 'https://open.spotify.com/track/0h9Jl9HgvmSF925xzkf5yK'}, {'trackTitle': 'Te Guste', 'href': 'https://open.spotify.com/track/0ifLplTQxXkFZKMQpWCHii'}, {'trackTitle': 'EL CLúB', 'href': 'https://open.spotify.com/track/0iKo4pNNjHHdKUcFARlfCa'}, {'trackTitle': 'El Favorito de los Capo - Remix', 'href': 'https://open.spotify.com/track/0jPkVCHNaLJhhtq70OingB'}, {'trackTitle': 'Kabar Aroma Tanah', 'href': 'https://open.spotify.com/track/7jZdufNsVHanf1omO5m2Sc'}, {'trackTitle': 'In Da Getto', 'href': 'https://open.spotify.com/track/1fwgfKheMO99mFnCg5Sp9z'}, {'trackTitle': 'Crazy Feelings', 'href': 'https://open.spotify.com/track/6ZLsMt2qbnmmFBfrjyRji5'}, {'trackTitle': 'Wicked Games', 'href': 'https://open.spotify.com/track/00aqkszH1FdUiJJWvX6iEl'}, {'trackTitle': 'One Right Now (with The Weeknd)', 'href': 'https://open.spotify.com/track/00Blm7zeNqgYLPtW6zg8cj'}, {'trackTitle': 'Sacrifice', 'href': 'https://open.spotify.com/track/00gscXjMt09aOxodmaDeR4'}, {'trackTitle': 'Blinding Lights', 'href': 'https://open.spotify.com/track/00uqj8HXl0hWr3tnxC0NZ5'}, {'trackTitle': 'After Hours - Live', 'href': 'https://open.spotify.com/track/00YDEzvKWMtkeTMbiNTv12'}, {'trackTitle': 'Fill The Void (with Lily Rose Depp, Ramsey)', 'href': 'https://open.spotify.com/track/010ZkIVv6Ay5vqqHVCCiKB'}, {'trackTitle': 'Party Monster', 'href': 'https://open.spotify.com/track/01qhnHgVio20RPBxIo4X6I'}, {'trackTitle': 'Moth to a Flame - Radio Edit', 'href': 'https://open.spotify.com/track/01vUD0zbE60Cu8oOUROxAJ'}, {'trackTitle': 'Rockin’', 'href': 'https://open.spotify.com/track/02V0fopGouDF5GbDHftv4S'}, {'trackTitle': 'Less Than Zero', 'href': 'https://open.spotify.com/track/02w1rM6spvEcbFxd63xCl2'}, {'trackTitle': 'Take My Breath - Live', 'href': 'https://open.spotify.com/track/02YlAvsmptN8LisZqrWBIb'}, {'trackTitle': 'Don’t Break My Heart', 'href': 'https://open.spotify.com/track/03CrsgSwGFlT5dr69wG4KE'}, {'trackTitle': 'Crew Love - Live', 'href': 'https://open.spotify.com/track/03H6iCycyxfB2mZzIOEeKJ'}, {'trackTitle': 'Real Life', 'href': 'https://open.spotify.com/track/03j354P848KtNU2FVSwkDG'}, {'trackTitle': 'Reminder', 'href': 'https://open.spotify.com/track/045g99gDVveOIJIlrJ2D8H'}, {'trackTitle': 'Blinding Lights', 'href': 'https://open.spotify.com/track/04948IGlqY1vSh7AHbueiQ'}, {'trackTitle': "Creepin' (with The Weeknd & 21 Savage) - ChoppedNotSlopped", 'href': 'https://open.spotify.com/track/067yehfYP7HD99fzRx5yOz'}, {'trackTitle': 'Gasoline', 'href': 'https://open.spotify.com/track/06CXvz1j4XLxVkcldLToIG'}, {'trackTitle': 'Save Your Tears', 'href': 'https://open.spotify.com/track/06fglfpCAtDtmlyfJYgA01'}, {'trackTitle': 'Pretty', 'href': 'https://open.spotify.com/track/06iCqHBiXigDk456S5L11y'}, {'trackTitle': 'Love Me Harder - A Cappella', 'href': 'https://open.spotify.com/track/071IQ2wufBbCpB95z7VU7i'}, {'trackTitle': 'Ordinary Life', 'href': 'https://open.spotify.com/track/09mBPwUMt1TXNtneqvmZZ5'}, {'trackTitle': 'Call Out My Name', 'href': 'https://open.spotify.com/track/09mEdoA6zrmBPgTEN5qXmN'}, {'trackTitle': 'Smile (with The Weeknd)', 'href': 'https://open.spotify.com/track/09NtNfFG4vpHsAUbdUug0M'}, {'trackTitle': 'Less Than Zero', 'href': 'https://open.spotify.com/track/0a2zAX33ZMrd5J73H1Ii9O'}, {'trackTitle': 'Old Memories On Christmas', 'href': 'https://open.spotify.com/track/00ZBDgUJ6FXyfGdM0U18hw'}, {'trackTitle': "You Don't Know My Name", 'href': 'https://open.spotify.com/track/012CtAkXny4bLUuXTWncvT'}, {'trackTitle': 'Another Way to Die', 'href': 'https://open.spotify.com/track/01bMpqmvH031R417l3AQTA'}, {'trackTitle': 'Looking for Paradise (feat. Alicia Keys)', 'href': 'https://open.spotify.com/track/02f5iKhfXVvCWK641es1sT'}, {'trackTitle': "You Don't Have To Be Alone", 'href': 'https://open.spotify.com/track/02Jg0jFoyNkZCAdrYnP3TR'}, {'trackTitle': 'Nat King Cole (Unlocked) (feat. Lil Wayne)', 'href': 'https://open.spotify.com/track/02pbPzBxvLfP81zmNEY5GO'}, {'trackTitle': 'Paper Flowers (Originals) (feat. Brandi Carlile)', 'href': 'https://open.spotify.com/track/04gtWDH0TJaJxvdROPb1fY'}, {'trackTitle': 'December Back 2 June', 'href': 'https://open.spotify.com/track/05DCz0eIhcGAb6YpNiwdbv'}, {'trackTitle': 'Nat King Cole (Live from Movistar Arena Santiago, Chile)', 'href': 'https://open.spotify.com/track/06mUBCiMjXvs6XNsJjxrX2'}, {'trackTitle': "Like You'll Never See Me Again - Clear Channel Stripped", 'href': 'https://open.spotify.com/track/07hN6XKoZaP8kTRthDIVTz'}, {'trackTitle': 'Authors Of Forever', 'href': 'https://open.spotify.com/track/07KwQFLMVs59SPF5pX36x2'}, {'trackTitle': 'Brand New Me', 'href': 'https://open.spotify.com/track/0827eActpDYORuhgvWB0oY'}, {'trackTitle': "How Come You Don't Call Me - Unplugged Live at the Brooklyn Academy of Music, Brooklyn, NY - July 2005", 'href': 'https://open.spotify.com/track/09oPdIGjxiJbzyX8AcHply'}, {'trackTitle': 'Wasted Energy (feat. Diamond Platnumz)', 'href': 'https://open.spotify.com/track/09vOpQsWEd7lK1OYGVhPH9'}, {'trackTitle': 'Heartburn - Unplugged Live at the Brooklyn Academy of Music, Brooklyn, NY - July 2005', 'href': 'https://open.spotify.com/track/0aIdmsQsG22oMaw5G3CLFo'}, {'trackTitle': 'Skydive Unlocked (Live From Movistar Arena Buenos Aires, Argentina)', 'href': 'https://open.spotify.com/track/0bJD1vA0dUQb5U869muHCy'}, {'trackTitle': 'Diary (feat. Tony! Toni! Tone! & Jermaine Paul) - Hani Mix', 'href': 'https://open.spotify.com/track/0BJwHrUuyw7msHP3AN9J54'}, {'trackTitle': 'No One - Live at Metropolis Studios, New York, NY - May 2013', 'href': 'https://open.spotify.com/track/0BleHROB2SxV7jv9dOQr7J'}, {'trackTitle': 'Only You (Unlocked)', 'href': 'https://open.spotify.com/track/0cBOTfiD6cgAVRi9xT3KuA'}, {'trackTitle': 'Love When You Call My Name (Unlocked)', 'href': 'https://open.spotify.com/track/0CSbPg8yLS8ZpAvVdedRbz'}, {'trackTitle': 'So Done (feat. Khalid)', 'href': 'https://open.spotify.com/track/0DC6yJLAPwIEeZh6EZpn1f'}, {'trackTitle': 'No One - Acoustic', 'href': 'https://open.spotify.com/track/0DeNwzmYKxmAe7XtfXRsB6'}, {'trackTitle': 'Illusion Of Bliss', 'href': 'https://open.spotify.com/track/0Dg3f2QML7eS1snW5Ra6A4'}, {'trackTitle': 'The Thing About Love', 'href': 'https://open.spotify.com/track/0dS5vi71dgXFID7jlyjKsr'}, {'trackTitle': 'Streets Of New York - AOL Broadband Rocks! Live at Webster Hall - December 1, 2003', 'href': 'https://open.spotify.com/track/0ejCk9fZOMpKqL6UXf544B'}, {'trackTitle': 'Treasure', 'href': 'https://open.spotify.com/track/00UKzpMWRTFew5KSh37MCB'}, {'trackTitle': "Love's Train", 'href': 'https://open.spotify.com/track/01Ok8HNEjfSYu6DQqes5Eu'}, {'trackTitle': 'Grenade - Michael Meds Mix', 'href': 'https://open.spotify.com/track/01sdh37jvLGU1t2O6uxJbn'}, {'trackTitle': 'Treasure', 'href': 'https://open.spotify.com/track/02HUuKwv31KEo8WnrNAf54'}, {'trackTitle': 'Finesse - Remix; feat. Cardi B', 'href': 'https://open.spotify.com/track/02iXInevQEAlihE3IPF0eh'}, {'trackTitle': 'Leave The Door Open', 'href': 'https://open.spotify.com/track/02VBYrHfVwfEWXk5DXyf0T'}, {'trackTitle': 'Locked out of Heaven - Paul Oakenfold Remix', 'href': 'https://open.spotify.com/track/03BpMAiFJ0b9c47Ntt8MRf'}, {'trackTitle': 'Finesse - James Hype Remix; feat. Cardi B', 'href': 'https://open.spotify.com/track/04OERuULAbFq54j25v5dZ4'}, {'trackTitle': 'Just the Way You Are - Manufactured Superstars and Jquintal Remix', 'href': 'https://open.spotify.com/track/04T47lGsiQU6x1cV9GhgDN'}, {'trackTitle': '3D', 'href': 'https://open.spotify.com/track/08RvcLNc26GX3vHgOzv4wV'}, {'trackTitle': 'Too Good to Say Goodbye', 'href': 'https://open.spotify.com/track/0B0tYbVp7pDQAqKDhgMeaL'}, {'trackTitle': 'Uptown Funk (feat. Bruno Mars) - BB Disco Dub Mix', 'href': 'https://open.spotify.com/track/0bjkXXAhDX2LEGgpTXE7IH'}, {'trackTitle': 'When I Was Your Man', 'href': 'https://open.spotify.com/track/0dccatsknQ5XkAflIRw5tK'}, {'trackTitle': 'Uptown Funk (feat. Bruno Mars)', 'href': 'https://open.spotify.com/track/0EI7zP0JAnUEVsUISYaVS7'}, {'trackTitle': 'The Other Side (feat. CeeLo Green and B.o.B)', 'href': 'https://open.spotify.com/track/0HasfWMrNxTjycDy9TkRtA'}, {'trackTitle': 'Locked Out of Heaven', 'href': 'https://open.spotify.com/track/0ilK3383D2WrFjbKhjNmIV'}, {'trackTitle': 'Natalie', 'href': 'https://open.spotify.com/track/0inMKhbKWOTDA9UBUAKoU6'}, {'trackTitle': "That's What I Like", 'href': 'https://open.spotify.com/track/0KKkJNfGyhkQ5aFogxQAPU'}, {'trackTitle': 'Versace on the Floor', 'href': 'https://open.spotify.com/track/0kN8xEmgMW9mh7UmDYHlJP'}, {'trackTitle': 'It Will Rain', 'href': 'https://open.spotify.com/track/0M3HkE321xpCbCYqVKzr1q'}, {'trackTitle': 'It Will Rain', 'href': 'https://open.spotify.com/track/0M57YPkDzSSx2GOeEq3V28'}, {'trackTitle': 'Chunky', 'href': 'https://open.spotify.com/track/0mBKv9DkYfQHjdMcw2jdyI'}, {'trackTitle': 'After Last Night', 'href': 'https://open.spotify.com/track/0mkOFe07y9cnCDcur07Ypd'}, {'trackTitle': 'When I Was Your Man', 'href': 'https://open.spotify.com/track/0nJW01T7XtvILxQgC5J7Wh'}, {'trackTitle': 'Lighters', 'href': 'https://open.spotify.com/track/0OUUS0P8FU6c0FMi1OLLDz'}, {'trackTitle': 'Brand New Man - with Luke Combs', 'href': 'https://open.spotify.com/track/001UkMQHw4zXfFNdKpwXAF'}, {'trackTitle': "This One's for You", 'href': 'https://open.spotify.com/track/02Ey48n33H3erWJRZAtTFj'}, {'trackTitle': 'Let the Moonshine', 'href': 'https://open.spotify.com/track/05DejmhRYCktQogzOVX1H9'}, {'trackTitle': 'Beyond (feat. Luke Combs) - Live', 'href': 'https://open.spotify.com/track/05zt3H2jdG0MA1V6Q2t2Et'}, {'trackTitle': 'Whoever You Turn Out to Be', 'href': 'https://open.spotify.com/track/09CXwVGMfxcRdOJQbiCJT6'}, {'trackTitle': 'How I Learned To Pray (feat. Luke Combs)', 'href': 'https://open.spotify.com/track/0bDLcvHBHnXxHfyS8yZX7R'}, {'trackTitle': 'South On Ya', 'href': 'https://open.spotify.com/track/0cvmA0xg8FkzKvBnO8987X'}, {'trackTitle': "Angels Workin' Overtime", 'href': 'https://open.spotify.com/track/0dGt5iXBcHZWMN8N8EmJIP'}, {'trackTitle': 'Be Careful What You Wish For', 'href': 'https://open.spotify.com/track/0dZxwPZlB1awNIvYbdULDH'}, {'trackTitle': 'Where the Wild Things Are', 'href': 'https://open.spotify.com/track/0eBFgRxyVSeuT4iyrbukdn'}, {'trackTitle': 'Memories Are Made Of', 'href': 'https://open.spotify.com/track/0h31TZMlv0ZLc5yppKngwk'}, {'trackTitle': "Lovin' On You", 'href': 'https://open.spotify.com/track/0IyIAxDXYOJMHLsTLrbOfy'}, {'trackTitle': 'The Other Guy', 'href': 'https://open.spotify.com/track/0jcZ1uIHmvh6Is9T6hXOUk'}, {'trackTitle': 'My Old Man Was Right', 'href': 'https://open.spotify.com/track/0JKxuYbxxfGMz4GGveQD0Q'}, {'trackTitle': 'Outlaw (feat. Luke Combs)', 'href': 'https://open.spotify.com/track/0jqIg4wzcKfRNJOJxxgPyn'}, {'trackTitle': 'Joe', 'href': 'https://open.spotify.com/track/0kPhTGl84wcSzdTareTroP'}, {'trackTitle': 'Does To Me (feat. Eric Church)', 'href': 'https://open.spotify.com/track/0nGXi46VcQQ56ZJR428MKS'}, {'trackTitle': "Lovin' On You", 'href': 'https://open.spotify.com/track/0nYvjcSlCgjcwogQAwIwNp'}, {'trackTitle': 'One Number Away - Recorded At Sound Stage Nashville', 'href': 'https://open.spotify.com/track/0RmtUP9oQqhO3WFqB3KrM2'}, {'trackTitle': 'Six Feet Apart', 'href': 'https://open.spotify.com/track/0tDOIR44aeHGLB5gpK1Gfn'}, {'trackTitle': "I Know She Ain't Ready", 'href': 'https://open.spotify.com/track/0TQ9Hf5DwI9crGZSIlq445'}, {'trackTitle': 'All I Ever Do Is Leave', 'href': 'https://open.spotify.com/track/0ttUJOEXB6jx1ybV6u1wsl'}, {'trackTitle': 'Tattoo on a Sunburn', 'href': 'https://open.spotify.com/track/0V75hy6x3cToema5BdJaj9'}, {'trackTitle': 'Blue Collar Boys', 'href': 'https://open.spotify.com/track/0wovagMoJqtU8LUvDQnewu'}, {'trackTitle': 'Reasons', 'href': 'https://open.spotify.com/track/0zK0C1rgdcZTVHtUCh2FPW'}, {'trackTitle': 'So Little I Wanted, So Little I Got (1960 Recording Remastered)', 'href': 'https://open.spotify.com/track/0SKtpBvIPbVrM7jY1F8LtM'}, {'trackTitle': 'Forbidden Love (1960 Recording Remastered)', 'href': 'https://open.spotify.com/track/5aXfjgoNZFnFvqDy0KJx5V'}, {'trackTitle': 'Money Motivation', 'href': 'https://open.spotify.com/track/1dKwXxwrPdzAG8Ipu3b2Wz'}, {'trackTitle': 'Jesus, Take the Wheel', 'href': 'https://open.spotify.com/track/00pFKTsXTYfLwGlNnUYETw'}, {'trackTitle': 'Wanted Woman', 'href': 'https://open.spotify.com/track/01iDGX2XRrd4ZVlhaDLbLp'}, {'trackTitle': 'Last Name- Story Behind the Song', 'href': 'https://open.spotify.com/track/022TgXGyKTNkYKzY998KvX'}, {'trackTitle': 'I Wanna Remember (feat. Carrie Underwood)', 'href': 'https://open.spotify.com/track/03ElQaGbZDwOSDMiEPwFPz'}, {'trackTitle': 'Just a Dream- Story Behind the Song', 'href': 'https://open.spotify.com/track/045z6ZTzvzWXGhGdq27qGt'}, {'trackTitle': 'Heartbeat', 'href': 'https://open.spotify.com/track/05BgC2247XGi8ySwBzOO0o'}, {'trackTitle': 'Leave a Light On (Talk Away The Dark)', 'href': 'https://open.spotify.com/track/05N2CVEkUbEd0slHLapdER'}, {'trackTitle': 'Hark! The Herald Angels Sing', 'href': 'https://open.spotify.com/track/06dg26ZZwu2FUY4dnbZHv3'}, {'trackTitle': 'Ghosts On The Stereo', 'href': 'https://open.spotify.com/track/0aoT1B6jxuaxPh1RQ2Cank'}, {'trackTitle': 'Songs Like This', 'href': 'https://open.spotify.com/track/0AqE1fmcWjKjrYNcTphhEM'}, {'trackTitle': 'Two Black Cadillacs- Story Behind the Song', 'href': 'https://open.spotify.com/track/0cqIQFvvegpKg9Sx9uU7DH'}, {'trackTitle': 'Temporary Home', 'href': 'https://open.spotify.com/track/0d0tJF80562KcMndcBcSfM'}, {'trackTitle': 'Blown Away- Story Behind the Song', 'href': 'https://open.spotify.com/track/0d1MqBEtk6EPc7mu5iUOGn'}, {'trackTitle': 'Something Good', 'href': 'https://open.spotify.com/track/0DD2CvkFnCrmt8fMuCL8TM'}, {'trackTitle': 'Hark! The Herald Angels Sing', 'href': 'https://open.spotify.com/track/0FH83qinp8Wyx36z33HMjU'}, {'trackTitle': 'Someday When I Stop Loving You', 'href': 'https://open.spotify.com/track/0FvYbfE2siVMEoXM8j0p5u'}, {'trackTitle': "Mama's Song", 'href': 'https://open.spotify.com/track/0HicNcPLKNp2YTnGRjj2te'}, {'trackTitle': 'Good Girl- Story Behind the Song', 'href': 'https://open.spotify.com/track/0HRqyCxfo2X8ix2HhqAWpX'}, {'trackTitle': 'Amazing Grace', 'href': 'https://open.spotify.com/track/0i67q5f6SBh6QvDgJV4f1v'}, {'trackTitle': 'Because He Lives', 'href': 'https://open.spotify.com/track/0IssjoPK88JuZug9zYkwcC'}, {'trackTitle': 'Jesus, Take the Wheel- Story Behind the Song', 'href': 'https://open.spotify.com/track/0K3nD5RScU9RemI1OseLiQ'}, {'trackTitle': 'I Wanna Remember (feat. Carrie Underwood)', 'href': 'https://open.spotify.com/track/0klaBlZdtjtWHOtAS7nUMJ'}, {'trackTitle': 'Blown Away', 'href': 'https://open.spotify.com/track/0LbaxqqbUVE1kANizaaL0F'}, {'trackTitle': 'Renegade Runaway', 'href': 'https://open.spotify.com/track/0Lf5evFei2z92kAxQzapy7'}, {'trackTitle': 'Pink Champagne', 'href': 'https://open.spotify.com/track/0LI59fuqv8OTAnY9cqCife'}]
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

def get_spotify_embed_url(track_id):
    return f"https://open.spotify.com/embed/track/{track_id}"  

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

    #----------------------------- Artist details -----------------------------#

    query_params = st.query_params
    selected_artist = query_params.get("artist_id")

    

    if selected_artist:
        selected_artist=get_artist_tracks(selected_artist)

        tracks = {}
        for i in selected_artist:
            tracks[i.get('trackTitle')]=i.get('href')
        
        col1, col2 = st.columns([1, 3])

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

    else:
        if "tracks" not in st.session_state:
            st.session_state["tracks"] = {i.get('trackTitle'): i.get('href') for i in artist_tracks_exception()}  # ✅ Store in session state


        col1, col2 = st.columns([1, 3])

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

    #----------------------------- Artist details -----------------------------#

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




# streamlit run player_layout.py