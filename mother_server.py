import os 
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, ConfigDict
import ZODB, ZODB.FileStorage
import transaction
from BTrees.OOBTree import OOBTree
from typing import List
from classFiles.UserClass import User

app = FastAPI()

db_path = "/data/database.fs" if os.path.exists("/data") else "database.fs"
storage = ZODB.FileStorage.FileStorage(db_path)
db = ZODB.DB(storage)
connection = db.open()
root = connection.root()


if not hasattr(root, 'users'):
    root.users = OOBTree()
    transaction.commit()

class UserData(BaseModel):
    username: str
    password: str

class UserSchema(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)
    username: str  
    gmail: str
    phone: str
    password: str
    id: int
    rooms: List[dict] = []

@app.post("/register")
def register(data: UserSchema):
    
    if data.username in root.users:
            raise HTTPException(status_code=400, detail="Username already exists")

    new_user = User(
        gmail=data.gmail,
        name=data.username,
        id=data.id,
        pno=data.phone,
        memOf=[] 
    )

    new_user.password = data.password 

    root.users[data.username] = new_user
    transaction.commit()

    return {"status": "success", "message": f"User {data.username} created"}


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


@app.get("/users/all")
def get_all_users():
    all_users_list = []

   
    for username, user_obj in root.users.items():
        try:
            
            if hasattr(user_obj, 'to_dict'):
                user_data = user_obj.to_dict()
            else:
              
                user_data = {
                    "username": username,
                    "note": "Old data format (missing fields)"
                }
            all_users_list.append(user_data)
            
        except Exception as e:
            print(f"Error processing user {username}: {e}")
            continue

   
    return {
        "total_users": len(all_users_list),
        "users": all_users_list
    }
