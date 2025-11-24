from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, INTEGER,  String, TEXT, JSON, ForeignKey
from sqlalchemy.ext.mutable import  MutableList


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


class CandidateInfo(CompilerModelBase):
    __tablename__ = "candidate_info"

    candidate_id = Column(String(25), primary_key=True, nullable=False)


class CandidateExamResult(CompilerModelBase):
    __tablename__ = "candidate_exam_result"

    candidate_id = Column(String(25), ForeignKey(column="candidate_info.candidate_id"), primary_key=True, nullable=False)
    score = Column(MutableList.as_mutable(JSON), nullable=False)
    
    


