from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import ZODB, ZODB.FileStorage
import transaction
from BTrees.OOBTree import OOBTree
from classFiles.RoomClass import RoomObj
from typing import List
from classFiles.UserClass import User

app = FastAPI()

storage = ZODB.FileStorage.FileStorage('database.fs')
db = ZODB.DB(storage)
connection = db.open()
root = connection.root()


if not hasattr(root, 'users'):
    root.users = OOBTree()
    transaction.commit()

class UserData(BaseModel):
    username: strf
    password: str

class UserSchema(BaseModel):
    username: str  
    gmail: str
    phone: str
    password: str
    id: int
    rooms: List[dict] = []

@app.post("/register")
def register(data: UserSchema):
    
    if data.name in root.users:
            raise HTTPException(status_code=400, detail="Username already exists")

    new_user = User(
        gmail=data.gmail,
        name=data.username,
        id=data.id,
        pno=data.phone,
        memOf=[] 
    )

    new_user.password = data.password 

    root.users[data.name] = new_user
    transaction.commit()

    return {"status": "success", "message": f"User {data.name} created"}


@app.post("/login")
def login(user: UserData):
   
    if user.username not in root.users:
        raise HTTPException(status_code=401, detail="User not found")
    
    user_obj = root.users[user.username]
    if user_obj.password != user.password:
        raise HTTPException(status_code=401, detail="Incorrect password")
    
    print(f"Server: '{user.username}' logged in successfully.")
    return {
            "status": "success",
            "user_data": user_obj.to_dict() 
        }
