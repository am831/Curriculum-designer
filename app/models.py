from database import Base 
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text

class Post(Base): 
    """ 
    sets up the postgres table and defines columns
    """
    __tablename__ = "posts"
    id = Column(Integer, primary_key = True, nullable = False)
    course = Column(String, nullable = False)
    duration = Column(String, nullable = True)
    effort = Column(String, nullable = True)
    link = Column(String, nullable = True)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, 
    server_default=text('now()'))
    owner_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), 
    nullable=False)
    year = Column(Integer, nullable = False)
    comments = Column(String, nullable = True)

class User(Base):
    __tablename__ = "users"
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    id = Column(Integer, primary_key = True, nullable = False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, 
    server_default=text('now()'))
