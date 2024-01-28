from fastapi import FastAPI
from database.database import init_db
from routers import menu, submenu, dish


app = FastAPI(
    title='Restaurant API',
    description='Приложение для управления меню ресторана',
    version='2.0.0',
    openapi_tags=[
        {
            'name': 'Меню',
            'description': 'Операции с меню',
        },
        {
            'name': 'Подменю',
            'description': 'Операции с подменю',
        },
        {
            'name': 'Блюда',
            'description': 'Операции с блюдами',
        },
    ]
)


@app.on_event('startup')
async def on_startup():
    """Выполняется при запуске приложения.
    Инициализирует БД и запускает задачу обновления БД."""
    print("Running on_startup()")
    await init_db()
    print("Database initialization complete")


app.include_router(menu.router)
app.include_router(submenu.router)
app.include_router(dish.router)
