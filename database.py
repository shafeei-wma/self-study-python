from fastapi import FastAPI
from tortoise import Tortoise
from tortoise.contrib.fastapi import register_tortoise
import os

from settings import settings

Tortoise.init_models(["models"], "models")

PYTHON_ENV = os.getenv("PYTHON_ENV")
if PYTHON_ENV == "test":
    DB_HOST = "db"
else:
    DB_HOST = settings.DB_HOST

TORTOISE_ORM = {
    "connections": {
        "default": f"postgres://{settings.DB_USER}:{settings.DB_PASS}@{DB_HOST}:{settings.DB_PORT}/{settings.DB_NAME}",
    },
    "apps": {
        "models": {
            "models": ["models", "aerich.models"],
            "default_connection": "default",
        },
    },
    "use_tz": False,
}

def init_db(app: FastAPI) -> None:
    register_tortoise(
        app,
        config=TORTOISE_ORM,
        modules={"models": ["models", "aerich.models"]},
        generate_schemas=True,
        add_exception_handlers=True,
    )

async def manual_query(query: str):
    # Use Tortoise.get_connection() to get a connection
    conn = Tortoise.get_connection('default')

    # Use execute_query() to run your raw SQL
    result = await conn.execute_query(query)
    print(result)
    
    # Disconnect when you're finished
    await Tortoise.close_connections()
    return result


# aerich init -t database.TORTOISE_ORM
# aerich init-db
# -----if any changes made in model, re run 2 codes below. 
# aerich migrate
# aerich upgrade