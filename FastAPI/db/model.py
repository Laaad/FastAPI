from db.database import Base
from sqlalchemy import Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer,String, Boolean



class DbUser(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    email = Column(String)
    password = Column(String)
    # article = relationship()
#
#
# class DbArticle(Base):
#     __tablename__ = 'articles'
#     id = Column(Integer, primary_key = True, index=True)
#     title = Column(String)
#     content = Column(String)
#     published = Column(Boolean)
#     user_id = Column(Integer, ForeignKey('users.id'))
#
#
