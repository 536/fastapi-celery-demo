from fastapi import FastAPI, Request

from apps.account.urls import account
from apps.task.urls import task


app = FastAPI()


@app.get("/")
def index(request: Request):
    return {"code": 0, "message": "Hello World", "data": {"docs": f"{request.scope.get('root_path')}/docs"}}


app.include_router(account, prefix="/account", tags=["账户管理"])
app.include_router(task, prefix="/task", tags=["任务管理"])


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", port=8000, reload=True)
