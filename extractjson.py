# -*- coding: utf-8 -*-
# 특정 단어를 포함한 파일명의 json 파일만 따로 저장하고 싶을때
# 파일명 규칙에 따라 자유롭게 커스텀하면 됩니다

import json

json_dir = r'C:\Users\user\Desktop\JSONdir\sample(1).json'    # 원본 json파일 경로
new_dir = r'C:\Users\user\Desktop\new_JSONdir\extJSON.json'     # 새로 저장할 json파일 경로, 파일명도 저장해줘야됨
a = "Top"   # 특정 단어

def extJSON():
    with open(json_dir, 'r') as file_1:
        data1 = json.load(file_1)

    data1["data"] = [x for x in data1["data"] if (a in x["fileName"])]
#    data1["data"] = [x for x in data1["data"] if (a in x["fileName"]) and (x["set"] != "not_used")]
    with open(new_dir, 'w') as outfile:
        json.dump(data1, outfile)

if __name__ == '__main__':
    extJSON()