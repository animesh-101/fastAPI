# to run the server use command 'fastapi dev main.py'


from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

posts : list[dict] = [
    {
        "id": 1,
        "author": "Animesh Raj",
        "title": "First FastAPI Post",
        "content": "This is the content of the first post.",
        "date_posted": "2024-06-01"
    },
    {
        "id": 2,
        "author": "Animesh Raj",
        "title": "Second FastAPI Post",
        "content": "This is the content of the second post.",
        "date_posted": "2024-06-02"
    },
]


# We can add to routes to display the same content in the HTML format. 
@app.get("/", response_class = HTMLResponse, include_in_schema=False) # this is to specify that the response will be in HTML format
@app.get("/posts", response_class = HTMLResponse, include_in_schema=False) # this is to specify that the response will be in HTML format
def home():
    return f"<h1>{posts[0]['title']} by {posts[0]['author']}</h1>"

@app.get("/api/posts")
def get_posts():
    return posts