import requests
import os
# 保存的图片路径
root="D://pics//"
url="https://img08.tooopen.com/20190705/tooopen_sl_151556155680624.jpg"
path=root+url.split("/")[-1]
try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        r=requests.get(url)
        with open(path,'wb') as f:
            f.write(r.content)
            f.close()
            print("文件保存成功")
    else:
        print("文件已存在")
except:
    print("爬取失败")