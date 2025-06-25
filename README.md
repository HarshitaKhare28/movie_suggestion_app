# 🎬 Movie Suggestion Page

A simple web page built with **FastAPI** and **Tailwind CSS** that gives random movie suggestions based on the selected genre.

## 🔧 Tech Used

- **FastAPI** (Python) – for serving movie suggestions
- **HTML + Tailwind CSS** – for the frontend UI

## 🗂️ Structure

```
movie_suggestion_app/
├── main.py               # FastAPI backend
└── static/
    └── index.html        # Frontend page
```

## ▶️ How to Run

1. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv env
   env\Scripts\activate  # On Windows
   ```

2. Install dependencies:
   ```bash
   pip install fastapi uvicorn
   ```

3. Run the server:
   ```bash
   uvicorn main:app --reload
   ```

4. Open in your browser:
   ```
   https://movie-suggestion-app.onrender.com
   ```

---

