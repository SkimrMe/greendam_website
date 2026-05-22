from fastapi import APIRouter
import json, os, datetime


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


# 根据文件夹列出文件
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
            url_path = f"{url}/{filename}"
            rule_list.append({
                "id": id,
                "filename": filename,
                "url_path": url_path
            })
        return (rule_list)
###########

# 展示不同版本的小绿图片
###########
@router.get("/image/list/")
@router.get("/image/list/{name}/")
async def 展示不同版本的小绿图片(name: str = None):
    if not name:
        image_path = "../../var/static/resources/other/image"
        image_name = os.listdir(image_path)
        image_files = [f for f in image_name if f.lower().endswith((""))]
        rule_list = []
        url = f"https://{root_url}/static/resources/other/image"
        for id, filename in enumerate(image_files, start=1):
            url_path = f"{url}/{filename}"
            rule_list.append({
                "id": id,
                "filename": filename,
                "url_path": url_path
            })
        return (rule_list)
    else:
        image_path = f"../../var/static/resources/other/image/{name}"
        image_name = os.listdir(image_path)
        image_files = [f for f in image_name if f.lower().endswith((""))]
        rule_list = []
        url = f"https://{root_url}/static/resources/other/image/{name}"
        for id, filename in enumerate(image_files, start=1):
            url_path = f"{url}/{filename}"
            rule_list.append({
                "id": id,
                "filename": filename,
                "url_path": url_path
            })
        return  (rule_list)

###########


# 展示不同版本的小绿视频合集
###########
@router.get("/video/list/")
@router.get("/video/list/{name}/")
def 展示不同版本的小绿视频合集(name: str = None):
    if not name:
        video_path = "../../var/static/resources/other/video"
        video_name = os.listdir(video_path)
        video_files = [f for f in video_name if f.lower().endswith((""))]
        rule_list = []
        url = f"https://{root_url}/static/resources/other/video"
        for id, filename in enumerate(video_files, start=1):
            url_path = f"{url}/{filename}"
            rule_list.append({
                "id": id,
                "filename": filename,
                "url_path": url_path
            })
        return (rule_list)
    else:
        video_path = f"../../var/static/resources/other/video/{name}"
        video_name = os.listdir(video_path)
        video_files = [f for f in video_name if f.lower().endswith((""))]
        rule_list = []
        url = f"https://{root_url}/static/resources/other/video/{name}"
        for id,filename in enumerate(video_files, start=1):
            url_path = f"{url}/{filename}"
            rule_list.append({
                "id": id,
                "filename": filename,
                "url_path": url_path
            })
        return (rule_list)
###########