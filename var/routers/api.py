from fastapi import APIRouter
import json


root_url = "greendam.ww3.tw"

# 建立 APIRouter 实例
router = APIRouter(
    prefix="/api",
    tags=["api"]
)

@router.get('/')
def 用于测试():
    return {
        "code": "200 ok!",
        "msg": "Hello, World!!"
        }
