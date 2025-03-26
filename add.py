import streamlit as st

def add_movie_page():
    st.title("🎬 Add a New Movie")
    st.write("Enter the details of the movie below:")

    # 🔹 Title & Release Year in One Row
    col1, col2 = st.columns(2)
    with col1:
        title = st.text_input(" Movie Title", placeholder="Enter the movie title")
    with col2:
        release_year = st.number_input(" Release Year", min_value=1900, max_value=2100, step=1)

    # 🔹 Genre Selection & Rating in One Row
    genres = ["Action", "Comedy", "Drama", "Horror", "Romance", "Sci-Fi", "Thriller", "Animation", "Fantasy", "Mystery"]
    col1, col2, col3 = st.columns(3)
    with col1:
        selected_genre1 = st.selectbox(" Genre 1", ["Select"] + genres)
    with col2:
        selected_genre2 = st.selectbox(" Genre 2", ["Select"] + genres)
    with col3:
        rating = st.slider("⭐ Rating", min_value=0.0, max_value=10.0, step=0.1)

    # 🔹 Review Input
    review = st.text_area(" Write a Review", placeholder="Share your thoughts about the movie")

    # 🔹 Submit Button
    if st.button("Submit Movie"):
        if not title:
            st.error("❌ Please enter a movie title.")
        elif not release_year:
            st.error("❌ Please enter a valid release year.")
        elif selected_genre1 == "Select" and selected_genre2 == "Select":
            st.error("❌ Please select at least one genre.")
        else:
            st.success(f" Movie '{title}' ({release_year}) added successfully! 🎉")
            st.write(f"** Genres:** {', '.join([g for g in [selected_genre1, selected_genre2] if g != 'Select'])}")
            st.write(f"**⭐ Rating:** {rating}/10")
            if review:
                st.write(f"** Review:** {review}")

# Run the page🎭✅🎭📅📝📝🎥
if __name__ == "__main__":
    add_movie_page()
