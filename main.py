
from fastapi import FastAPI
from app.models.compiler import CompilerModelBase
from app.db import engine
from app.routers import compiler_question


app = FastAPI()


@app.on_event("startup")
async def startup():
    CompilerModelBase.metadata.create_all(engine)
    return

app.include_router(compiler_question.router)





