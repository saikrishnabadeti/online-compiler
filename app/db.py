from dotenv import load_dotenv
import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
from fastapi import HTTPException
from sqlalchemy.exc import SQLAlchemyError



# Load environment variables
load_dotenv()
DATABASE_URL = os.getenv("DATABASE")

# Initialize SQLAlchemy engine
engine = create_engine(DATABASE_URL, echo=False)

# Create a base class for declarative models
Base = declarative_base()


# Database session dependency
def get_db():
    """Create a SQLAlchemy ORM session for database operations."""
    db = Session(bind=engine)
    try:
        yield  db
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Database session error: {e}")
    finally:
        db.close()

