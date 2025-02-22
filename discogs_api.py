import requests
import streamlit as st
import random




def search_releases(query):
    url = "https://api.discogs.com/database/search"
    params = {
        'q': query,  # Search term (e.g., artist or album name)
        'type': 'release',  # Only search for releases
        'token': 'ZPkumuBZDlkcvFBxegsCrnVhmHotUtEnlLXeMODB'  # Replace with your Discogs API token
    }

    proxies = {
        'http': 'http://127.0.0.1:8888',
        'https': 'http://127.0.0.1:8888'
    }
    response = requests.get(url, params=params,proxies=proxies,verify=False)
    
    try:
        data = response.json()
        if len(data.get('results')) == 0:
            return False
        else:
            return data.get('results')
    except:
        return False


if __name__ == "__main__":

    st.title("Hello Streamlit")
    st.write("This is my first Streamlit app!")
    user_input = st.text_input("Enter Artist name")
    

    if user_input:
        # st.write(search_releases(user_input))
        user_data = search_releases(user_input)

        if user_data:
            num_columns = 5
            columns = st.columns(num_columns)
            for i in range(num_columns):
                column = columns[i % num_columns]
                user_data_main = random.choice(user_data)
                column.write(user_data_main.get('title'))
                column.write(user_data_main.get('year'))
                column.image(user_data_main.get('thumb'),width=100)
            # st.image(search_releases(user_input),width=100)
        else:
            st.write("No data found")