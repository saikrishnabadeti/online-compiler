from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, INTEGER, FLOAT, String, TEXT, JSON
from sqlalchemy.ext.mutable import MutableDict, MutableList


class CompilerModelBase(DeclarativeBase):
    pass

class Questions(CompilerModelBase):

    __tablename__ = "questions"

    question_id = Column(INTEGER, primary_key=True, nullable=False)
    title = Column(String(100), nullable=False)
    question = Column(String(225), nullable=False)
    description = Column(TEXT, nullable=False)
    sample_inputs = Column(String(100), nullable=True)
    sample_outputs = Column(String(100), nullable=True)
    test_cases = Column(MutableList.as_mutable(JSON), nullable=False)





