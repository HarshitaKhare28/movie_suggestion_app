from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import random
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
def serve_frontend():
    return FileResponse(os.path.join("static", "index.html"))

# Movie data
movie_db = {
    "action": ["Mad Max: Fury Road", "John Wick", "Die Hard", "The Dark Knight"],
    "comedy": ["The Hangover", "Superbad", "Step Brothers", "The Grand Budapest Hotel"],
    "romance": ["The Notebook", "Pride & Prejudice", "La La Land", "Titanic"],
    "sci-fi": ["Inception", "Interstellar", "The Matrix", "Arrival"]
}

@app.get("/movies")
def get_movies(genre: str = Query(..., description="Genre like action, comedy, romance")):
    genre = genre.lower()
    if genre in movie_db:
        return {"genre": genre, "movies": random.sample(movie_db[genre], k=min(3, len(movie_db[genre])))}
    else:
        return {"genre": genre, "movies": []}
