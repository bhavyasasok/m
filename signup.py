import streamlit as st

# Set page background color
st.markdown("""
    <style>
        body {
            background-color: navy;
        }
        .stApp {
            background-color: navy;
        }
        h1 {
            color: white !important;
        }
        label {
            color: white !important;
        }
        input {
            color: white !important;
            background-color: black !important;
        }
    </style>
""", unsafe_allow_html=True)

# Signup function
def signup():
    st.title("User Signup")
    
    if "users" not in st.session_state:
        st.session_state.users = {}
    
    username = st.text_input("Enter a username")
    password = st.text_input("Enter a password", type="password")
    confirm_password = st.text_input("Confirm password", type="password")
    
    if st.button("Sign Up"):
        if username in st.session_state.users:
            st.error("Username already exists. Please choose a different one.")
        elif password != confirm_password:
            st.error("Passwords do not match. Please try again.")
        elif username and password:
            st.session_state.users[username] = password
            st.success("Signup successful! You can now log in.")
            st.switch_page("pages/login.py")
        else:
            st.error("Please enter a valid username and password.")
    
    if st.button("Already have an account? Login"):
        st.switch_page("pages/login.py")

if __name__ == "__main__":
    signup()
