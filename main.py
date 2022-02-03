#Python
from uuid import UUID
from datetime import date, datetime
from typing import Optional

#Pydantic
from pydantic import BaseModel
from pydantic import Field
from pydantic import EmailStr

#FastAPI
from fastapi import FastAPI
from fastapi import Body
from fastapi import UploadFile, File

app = FastAPI()

##Models

#User
class UserBase(BaseModel):
    user_id: UUID = Field(...)
    email: EmailStr = Field(...)
    username: str = Field(
    ...,
    min_length=1,
    max_length=20
    )

class UserLogin(UserBase):
    password: str = Field(
        ...,
        min_length=8,
        max_length=40
    )

class User(UserBase):
    profile_name: str = Field(
    ...,
    min_length=1,
    max_length=20
    )
    birth_date: Optional[date] = Field(default=None)

#Tweets
class Tweet(BaseModel):
    tweet_id: UUID = Field(...)
    creator: UUID = Field(...)
    date: datetime = Field(...)
    content: str = Field(
        ...,
        min_length=1,
        max_length=280
        )
    media: Optional[UploadFile] = File(default=None)
    # view_status

##Endpoints

@app.get(path='/')
def home():
    return {"Twitter API": "Working"}

@app.post(path='/profile/create')
def create_profile(
    user: User = Body(...)
):
    return user

@app.post(path='/tweet/create')
def create_tweet(
    tweet: Tweet = Body(...)
):
    return tweet