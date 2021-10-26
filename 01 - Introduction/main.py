from fastapi import FastAPI
from fastapi.responses import HTMLResponse



app = FastAPI()


@app.get('/', response_class=HTMLResponse)
def hello_world():
    return '<h1>Hello World</h1>'

@app.get('/about/{username}', response_class=HTMLResponse)
def about_page(username):
    return f'<h1>This is the about page of {username}</h1>'
