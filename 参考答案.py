# -*- coding: utf-8 -*-
"""
参考答案

用法：先自己在 lessons/ 里把练习写出来，卡住了再来看这里。
对照思路就行，变量名不必和这里一模一样——能跑通、结果对，就是好答案。

直接运行本文件，会把所有答案的输出打印出来：
    & "C:\\Users\\wylnb\\AppData\\Local\\Programs\\Python\\Python314\\python.exe" 参考答案.py
"""

import csv
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "..", "data")


def title(text):
    print(f"\n{'=' * 50}\n{text}\n{'=' * 50}")


# ============================================================
# 第 1 课
# ============================================================
title("第 1 课 参考答案")

# 1-1
print("张三，教龄 8 年")

# 1-2
r = 3
S = 3.14159 * r ** 2
print(f"半径 {r} 的圆面积是 {S:.2f}")

# 1-3
v0, a, t = 20, 5, 4
s = v0 * t + 0.5 * a * t ** 2
print(f"位移 s = {s} 米")

# 1-4（这里为了能自动运行，直接给个固定值；你在 PyCharm 里可以换成 input）
c = 37.0
f = c * 9 / 5 + 32
print(f"{c} 摄氏度 = {f} 华氏度")
# 交互版写法：
#   c = float(input("请输入摄氏温度："))
#   print(f"{c} 摄氏度 = {c * 9 / 5 + 32} 华氏度")


# ============================================================
# 第 2 课
# ============================================================
title("第 2 课 参考答案")

# 2-1
scores = [72, 85, 90, 66, 100, 58]
print("平均分：", round(sum(scores) / len(scores), 1))
print("最高分：", max(scores))
print("最低分：", min(scores))

# 2-2
city = "福建省福州市"
print(city[:2], city[-2:], city[::-1])

# 2-3
my_class = {
    "名称": "高一(3)班",
    "人数": 48,
    "平均分": 76.5,
    "重点班": False,
}
print(f"{my_class['名称']}共 {my_class['人数']} 人，"
      f"平均分 {my_class['平均分']}，"
      f"{'是' if my_class['重点班'] else '不是'}重点班")

# 2-4
students = [
    {"name": "小明", "score": 92},
    {"name": "小红", "score": 88},
    {"name": "小刚", "score": 75},
]
best = students[0]
for stu in students:
    if stu["score"] > best["score"]:
        best = stu
print(f"最高分是 {best['name']}，{best['score']} 分")


# ============================================================
# 第 3 课
# ============================================================
title("第 3 课 参考答案")

# 3-1
year = 2024
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print(f"{year} 是闰年")
else:
    print(f"{year} 不是闰年")

# 3-2
result = [n for n in range(1, 101) if n % 7 == 0]
print("1~100 中 7 的倍数：", result)

# 3-3
question_scores = [8, 10, 6, 9, 7]
total = 0
for i, qs in enumerate(question_scores, start=1):
    total += qs
    print(f"第 {i} 题得 {qs} 分，累计 {total} 分")

# 3-4
total = 0
for n in range(1, 101):
    total += n
print("1~100 的和 =", total)

odd_total = 0
for n in range(1, 101):
    if n % 2 == 1:
        odd_total += n
print("1~100 奇数和 =", odd_total)


# ============================================================
# 第 4 课
# ============================================================
title("第 4 课 参考答案")

# 4-1
def to_fahrenheit(c):
    return c * 9 / 5 + 32


for c in [0, 37, 100]:
    print(f"{c}℃ = {to_fahrenheit(c)}℉")

# 4-2
def is_pass(score, line=60):
    return score >= line


print(is_pass(59), is_pass(60), is_pass(70, line=65))

# 4-3
def count_words(text):
    return len(text)


def count_terms(text):
    return len(text.split())


sample = "匀变速直线运动 位移 与 时间"
print("字符数：", count_words(sample))
print("词数：", count_terms(sample))

# 4-4
def max_of(numbers):
    biggest = numbers[0]
    for n in numbers:
        if n > biggest:
            biggest = n
    return biggest


print("自写 max：", max_of([3, 9, 2, 15, 7]))


# ============================================================
# 第 5 课
# ============================================================
title("第 5 课 参考答案")

# 5-1
notes = os.path.join(DATA, "notes.txt")
if os.path.exists(notes):
    with open(notes, "a", encoding="utf-8") as f:
        f.write("第四章：牛顿运动定律\n")
        f.write("第五章：曲线运动\n")
    with open(notes, "r", encoding="utf-8") as f:
        print(f.read())
else:
    print("（请先运行第 5 课，生成 data/notes.txt）")

# 5-2
csv_path = os.path.join(DATA, "成绩单.csv")
if os.path.exists(csv_path):
    with open(csv_path, "r", encoding="utf-8-sig") as f:
        rows = list(csv.DictReader(f))
    for subject in ["物理", "数学", "英语"]:
        values = [float(row[subject]) for row in rows]
        print(f"{subject} 平均分：{sum(values) / len(values):.1f}")
else:
    print("（请先运行第 5 课，生成 data/成绩单.csv）")

# 5-3
json_path = os.path.join(DATA, "班级信息_答案.json")
info = {"班级": "高一(3)班", "人数": 4}
with open(json_path, "w", encoding="utf-8") as f:
    json.dump(info, f, ensure_ascii=False)
with open(json_path, "r", encoding="utf-8") as f:
    print("读回的人数：", json.load(f)["人数"])

# 5-4
if os.path.exists(csv_path):
    with open(csv_path, "r", encoding="utf-8-sig") as f:
        rows = list(csv.DictReader(f))

    for row in rows:
        row["总分"] = int(row["物理"]) + int(row["数学"]) + int(row["英语"])

    out_path = os.path.join(DATA, "成绩单_含总分.csv")
    fieldnames = ["姓名", "班级", "物理", "数学", "英语", "总分"]
    with open(out_path, "w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    print("已写出：", out_path)
    for row in rows:
        print(f"  {row['姓名']} 总分 {row['总分']}")
else:
    print("（请先运行第 5 课，生成 data/成绩单.csv）")

print("\n全部参考答案运行完毕。")
