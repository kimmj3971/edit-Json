# -*- coding: utf-8 -*-
# json 파일 두개 이어붙이기
# 데이터셋에서 라벨링 따로한거 마스크이미지 손상 없이 붙이고 싶을때

import json

json_dir1 = r"C:\Users\user\Desktop\JSONdir\sample(1).json"  # 원본 json파일 폴더 경로
json_dir2 = r"C:\Users\user\Desktop\JSONdir\sample(2).json"  # 원본 json파일 폴더 경로
new_dir = r'C:\Users\user\Desktop\new_dir\subjson.json'  # 새로 저장할 json파일 경로, 파일명도 저장해줘야됨


def subjson():
    with open(json_dir1, 'r') as f1:
        data1 = json.load(f1)  # top
    with open(json_dir2, 'r') as f2:
        data2 = json.load(f2)  # bot

    tmp = data1

    for i in range(len(data2["data"])):
        tmp["data"].append(data2["data"][i])

    with open(new_dir, 'w') as outfile:
        json.dump(tmp, outfile)


if __name__ == '__main__':
    subjson()