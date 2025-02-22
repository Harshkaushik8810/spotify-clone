import requests
import streamlit as st
import random




def track_recommendation(query):
    url = "https://api.reccobeats.com/v1/track/recommendation"

    params = {
        'size':'10',
        'seeds':'23'
    }
    headers = {
    'Accept': 'application/json'
    }
    proxies = {
        'http': 'http://127.0.0.1:8888',
        'https': 'http://127.0.0.1:8888'
    }
    response = requests.get(url, headers=headers,params=params,proxies=proxies,verify=False)
    
    try:
        data = response.json()
        return data
    except:
        return False


def track_details(query):
    url = "https://api.reccobeats.com/v1/track/{}".format(query)

    headers = {
    'Accept': 'application/json'
    }
    proxies = {
        'http': 'http://127.0.0.1:8888',
        'https': 'http://127.0.0.1:8888'
    }
    response = requests.get(url, headers=headers,proxies=proxies,verify=False)
    
    try:
        data = response.json()
        return data
    except:
        return False
    
def get_multiple_track(query):
    url = "https://api.reccobeats.com/v1/track?ids={}".format(query)

    headers = {
    'Accept': 'application/json'
    }
    proxies = {
        'http': 'http://127.0.0.1:8888',
        'https': 'http://127.0.0.1:8888'
    }
    response = requests.get(url, headers=headers,proxies=proxies,verify=False)
    
    try:
        data = response.json()
        return data
    except:
        return False
    
def get_track_album(query):
    url = "https://api.reccobeats.com/v1/track/{}/album".format(query)

    headers = {
    'Accept': 'application/json'
    }
    proxies = {
        'http': 'http://127.0.0.1:8888',
        'https': 'http://127.0.0.1:8888'
    }
    response = requests.get(url, headers=headers,proxies=proxies,verify=False)
    
    try:
        data = response.json()
        return data
    except:
        return False
    
def get_artist_detail(query):
    url = "https://api.reccobeats.com/v1/artist/{}".format(query)

    headers = {
    'Accept': 'application/json'
    }
    proxies = {
        'http': 'http://127.0.0.1:8888',
        'https': 'http://127.0.0.1:8888'
    }
    response = requests.get(url, headers=headers,proxies=proxies,verify=False)
    
    try:
        data = response.json()
        return data
    except:
        return False

def get_multiple_artist(query):
    url = "https://api.reccobeats.com/v1/artist?ids={}".format(query)

    headers = {
    'Accept': 'application/json'
    }
    proxies = {
        'http': 'http://127.0.0.1:8888',
        'https': 'http://127.0.0.1:8888'
    }
    response = requests.get(url, headers=headers,proxies=proxies,verify=False)
    
    try:
        data = response.json()
        return data
    except:
        return False
    

def search_artist(query):
    url = "https://api.reccobeats.com/v1/artist/search?searchText={}".format(query)

    headers = {
    'Accept': 'application/json'
    }
    proxies = {
        'http': 'http://127.0.0.1:8888',
        'https': 'http://127.0.0.1:8888'
    }
    response = requests.get(url, headers=headers,proxies=proxies,verify=False)
    
    try:
        data = response.json()
        return data.get('content')[0]
    except:
        return False
    
def get_artist_album(query):
    url = "https://api.reccobeats.com/v1/artist/{}/album".format(query)

    headers = {
    'Accept': 'application/json'
    }
    proxies = {
        'http': 'http://127.0.0.1:8888',
        'https': 'http://127.0.0.1:8888'
    }
    response = requests.get(url, headers=headers,proxies=proxies,verify=False)
    
    try:
        data = response.json()
        return data.get('content')
    except:
        return False
    
def get_artist_track(query):
    url = "https://api.reccobeats.com/v1/artist/{}/track".format(query)

    headers = {
    'Accept': 'application/json'
    }
    proxies = {
        'http': 'http://127.0.0.1:8888',
        'https': 'http://127.0.0.1:8888'
    }
    response = requests.get(url, headers=headers,proxies=proxies,verify=False)
    
    try:
        data = response.json()
        return data.get('content')
    except:
        return False
    
def get_album_detail(query):
    url = "https://api.reccobeats.com/v1/album/{}".format(query)

    headers = {
    'Accept': 'application/json'
    }
    proxies = {
        'http': 'http://127.0.0.1:8888',
        'https': 'http://127.0.0.1:8888'
    }
    response = requests.get(url, headers=headers,proxies=proxies,verify=False)
    
    try:
        data = response.json()
        return data
    except:
        return False
    
def get_multiple_album_detail(query):
    url = "https://api.reccobeats.com/v1/album?ids={}".format(query)

    headers = {
    'Accept': 'application/json'
    }
    proxies = {
        'http': 'http://127.0.0.1:8888',
        'https': 'http://127.0.0.1:8888'
    }
    response = requests.get(url, headers=headers,proxies=proxies,verify=False)
    
    try:
        data = response.json()
        return data
    except:
        return False
    
def get_album_track(query):
    url = "https://api.reccobeats.com/v1/album/{}/track".format(query)

    headers = {
    'Accept': 'application/json'
    }
    proxies = {
        'http': 'http://127.0.0.1:8888',
        'https': 'http://127.0.0.1:8888'
    }
    response = requests.get(url, headers=headers,proxies=proxies,verify=False)
    
    try:
        data = response.json()
        return data
    except:
        return False
    
def search_album(query):
    url = "https://api.reccobeats.com/v1/album/search?searchText={}".format(query)

    headers = {
    'Accept': 'application/json'
    }
    proxies = {
        'http': 'http://127.0.0.1:8888',
        'https': 'http://127.0.0.1:8888'
    }
    response = requests.get(url, headers=headers,proxies=proxies,verify=False)
    
    try:
        data = response.json()
        return data
    except:
        return False
    
if __name__ == "__main__":
    
    l=[]
    singers= [
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

    l=[]
    for i in singers:
        data=get_artist_track(i.get('id'))
        for j in data:
            l.append({'trackTitle':j.get('trackTitle'),'href':j.get('href')})

    print(l)

    

   

#streamlit run reccobeats_api.py