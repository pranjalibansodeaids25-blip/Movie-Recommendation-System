import streamlit as st
from src.recommendation import recommend

st.set_page_config(
    page_title="AI Movie Recommendation System",
    page_icon="🎬",
    layout="centered"
)

st.title("🎬 AI Movie Recommendation System")
st.write("Find movies similar to your favorite movie using Machine Learning.")

movie_title = st.text_input(
    "Enter a movie name",
    placeholder="Example: Avatar"
)

number_of_movies = st.slider(
    "Number of recommendations",
    min_value=3,
    max_value=10,
    value=5
)

if st.button("🎯 Recommend Movies"):

    if movie_title.strip() == "":
        st.warning("Please enter a movie name.")

    else:
        recommendations = recommend(
            movie_title,
            number_of_movies
        )

        if recommendations:

            st.subheader(
                f"Movies similar to {movie_title.title()}"
            )

            for i, (title, score) in enumerate(
                recommendations,
                start=1
            ):
                st.write(
                    f"**{i}. {title}**"
                )
                st.caption(
                    f"Similarity Score: {score}"
                )

        else:
            st.error(
                "Movie not found. Please check the movie name."
            )