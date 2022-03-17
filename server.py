
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:3000",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/')
def home():
    return {'hello': 'world'}



@app.post('/start')
def start():
    return {'ack': True}



@app.post('/pause')
def pause():
    return {'ack': True}



@app.post('/stop')
def stop():
    return {'ack': True}



@app.get('/stream')
def stream():
    return {'ack': True}