import streamlit as st
import requests
import random
from streamlit.components.v1 import html
import streamlit.components.v1 as components
from pages import login, signup  # Ensure these exist in the 'pages' folder
import search  # Import search module

# ✅ Set Page Configuration (MUST be the first Streamlit command)
st.set_page_config(page_title="CINE.ARC", page_icon="🎬", layout="wide", initial_sidebar_state="collapsed")

# ✅ Initialize session state variables
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "users" not in st.session_state:
    st.session_state.users = {}  # Stores registered users
if "page" not in st.session_state:
    st.session_state.page = "home"  # Default page is Home

# ✅ Redirect to Login/Signup Page when Clicked
if st.session_state.page == "login":
    login.login_page()
    st.stop()  # Prevents running the rest of the script when on login page
elif st.session_state.page == "signup":
    signup.signup_page()
    st.stop()



st.markdown("""
    <style>
        
        [data-testid="stSidebarNav"] ul {display: none;}
        [data-testid="stAppViewContainer"] > section {padding-top: 0px;}
        
        [data-testid="stSidebarNav"] ul {display: none;}
        [data-testid="stAppViewContainer"] > section {padding-top: 0px;}
        [data-testid="stSidebar"] {display: none !important;}  /* Hides Sidebar */

        /* Top Bar with Title and Login */
        .top-bar {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 10px 20px;
        }

        /* Elegant Title Styling */
        .cinearc-title { 
    text-align: center; 
    font-size: 50px; 
    font-weight: bold; 
    font-family: 'Cinzel', serif;
    color: #ffcc00;
    letter-spacing: 3px;
    margin-top: -20px; /* Reduce the gap */
}

        /* Login Button Styling */
        .login-button {
            background-color: #ff6600;
            color: white;
            padding: 8px 15px;
            font-size: 16px;
            font-weight: bold;
            border: none;
            border-radius: 20px;
            cursor: pointer;
        }
        .login-button:hover {
            background-color: #ff4500;
        }

        /* Recommended Movies Styling */
        .recommend-title {
            text-align: center;
            font-size: 30px;
            font-weight: bold;
            font-family: 'Poppins', sans-serif;
            color: #ffcc00;
            text-shadow: 1px 1px 4px rgba(255, 204, 0, 0.5);
            margin-top: 20px;
        }
          .footer-container {
            width: 100%;
            background-color: #1e1e1e;
            color: white;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0px 4px 10px rgba(255, 255, 255, 0.1);
            display: flex;
            justify-content: space-between;
            flex-wrap: wrap;
        }
        .footer-section {
            flex: 1;
            min-width: 250px;
            padding: 10px;
        }
        .footer-title {
            color: #ffcc00;
            margin-bottom: 5px;
        }
        .footer-text a {
            color: #ffcc00;
            text-decoration: none;
        }
        .footer-text a:hover {
            text-decoration: underline;
        }
   
    </style>
   # <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@600&family=Poppins:wght@500&display=swap" rel="stylesheet">
    """, unsafe_allow_html=True)

# 🔹 Title & Login Button (Top Right Corner)
col1, col2 = st.columns([8, 1])  # Adjust spacing between title & login button🔑
with col1:
    st.markdown("<div class='cinearc-title'>🎬 CINE.ARC</div>", unsafe_allow_html=True)
with col2:
    if not st.session_state.logged_in:
        if st.button("Login", key="login_btn"):
            st.session_state.page = "login"
            st.rerun()  # Redirects to the login page


# 🔹 Main Tabs
tab1, tab2, tab3 = st.tabs(["Home", "Search", "Add Movies"])

# ✅ Home Tab
with tab1:
    def display_carousel():
        carousel_html = """
        <div id="fullpage-carousel" class="carousel slide" data-bs-ride="carousel" style="width: 100vw; height: 100vh; overflow: hidden;">
          <div class="carousel-inner">
            <div class="carousel-item active">
              <a href="https://www.imdb.com/title/tt0120338/" target="_blank">
                <img src="https://www.themoviedb.org/t/p/original/vIAm7UDNjGztvUYtDuS0in1VAXg.jpg" class="d-block w-100" style="object-fit: cover; width: 100vw; height: 100vh;" alt="Titanic">
              </a>
            </div>
            <div class="carousel-item">
              <a href="https://www.imdb.com/title/tt0499549/" target="_blank">
                <img src="https://wallpapercave.com/wp/wp9424696.jpg" class="d-block w-100" style="object-fit: cover; width: 100vw; height: 100vh;" alt="Avatar">
              </a>
            </div>
            <div class="carousel-item">
              <a href="https://www.imdb.com/title/tt4154796/" target="_blank">
                <img src="https://pbs.twimg.com/media/D2jvOdmUgAALnnx.jpg" class="d-block w-100" style="object-fit: cover; width: 100vw; height: 100vh;" alt="Avengers: Endgame">
              </a>
            </div>
            <div class="carousel-item">
              <a href="https://www.imdb.com/title/tt2283362/" target="_blank">
                <img src="https://goggler.my/wp-content/uploads/2019/12/JM2_INTL_30Sht_BRIDGE_03-e1575889045252.jpg" class="d-block w-100" style="object-fit: cover; width: 100vw; height: 100vh;" alt="Jumanji">
              </a>
            </div>
            <div class="carousel-item">
              <a href="https://www.imdb.com/title/tt26584495/" target="_blank">
                <img src="https://assets-in.bmscdn.com/discovery-catalog/events/et00414405-xsldnanrnl-landscape.jpg" class="d-block w-100" style="object-fit: cover; width: 100vw; height: 100vh;" alt="Movie 2">
              </a>
            </div>
            <div class="carousel-item">
              <a href="https://www.imdb.com/title/tt28630624/" target="_blank">
                <img src="https://cms.dmpcdn.com/movie/2025/01/17/c0a5c2e0-d46c-11ef-bc18-87acef2f0d44_webp_original.webp" class="d-block w-100" style="object-fit: cover; width: 100vw; height: 100vh;" alt="Movie 3">
              </a>
            </div>
          </div>
          <button class="carousel-control-prev" type="button" data-bs-target="#fullpage-carousel" data-bs-slide="prev">
            <span class="carousel-control-prev-icon" aria-hidden="true"></span>
            <span class="visually-hidden">Previous</span>
          </button>
          <button class="carousel-control-next" type="button" data-bs-target="#fullpage-carousel" data-bs-slide="next">
            <span class="carousel-control-next-icon" aria-hidden="true"></span>
            <span class="visually-hidden">Next</span>
          </button>
        </div>

        <script>
          var myCarousel = new bootstrap.Carousel(document.querySelector('#fullpage-carousel'), {
            interval: 2000,
            wrap: true
          });
        </script>

        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
        """
        components.html(carousel_html, height=700)


    display_carousel()

    @st.cache_data
    def fetch_trending_movies():
        try:
            api_key = st.secrets["tmdb_api_key"]
            url = f"https://api.themoviedb.org/3/trending/movie/week?api_key={api_key}"
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            movies = data.get("results", [])
            return [
                {"title": movie["title"], 
                 "poster_url": f"https://image.tmdb.org/t/p/w500{movie['poster_path']}", 
                 "tmdb_url": f"https://www.themoviedb.org/movie/{movie['id']}"}
                for movie in movies if movie.get("poster_path")
            ]
        except requests.RequestException as e:
            st.error(f"Error fetching movies: {e}")
            return []

    # Recommended Movies Section
    st.markdown('<div class="recommend-title">Recommended Movies</div>', unsafe_allow_html=True)

    trending_movies = fetch_trending_movies()
    recommendations = random.sample(trending_movies, min(12, len(trending_movies)))
    cols = st.columns(4)

    for i, movie in enumerate(recommendations):
        with cols[i % 4]:
            st.markdown(f"""
                <div style="text-align: center; padding: 10px;">
                    <a href="{movie['tmdb_url']}" target="_blank">
                        <img src="{movie['poster_url']}" width="250">
                    </a>
                    <p style="font-family: 'Poppins', sans-serif; font-size: 18px; font-weight: bold; color: #ffcc00;"><strong>{movie['title']}</strong></p>
                </div>
            """, unsafe_allow_html=True)

# ✅ Search Tab
with tab2:
    try:
        import search
        search.search_page()
    except ImportError:
        st.error("Error loading search module. Ensure 'search.py' exists.")

# ✅ Add Movies Tab
with tab3:
    try:
        import add
        add.add_movie_page()
    except ImportError:
        st.error("Error loading add module. Ensure 'add.py' exists.")

# Footer 📜📞📝 


# Footer Container Styling
st.markdown("<br><br>", unsafe_allow_html=True)

# Create three columns: col1 (Support), spacer (col_space), col2 (Terms & Privacy)
col1, col_space, col2 = st.columns([1, 0.5, 1])  # Adjust the middle column width for spacing

with col1:
    st.markdown("### Support")
    st.write(
        "Need help? Visit our [Help Center](https://support.cinearc.com) "
        "or email us at [support@cinearc.com](mailto:support@cinearc.com)."
    )

with col2:
    st.markdown("### Terms & Privacy")
    st.write(
        "Read our [Terms of Service](https://cinearc.com/terms) and "
        "[Privacy Policy](https://cinearc.com/privacy) for more details."
    )

st.markdown("<br><br>", unsafe_allow_html=True)

# Feedback Section


# ✅ Ensure session state is initialized


# Ensure session state is initialized
if "feedback_input" not in st.session_state:
    st.session_state.feedback_input = ""

st.markdown("<h3 style='text-align: center; color: white;'>We Value Your Feedback</h3>", unsafe_allow_html=True)

# Text area using session state
feedback = st.text_area("Write your feedback...", key="feedback_input")

if st.button("Submit Feedback"):
    if feedback.strip():
        st.success("Thank you for your feedback!")

        # ✅ Correct way to reset session state variable
        del st.session_state["feedback_input"]  # Remove variable
        st.rerun()  # ✅ Updated function to refresh UI
    else:
        st.error("Please enter some feedback before submitting.")
