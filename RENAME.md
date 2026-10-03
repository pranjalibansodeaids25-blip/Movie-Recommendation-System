# 🎬 AI-Based Movie Recommendation System

An AI-based movie recommendation system built using Python, Machine Learning, Streamlit, Docker, and Git.

## 📌 Project Overview

This project recommends movies similar to a movie selected by the user.

The system uses **Content-Based Filtering** with **TF-IDF Vectorization** and **Cosine Similarity** to find movies with similar content.

## 🚀 Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Docker
- Git & GitHub

## 🧠 Machine Learning

The recommendation engine uses:

1. Movie metadata preprocessing
2. TF-IDF Vectorization
3. Cosine Similarity
4. Content-Based Recommendation

## ✨ Features

- Search for a movie
- Get similar movie recommendations
- Select number of recommendations
- Display similarity scores
- Interactive Streamlit interface

## 📂 Project Structure

```text
Movie-Recommendation-System/
│
├── data/
│   ├── tmdb_5000_movies.csv
│   ├── tmdb_5000_credits.csv
│   └── processed_movies.csv
│
├── src/
│   ├── preprocess.py
│   └── recommendation.py
│
├── app.py
├── requirements.txt
├── .gitignore
├── Dockerfile
└── README.md
