from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import ZODB, ZODB.FileStorage
import transaction
from BTrees.OOBTree import OOBTree

app = FastAPI()

storage = ZODB.FileStorage.FileStorage('database.fs')
db = ZODB.DB(storage)
connection = db.open()
root = connection.root()


if not hasattr(root, 'users'):
    root.users = OOBTree()
    transaction.commit()


class UserData(BaseModel):
    username: str
    password: str


@app.post("/register")
def register(user: UserData):
    
    if user.username in root.users:
        raise HTTPException(status_code=400, detail="Username already exists")
    
    root.users[user.username] = {"password": user.password}
    transaction.commit() 
    
    print(f"Server: Registered new user '{user.username}'")
    return {"status": "success"}


@app.post("/login")
def login(user: UserData):
   
    if user.username not in root.users:
        raise HTTPException(status_code=401, detail="User not found")
    
    if root.users[user.username]["password"] != user.password:
        raise HTTPException(status_code=401, detail="Incorrect password")
    
    print(f"Server: '{user.username}' logged in successfully.")
    return {"status": "success"}