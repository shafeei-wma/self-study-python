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
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
class Item(BaseModel):
 myKey : object # Excpecting key datas in object receive from client

@app.get("/")
async def read_root(): # async allow route to handle multiple requests at the same time without blocking
 return {"Hello": "World"}

@app.post("/new")
async def post_example(item: Item):
 var1 = 'Data'
 return { 'msg': f"{var1} retreived!", 'res': item}