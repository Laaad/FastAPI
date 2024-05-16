from fastapi import APIRouter, Depends
from schemas import UserBase, UserDisplay
from sqlalchemy.orm import Session
from db.database import get_db
from typing import List
from db import db_user
from auth.auth2 import oauth2_schema

router = APIRouter( prefix='/user', tags=['user'])


#create user


@router.post('/', response_model=UserDisplay)
def create_user(request: UserBase, db: Session = Depends(get_db)):
    return db_user.create_user(db, request)

#read all users


@router.get('/', response_model=List[UserDisplay])
def get_all_users(db: Session = Depends(get_db)):
    return db_user.get_all_users(db)

#read_a_user


@router.get('/{id}', response_model=UserDisplay)
def get_user(id: int, db: Session = Depends(get_db)):
    return db_user.get_user(db, id)


@router.put('/{id}/update')
def update_user(id: int, request: UserBase, db: Session= Depends(get_db)):
    return db_user.update_user()


@router.delete('/delete/{id}')
def delete_user(id:int, db: Session=Depends(get_db)):
    return db_user.delete_user(db, id)
