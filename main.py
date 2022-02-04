#Python
from optparse import Option
from uuid import UUID
from datetime import date, datetime
from typing import Optional, List

#Pydantic
from pydantic import BaseModel
from pydantic import Field
from pydantic import EmailStr

#FastAPI
from fastapi import FastAPI
from fastapi import Body
from fastapi import UploadFile, File
from fastapi import status

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
    content: str = Field(
        ...,
        min_length=1,
        max_length=280
        )
    media: Optional[UploadFile] = File(default=None)
    creator: UUID = Field(...)
    created_at: datetime = Field(default=datetime.today())
    is_private: Optional[bool] = Field(default=False)

#Path Operations
##Users

###Register a user
@app.post(
    path='/user/create',
    response_model=User,
    status_code=status.HTTP_201_CREATED,
    summary="Register a user",
    tags=["Users"]
    )
def create_user():
    pass

###Login a user
@app.post(
    path='/login',
    response_model=User,
    status_code=status.HTTP_202_ACCEPTED,
    summary="Login a user",
    tags=["Users"]
    )
def login():
    pass

###Logout a user
@app.post(
    path='/logout',
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Logout a user",
    tags=["Users"]
    )
def logout():
    pass

###Show all users
@app.get(
    path='/users',
    response_model=List[User],
    status_code=status.HTTP_200_OK,
    summary="Show all users",
    tags=["Users"]
    )
def show_all_users():
   pass

###Show a user
@app.get(
    path='/users/{username}',
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Show a user",
    tags=["Users"]
    )
def show_user():
    pass

###Delete a user
@app.delete(
    path='/users/{user_id}/delete',
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Delete a user",
    tags=["Users"]
    )
def delete_user():
    pass

###Update a user
@app.put(
    path='/users/{username}/update',
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Update a user",
    tags=["Users"]
    )
def update_user():
    pass

##Tweets
###Show all tweets. Home
@app.get(
    path='/',
    response_model=List[Tweet],
    status_code=status.HTTP_200_OK,
    summary="Show all tweets",
    tags=["Tweets"]
    )
def show_all_tweets():
    pass

###Show a tweet
@app.get(
    path='/tweet/{tweet_id}',
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary="Show a tweet",
    tags=["Tweets"]
    )
def show_tweet():
    pass

###Post a tweet
@app.post(
    path='/post',
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary="Post a tweet",
    tags=["Tweets"]
    )
def post_tweet(
    tweet: Tweet = Body(...)
):
    return tweet

###Update a tweet
@app.put(
    path='/tweet/{tweet_id}/update',
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary="Update a tweet",
    tags=["Tweets"]
    )
def update_tweet():
    pass

###Delete a tweet
@app.delete(
    path='/tweet/{tweet_id}/delete',
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary="Delete a tweet",
    tags=["Tweets"]
    )
def home():
    pass