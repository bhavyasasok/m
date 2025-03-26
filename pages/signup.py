import streamlit as st

def signup_page():
    st.title("User Signup")

    # Initialize session state📝 
    if "users" not in st.session_state:
        st.session_state.users = {}  # Dictionary to store registered users
    if "page" not in st.session_state:
        st.session_state.page = "signup"

    username = st.text_input("Enter a username")
    password = st.text_input("Enter a password", type="password")
    confirm_password = st.text_input("Confirm password", type="password")

    if st.button("Sign Up"):
        if username in st.session_state.users:
            st.error("❌ Username already exists. Choose another one.")
        elif password != confirm_password:
            st.error("❌ Passwords do not match.")
        elif username and password:
            st.session_state.users[username] = password
            st.success("✅ Signup successful! Redirecting to login...")
            st.session_state.page = "login"  # Redirect to login page
            st.rerun()
        else:
            st.error("❌ Please fill in all fields.")

    # Provide Login Option
    st.markdown("---")
    st.write("Already have an account?")
    if st.button("Login here"):
        st.session_state.page = "login"  # Redirect back to login page
        st.rerun()

if __name__ == "__main__":
    signup_page()
