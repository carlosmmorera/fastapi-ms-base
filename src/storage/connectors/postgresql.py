from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from ...config import config
from ...config.postgresql import ConfigPostgreSQL

conf: ConfigPostgreSQL = config.get('postgresql', ConfigPostgreSQL)

# In case of using SQLite database instead of PostgreSQL use this type of URL
# SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"

engine = create_engine(conf.url) # Add parameter connect_args={"check_same_thread": False} for SQLite
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()