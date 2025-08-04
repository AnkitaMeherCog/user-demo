# user-demo

This project demonstrates a simple CRUD API built with **FastAPI** using a
SQLite database. The API allows creating, reading, updating and deleting user
records.

## Setup

Install the required dependencies:

```bash
pip install -r requirements.txt
```

Run the development server:

```bash
uvicorn app.main:app --reload
```

The API will be available at `http://127.0.0.1:8000`.

## Third-party endpoint demo

For demonstration purposes, the API can proxy requests to the open
[JSONPlaceholder](https://jsonplaceholder.typicode.com/) service:

- `GET /thirdparty/posts/{post_id}` fetches a post from JSONPlaceholder.
- `POST /thirdparty/posts` creates a post on JSONPlaceholder and returns the
  created resource.

## Packaging as a zip application

Python's `zipapp` module can be used to bundle the project into a single
executable archive:

```bash
python -m zipapp . -p "$(which python)" -o demo_app.pyz
```

Start the app with:

```bash
python demo_app.pyz
```


## Local Run
1. python -m venv .venv && source .venv/bin/activate  # Mac
2. pip install -r requirements.txt
3. uvicorn app.main:app --reload --port 8002