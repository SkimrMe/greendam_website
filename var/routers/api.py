from fastapi import APIRouter
import json, os


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

###########
@router.get('/files/list/')
@router.get('/files/list/{name}/')
async def 根据文件夹列出文件(name: str = None):
    if not name:
        files_path = "../../var/static/resources/greendam"
        files_name = os.listdir(files_path)
        files_files = [f for f in files_name if f.lower().endswith((""))]
        rule_list = []
        url = f"https://{root_url}/static/resources/greendam"
        for id, filename in enumerate(files_files, start=1):
            url_path = f"{url}/{filename}/"
            rule_list.append({
                "id": id,
                "filename": filename,
                "url_path": url_path
            })
        return (rule_list)
    else:
        files_path = f"../../var/static/resources/greendam/{name}"
        files_name = os.listdir(files_path)
        files_files = [f for f in files_name if f.lower().endswith((""))]
        rule_list = []
        url = f"https://{root_url}/static/resources/greendam/{name}"
        for id, filename in enumerate(files_files, start=1):
            url_path = f"{url}/{filename}/"
            rule_list.append({
                "id": id,
                "filename": filename,
                "url_path": url_path
            })
        return (rule_list)

###########