from fastapi import APIRouter

account = APIRouter()


@account.get("/")
def get():
    """get current account info"""
    return {"method": "get"}


@account.put("/info")
def update():
    """update currnt account info"""
    return {"method": "put"}


@account.post("/register")
def register():
    """register a new account"""
    return {"method": "post"}


@account.post("/login")
def login():
    """login account"""
    return {"method": "post"}


@account.post("/logout")
def logout():
    """logout account"""
    return {"method": "post"}
