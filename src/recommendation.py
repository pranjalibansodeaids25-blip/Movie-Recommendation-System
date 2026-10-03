import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load processed dataset
movies = pd.read_csv("data/processed_movies.csv")

# Replace missing tags with empty string
movies["tags"] = movies["tags"].fillna("")

# Convert text into TF-IDF vectors
tfidf = TfidfVectorizer(
    max_features=5000,
    stop_words="english"
)

tfidf_matrix = tfidf.fit_transform(movies["tags"])

# Calculate similarity between movies
similarity = cosine_similarity(tfidf_matrix)


def recommend(movie_title, number_of_recommendations=5):
    movie_title = movie_title.lower()

    # Find matching movie
    matches = movies[
        movies["title"].str.lower() == movie_title
    ]

    if matches.empty:
        return []

    movie_index = matches.index[0]

    # Get similarity scores
    similarity_scores = list(
        enumerate(similarity[movie_index])
    )

    # Sort by similarity
    similarity_scores = sorted(
        similarity_scores,
        key=lambda x: x[1],
        reverse=True
    )

    # Get top recommendations
    recommendations = []

    for index, score in similarity_scores[1:number_of_recommendations + 1]:
        recommendations.append(
            (
                movies.iloc[index]["title"],
                round(score, 3)
            )
        )

    return recommendations


# Test the recommendation system
if __name__ == "__main__":
    movie = "Avatar"

    recommendations = recommend(movie)

    print(f"\nRecommendations for: {movie}\n")

    if recommendations:
        for title, score in recommendations:
            print(f"{title}  |  Similarity: {score}")
    else:
        print("Movie not found.")