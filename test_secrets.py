import streamlit as st

if "tmdb_api_key" in st.secrets:
    print("✅ API Key Found:", st.secrets["tmdb_api_key"])
else:
    print("❌ API Key NOT Found in secrets.toml")
