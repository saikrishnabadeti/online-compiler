from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, INTEGER,  String, TEXT, JSON, ForeignKey, DATETIME, FLOAT
from sqlalchemy.ext.mutable import  MutableList, MutableDict


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



    
    
class CodingExam(CompilerModelBase):
    __tablename__ = "coding_exam"

    id = Column(INTEGER, primary_key=True, nullable=False)
    title = Column(String(100), nullable=False)
    description = Column(TEXT, nullable=True)
    collage = Column(String(100), nullable=False)
    window_start = Column(DATETIME, nullable=False)
    window_end = Column(DATETIME, nullable=False)
    duration = Column(FLOAT, nullable=False)
    category = Column(String(100), nullable=False)
    is_active = Column(INTEGER, nullable=False, default = 0)
    questions = Column(MutableDict.as_mutable(JSON), nullable=False)


## Table by rahul -------

class LanguagesInfo(CompilerModelBase):
    __tablename__ = "languages"
 
    lang_id = Column(INTEGER, primary_key=True, nullable=False, autoincrement=True)
    lang_name = Column(String(50), nullable=False, unique=True)
    description = Column(TEXT, nullable=True)

class CandidateExamResult(CompilerModelBase):
    __tablename__ = "candidate_exam_result"
 
    result_id = Column(INTEGER, primary_key=True, nullable=False)
    candidate_id = Column(String(25), ForeignKey(column="candidate_info.candidate_id"), nullable=False)
    exam_id = Column(INTEGER, ForeignKey(column="coding_exam.id"), nullable=False)
    score = Column(MutableList.as_mutable(JSON), nullable=False)
    total = Column(FLOAT, nullable=False)

##########################
