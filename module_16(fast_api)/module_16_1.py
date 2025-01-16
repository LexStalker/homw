from fastapi import FastAPI

# Создаём экземпляр приложения FastAPI
app = FastAPI()


@app.get("/")
async def welcome():
    return "Главная страница"


@app.get("user/admin")
async def admin():
    return "Добро пожаловать Админимтратор"


@app.get("user/{id}")
async def user(id):
    return f"Вы вошли, ваш номер пользователя № {id}!"


@app.get("/user")
async def info_user(username='user', age=25):
    return f"Информация о пользователе. Имя: {username}, Возраст: {age}"
