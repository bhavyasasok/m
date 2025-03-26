import streamlit as st

def login_page():
    
    st.title(" User Login")

    # Initialize session state 🔑
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False
    if "users" not in st.session_state:
        st.session_state.users = {}  # Stores registered users
    if "page" not in st.session_state:
        st.session_state.page = "login"  # Default page is login

    # Show login fields if user is not logged in
    if not st.session_state.logged_in:
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

        if st.button("Login"):
            if username in st.session_state.users and st.session_state.users[username] == password:
                st.session_state.logged_in = True
                st.success("✅ Login successful! Redirecting to home...")
                st.session_state.page = "home"  # Redirect to home page
                st.rerun()
            else:
                st.error("❌ Invalid username or password")

    else:
        st.success("✅ You are already logged in!")

    # Sign Up Button
    st.markdown("---")
    st.write("Not registered?")
    if st.button("Sign up here"):
        st.session_state.page = "signup"  # Redirect to Signup page
        st.rerun()

if __name__ == "__main__":
    login_page()
