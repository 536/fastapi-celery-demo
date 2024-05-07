from fastapi import APIRouter

task = APIRouter()


@task.get("/")
def get():
    """get task info"""
    return {"method": "get"}


@task.post("/")
def create():
    """create task"""
    return {"method": "post"}


@task.put("/")
def update():
    """update task"""
    return {"method": "put"}


@task.delete("/")
def delete():
    """delete task"""
    return {"method": "delete"}
