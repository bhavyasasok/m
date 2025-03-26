import streamlit as st
import requests

# ✅ DO NOT INCLUDE `st.set_page_config()` HERE

# ✅ Fetch TMDb API Key
API_KEY = st.secrets["tmdb_api_key"]
BASE_URL = "https://api.themoviedb.org/3"

# ✅ Fetch Genres from TMDb API
@st.cache_data
def fetch_tmdb_genres():
    url = f"{BASE_URL}/genre/movie/list?api_key={API_KEY}&language=en-US"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return {genre['id']: genre['name'] for genre in response.json().get('genres', [])}
    except requests.RequestException as e:
        st.error(f"Error fetching genres: {e}")
        return {}

# ✅ Fetch Available Years
@st.cache_data
def fetch_available_years():
    return [str(year) for year in range(2025, 1950, -1)]

# ✅ Fetch Movies
@st.cache_data
def fetch_movies(query="", genre_id=None, release_year=None):
    url = f"{BASE_URL}/search/movie?api_key={API_KEY}&query={query}&language=en-US" if query else f"{BASE_URL}/discover/movie?api_key={API_KEY}&language=en-US"
    params = {}
    if genre_id:
        params["with_genres"] = genre_id
    if release_year:
        params["primary_release_year"] = release_year

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json().get("results", [])
    except requests.RequestException as e:
        st.error(f"Error fetching movies: {e}")
        return []

# ✅ Search Page Function
def search_page():
    st.markdown("<h1 style='text-align: center; font-family: Cinzel, serif; color: #ffcc00;'></h1>", unsafe_allow_html=True)

    # ✅ Fetch Genres & Years
    genres = fetch_tmdb_genres()
    years = fetch_available_years()

    # ✅ Filters in One Row
    col1, col2, col3 = st.columns(3)

    with col1:
        selected_movie = st.text_input(" Filter by Name", "")

    with col2:
        selected_genre = st.selectbox(" Filter by Genre", ["All"] + list(genres.values()))
        genre_id = next((gid for gid, gname in genres.items() if gname == selected_genre), None)

    with col3:
        selected_year = st.selectbox(" Filter by Year", ["All"] + years)
        release_year = selected_year if selected_year != "All" else None

    # ✅ Fetch Movies Based on Filters📅🎭🎥🔍🔥⚠️
    with st.spinner(' Searching for movies...'):
        movies = fetch_movies(query=selected_movie, genre_id=genre_id, release_year=release_year)

    # ✅ Display Movies
    if movies:
        st.subheader(" Search Results")
        cols = st.columns(4)
        for i, movie in enumerate(movies[:12]):
            with cols[i % 4]:
                title = movie.get("title", "Unknown Title")
                poster = f"https://image.tmdb.org/t/p/w500{movie.get('poster_path', '')}" if movie.get('poster_path') else "https://via.placeholder.com/250x375"

                st.markdown(f"**{title}**")  # Display title as plain text
                st.image(poster, use_container_width=True)  # Fixed deprecation warning
                st.caption(f"📅 {movie.get('release_date', 'Unknown')[:4]} | 🎭 {selected_genre if selected_genre != 'All' else 'Multiple Genres'}")
    else:
        st.warning("⚠️ No movies found.")

# ✅ Run search_page when executed directly
if __name__ == "__main__":
    search_page()
