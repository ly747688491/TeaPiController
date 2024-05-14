"""
@Project        ：TeaPiController 
@File           ：database.py
@IDE            ：PyCharm 
@Author         ：李延
@Date           ：2024/5/13 下午4:12 
@Description    ：
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = f"sqlite:///./teapi.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, echo=True
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
