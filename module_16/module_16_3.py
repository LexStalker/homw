from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}


@app.get("/users")
async def user_get() -> dict:
    return users


@app.post('/user/{username}/{age}')
async def insert_user(
        username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username', example='UrbanUser')]
        , age: Annotated[int, Path(ge=18, le=120, description='Enter Age', example='24')]) -> str:
    user_id = str(int(max(users, key=int)) + 1)
    users[user_id] = f'Имя: {username}, возраст: {age}'
    return "User {user_id} is registered"


@app.put('/user/{user_id}/{username}/{age}')
async def update_user(user_id: Annotated[int, Path(ge=1, le=120, description='Enter User ID', example='2')]
                      , username: Annotated[
            str, Path(min_length=5, max_length=20, description='Enter username', example='UrbanUser')]
                      , age: Annotated[int, Path(ge=18, le=120, description='Enter Age', example='24')]) -> str:
    users[user_id] = f'Имя: {username}, возраст: {age}'
    return "The user {user_id} is updated"


@app.delete('/user/{user_id}')
async def user_delete(user_id:
Annotated[int, Path(ge=1, le=120, description='Enter User ID', example='2')]) -> str:
    users.pop(user_id)
    return f'User №{user_id}is deleted'
