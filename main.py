
from fastapi import FastAPI
from app.models.compiler import CompilerModelBase
from app.db import engine
from app.routers import compiler_question
from app.routers import compiler_interpreter
from app.routers import interactive_compiler
from app.routers import interactive_compiler_docker
from app.routers import compiler_exam
from app.routers import language

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


## apply cors
app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,  # Allow cookies to be included in cross-origin requests
        allow_methods=["*"],     # Allow all HTTP methods (GET, POST, PUT, DELETE, etc.)
        allow_headers=["*"],     # Allow all headers
    )

@app.on_event("startup")
async def startup():
    CompilerModelBase.metadata.create_all(engine)
    return

app.include_router(compiler_question.router)
app.include_router(compiler_interpreter.router)
app.include_router(interactive_compiler.router)
app.include_router(interactive_compiler_docker.router)
app.include_router(compiler_exam.router)
app.include_router(language.router)






