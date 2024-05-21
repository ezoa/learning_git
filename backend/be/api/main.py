from fastapi import FastAPI
from db import session
from model import TestUser,TestUserTable



app=FastAPI()


@app.get("/test_users")

def get_user_list():
    users=session.query(TestUserTable).all()
    return users


@app.get("/test_users/{user_id}")

def get_user(user_id: int):
    user=session.query(TestUserTable).\
        filter(TestUserTable.id==user_id).first()
    return user
@app.post("/test_users")

def post_user(user:TestUser):

    db_test_user= TestUser(name=user.name,email=user.email)
    session.add(db_test_user)
    session.commit()

@app.put("/test_users/{user_id}")
def put_users(user:TestUser,user_id:int):
    target_user=session.query(TestUserTable).\
        filter(TestUserTable.id==user_id).first()
    target_user.name= user.name
    target_user.email=user.email
    session.commit()