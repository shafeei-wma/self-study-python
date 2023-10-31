# Flask old method run server
# run server by type this in terminal --> python server.py  OR python server.py runserver
# from flask import Flask
# app = Flask(__name__)

# @app.route('/')
# def home():
#     return "Hello, World!"

# if __name__ == '__main__':
#     app.run(port=8000)

# FastApi method
# python -m uvicorn server:app --reload
from fastapi import FastAPI, HTTPException, Depends, Request
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from dotenv import load_dotenv
import os
from settings import settings
from database import init_db
from database import manual_query
from models import Note
from tortoise.exceptions import IntegrityError


load_dotenv()
app = FastAPI(title="fastapi-gcp")
init_db(app)

class Item(BaseModel):
 myKey : object # Excpecting key datas in object receive from client

class CreateNotePayload(BaseModel):
    filename: str
    title: str
    content: str


@app.get("/", response_class=HTMLResponse)
async def read_root(): # async allow route to handle multiple requests at the same time without blocking
#  return {"Hello": "World"}
 a1 = "Hello!"
 a2= os.getenv('DB_NAME')
 #  alternative
 a3= settings.DB_NAME
 return f"<h1>Python Test Page!</h2>{a1} | {a2} | {a3}"

@app.post("/new")
async def post_example(item: Item):
 var1 = 'Data'
 return { 'msg': f"{var1} retreived!", 'res': item}

@app.post("/other")
async def post_example(request: Request):
 item = await request.json()  # Extract JSON from the request body as a python dictionary
 print(item["name"]) # Harry Potter
 return { 'msg': "Data retreived!", 'res': item}

# interaction with postgresql db
@app.post("/notes")
async def create_note(payload: CreateNotePayload):
    try:
      note = await Note.create(**payload.model_dump())
      return {"message": f"Note created successfully with id {note.id}"}
    except IntegrityError:
      raise HTTPException(status_code=400, detail="Note with this title already exists")

@app.get("/notes/str/{title}")
async def get_note_by_title(title: str):
    if not (note := await Note.get_or_none(title=title)):
        raise HTTPException(status_code=404, detail="Note not found")
    return note.id

@app.get("/notes/json")
async def get_note_by_title(request: Request):
    item = await request.json()  # Extract JSON from the request body as a python dictionary
    if not (note := await Note.get_or_none(title=item['title'])):
      raise HTTPException(status_code=404, detail="Note not found")
    return note.id

@app.get("/notes/query/")
async def get_note_by_title(request: Request):
    item = await request.json() 
    query = f"select * from note where title = '{item['title']}'"
    res = await manual_query(query)
    return res