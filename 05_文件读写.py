# -*- coding: utf-8 -*-
"""
第 5 课：读写文件 —— 让程序处理你电脑上真实的数据

学完这一课，你就能自己去读「参考文献核对清单.csv」这类文件了。
"""

import csv
import json
import os

# 本文件所在的文件夹（这样就不用管运行目录在哪了）
HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "..", "data")

# 确保数据文件夹存在（不存在就新建，已存在也不报错）
os.makedirs(DATA, exist_ok=True)

# ============================================================
# 1. 写文本文件
#    with open(...) as f:  这种写法会在用完后自动关掉文件，最安全
#    encoding="utf-8" 一定要写，否则中文可能变乱码
# ============================================================

txt_path = os.path.join(DATA, "notes.txt")

with open(txt_path, "w", encoding="utf-8") as f:
    f.write("高一物理备课笔记\n")
    f.write("第一章：运动的描述\n")
    f.write("第二章：匀变速直线运动\n")

print("已写入：", txt_path)

# 模式说明："w" 覆盖写， "a" 追加写， "r" 读取


# ============================================================
# 2. 读文本文件（整份读）
# ============================================================

with open(txt_path, "r", encoding="utf-8") as f:
    content = f.read()          # 一次读全部，得到一个大字符串

print("---- 文件内容 ----")
print(content)

# 一行一行读，适合大文件
with open(txt_path, "r", encoding="utf-8") as f:
    for line_no, line in enumerate(f, start=1):
        print(f"第 {line_no} 行：{line.rstrip()}")   # rstrip 去掉行尾换行符


# ============================================================
# 3. 追加写入
# ============================================================

with open(txt_path, "a", encoding="utf-8") as f:
    f.write("第三章：相互作用力\n")

with open(txt_path, "r", encoding="utf-8") as f:
    print(f"现在共 {len(f.readlines())} 行")


# ============================================================
# 4. 读写 CSV（逗号分隔的表格，Excel 能直接打开）
# ============================================================

csv_path = os.path.join(DATA, "成绩单.csv")

# 写入：用 csv.writer，每行是一个列表
rows = [
    ["姓名", "班级", "物理", "数学", "英语"],
    ["小明", "高一(3)班", "92", "88", "85"],
    ["小红", "高一(3)班", "88", "95", "91"],
    ["小刚", "高一(3)班", "75", "70", "68"],
    ["小丽", "高一(3)班", "96", "92", "89"],
]

with open(csv_path, "w", encoding="utf-8-sig", newline="") as f:
    # newline="" 是 csv 模块的固定要求，避免多出空行
    # utf-8-sig 带 BOM，这样用 Excel 打开中文不会乱码
    writer = csv.writer(f)
    writer.writerows(rows)

print("已写入：", csv_path)

# 读取：用 csv.DictReader，每一行变成一个字典（键就是表头）
with open(csv_path, "r", encoding="utf-8-sig") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(f"{row['姓名']} 物理 {row['物理']} 分")


# ============================================================
# 5. 读写 JSON（结构化数据，程序中传数据常用）
# ============================================================

json_path = os.path.join(DATA, "班级信息.json")

info = {
    "班级": "高一(3)班",
    "人数": 4,
    "学生": [
        {"姓名": "小明", "物理": 92},
        {"姓名": "小红", "物理": 88},
    ],
}

# ensure_ascii=False 才能让中文正常显示（否则会变 \u5c0f\u660e）
with open(json_path, "w", encoding="utf-8") as f:
    json.dump(info, f, ensure_ascii=False, indent=2)

with open(json_path, "r", encoding="utf-8") as f:
    loaded = json.load(f)          # 变回字典/列表

print(type(loaded), loaded["班级"], loaded["学生"][0]["姓名"])


# ============================================================
# 6. 文件和文件夹的常用操作
# ============================================================

print("文件是否存在：", os.path.exists(csv_path))
print("文件大小（字节）：", os.path.getsize(csv_path))
print("所在文件夹：", os.path.dirname(csv_path))

# 保险起见，生成文件前先确保文件夹存在
os.makedirs(os.path.join(DATA, "备份"), exist_ok=True)

print("\n==== 第 5 课结束 ====")


# ============================================================
# 【练习】
# ============================================================
# 练习 5-1：把上面的“备课笔记”再追加两章，然后重新读出来打印。
#
# 练习 5-2：读取 data/成绩单.csv，打印每一列的平均分（物理、数学、英语）。
#           提示：先建一个空列表收集某一科的所有分数，注意字段是字符串，
#           要用 int(...) 或 float(...) 转成数字再算。
#
# 练习 5-3：把班级信息写入一个 json 文件，再读回来打印“人数”。
#
# 练习 5-4（稍难）：给成绩单再加一列“总分”，重新写回
#           data/成绩单_含总分.csv。
#           提示：读进来时是字典，算完总分往字典里加一个键，再用
#           csv.DictWriter 写出去（需要先写表头 fieldnames）。
