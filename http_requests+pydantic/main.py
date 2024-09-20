from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict

app = FastAPI()

# User model
from typing import Optional

class User(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None

# In-memory "database"
db: Dict[int, User] = {}
user_id_counter = 1

@app.get("/users/{user_id}")
async def get_user(user_id: int):
    user = db.get(user_id)
    if user:
        return {"user_id": user_id, "name": user.name, "email": user.email}
    raise HTTPException(status_code=404, detail="User not found")

@app.post("/users/")
async def create_user(user: User):
    global user_id_counter
    db[user_id_counter] = user
    user_id_counter += 1
    return {"msg": "User created", "user_id": user_id_counter - 1, "name": user.name, "email": user.email}

@app.put("/users/{user_id}")
async def update_user(user_id: int, user: User):
    if user_id in db:
        db[user_id] = user
        return {"msg": "User updated", "user_id": user_id, "name": user.name, "email": user.email}
    raise HTTPException(status_code=404, detail="User not found")

@app.patch("/users/{user_id}")
async def patch_user(user_id: int, user: User):
    if user_id in db:
        existing_user = db[user_id]
        if user.name:
            existing_user.name = user.name
        if user.email:
            existing_user.email = user.email
        return {"msg": "User updated", "user_id": user_id, "name": existing_user.name, "email": existing_user.email}
    raise HTTPException(status_code=404, detail="User not found")

@app.delete("/users/{user_id}")
async def delete_user(user_id: int):
    if user_id in db:
        del db[user_id]
        return {"msg": "User deleted", "user_id": user_id}
    raise HTTPException(status_code=404, detail="User not found")

@app.head("/users/{user_id}")
async def head_user(user_id: int):
    # Simply return a response with status code 200 if the user exists
    if user_id in db:
        return {"msg": "User exists"}
    raise HTTPException(status_code=404, detail="User not found")

@app.options("/users/{user_id}")
async def options_user(user_id: int):
    return {
        "allowed_methods": ["GET", "POST", "PUT", "PATCH", "DELETE"]
    }