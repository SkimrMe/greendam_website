from fastapi import FastAPI, Request
from fastapi import APIRouter # 引入路由表
from fastapi.staticfiles import StaticFiles # 设定静态文件夹
from fastapi.templating import Jinja2Templates # 引入jinja模板
from fastapi.responses import RedirectResponse # 重定向工具


# 初始化程序
app = FastAPI(
    docs_url=None,
    redoc_url=None
)
root_url = "greendam.ww3.tw" 

# 设定静态文件夹 包括挂载位置
app.mount("/static", StaticFiles(directory="/var/static"), name="static")

# 设定jinja模板位置
templates = Jinja2Templates(directory="templates")

# 路由表文件
from routers import api
app.include_router(api.router)

@app.get("/")
async def reload_301_home():
    return RedirectResponse(url="https://greendam.ww3.tw/home/")

@app.get("/docs")
@app.get("/docs/")
@app.get("/redoc")
@app.get("/redoc/")
async def reload_301():
    return RedirectResponse(url="https://greendam.ww3.tw/home/")

@app.get("/home/")
async def home(request: Request):
    return templates.TemplateResponse(
        "home.html",
        {
            "request": request,
            "title": "home"
        }
    )

@app.get("/resources/")
async def resources(request: Request):
    return templates.TemplateResponse(
        "resources.html",
        {
            "request": request,
            "title": "resources"
        }
    )

@app.get("/bbs/")
async def bbs(request: Request):
    return templates.TemplateResponse(
        "bbs.html",
        {
            "request": request,
            "title": "bbs"
        },
    )