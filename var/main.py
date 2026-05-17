from fastapi import FastAPI
from fastapi import APIRouter # 引入模板
from fastapi.staticfiles import StaticFiles # 设定静态文件夹


# 初始化程序
app = FastAPI()
root_url = "greendam.ww3.tw" 

# 设定静态文件夹 包括挂载位置
app.mount("/static", StaticFiles(directory="/var/static"), name="static")

# 模板文件
from routers import api
app.include_router(api.router)


@app.get("/")
def home():
    return "Hello, World!!!"
