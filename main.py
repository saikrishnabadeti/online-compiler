
from fastapi import FastAPI
from app.models.compiler import CompilerModelBase
from app.db import engine
from app.routers import compiler_question
from app.routers import compiler_interpreter
from app.routers import interactive_compiler
from app.routers import interactive_compiler_docker


app = FastAPI()


@app.on_event("startup")
async def startup():
    CompilerModelBase.metadata.create_all(engine)
    return

app.include_router(compiler_question.router)
app.include_router(compiler_interpreter.router)
app.include_router(interactive_compiler.router)
app.include_router(interactive_compiler_docker.router)






