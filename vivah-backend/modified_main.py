
from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from passlib.hash import bcrypt
from fastapi.middleware.cors import CORSMiddleware

from sqlalchemy.orm import Session

app = FastAPI()

# CORS Configuration
origins = ["http://localhost:3000"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependency to get the DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Updated UserCreate model
class UserCreate(BaseModel):
    name: str
    email: str
    password: str
    gender: str
    date_of_birth: str
    marital_status: str
    religion: str
    caste: str
    mother_tongue: str
    country: str
    state: str
    city: str

@app.post("/api/register")
async def register_user(user: UserCreate, db: Session = Depends(get_db)):
    hashed_password = bcrypt.hash(user.password)
    db_user = User(
        email=user.email,
        password=hashed_password,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    
    # Adding basic info
    basic_info = BasicInfo(
        user_id=db_user.id,
        full_name=user.name,
        gender=user.gender,
        date_of_birth=user.date_of_birth,
        marital_status=user.marital_status,
        religion_id=int(user.religion),  # Assuming ID is provided, can be modified to fetch by name
        caste_id=int(user.caste),
        mother_tongue_id=int(user.mother_tongue),
        country_id=int(user.country),
        state_id=int(user.state),
        city_id=int(user.city)
    )
    db.add(basic_info)
    db.commit()
    
    return {"message": "User registered successfully"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
