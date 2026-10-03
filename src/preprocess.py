import pandas as pd
import ast

# Load datasets
movies = pd.read_csv("data/tmdb_5000_movies.csv")
credits = pd.read_csv("data/tmdb_5000_credits.csv")

# Merge both datasets
movies = movies.merge(
    credits,
    left_on="id",
    right_on="movie_id"
)

# Keep useful columns
movies = movies[
    [
        "id",
        "title_x",
        "genres",
        "keywords",
        "overview",
        "cast",
        "crew",
        "vote_average",
        "vote_count",
        "popularity"
    ]
]

# Rename title column
movies.rename(columns={"title_x": "title"}, inplace=True)


# Convert JSON-like columns into useful text
def convert_to_names(text):
    try:
        data = ast.literal_eval(text)
        return " ".join(item["name"].replace(" ", "") for item in data)
    except:
        return ""


movies["genres"] = movies["genres"].apply(convert_to_names)
movies["keywords"] = movies["keywords"].apply(convert_to_names)


# Extract top 3 actors
def convert_cast(text):
    try:
        data = ast.literal_eval(text)
        return " ".join(
            item["name"].replace(" ", "")
            for item in data[:3]
        )
    except:
        return ""


movies["cast"] = movies["cast"].apply(convert_cast)


# Extract director
def get_director(text):
    try:
        data = ast.literal_eval(text)

        for item in data:
            if item["job"] == "Director":
                return item["name"].replace(" ", "")

        return ""
    except:
        return ""


movies["crew"] = movies["crew"].apply(get_director)


# Handle missing overview
movies["overview"] = movies["overview"].fillna("")


# Create combined feature
movies["tags"] = (
    movies["overview"]
    + " "
    + movies["genres"]
    + " "
    + movies["keywords"]
    + " "
    + movies["cast"]
    + " "
    + movies["crew"]
)


# Convert tags to lowercase
movies["tags"] = movies["tags"].str.lower()


# Remove unnecessary columns
movies = movies[
    [
        "id",
        "title",
        "vote_average",
        "vote_count",
        "popularity",
        "tags"
    ]
]


# Save processed dataset
movies.to_csv(
    "data/processed_movies.csv",
    index=False
)

print("Preprocessing completed successfully!")
print("Processed movies:", movies.shape)
print("File saved: data/processed_movies.csv")