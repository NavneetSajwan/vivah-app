from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from passlib.hash import bcrypt
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS Configuration
origins = ["http://localhost:3000"]  # Replace with your frontend's domain
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class UserCreate(BaseModel):
    name: str
    email: str
    password: str

fake_users_db = []

@app.post("/api/register")
async def register_user(user: UserCreate):
    hashed_password = bcrypt.hash(user.password)
    user_dict = user.dict()
    user_dict["password"] = hashed_password
    fake_users_db.append(user_dict)
    return {"message": "User registered successfully"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
