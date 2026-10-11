# -*- coding: utf-8 -*-
"""
第 6 课：综合练习 —— 成绩统计分析

把前 5 课学的东西串起来，做一件你工作中真用得上的事：
读一份成绩表 -> 算统计指标 -> 排名 -> 导出报告。

先整体读一遍代码，理解每一段在干什么，然后试着自己改：
改分数、加学生、加科目、改及格线、换成你真实班级的数据。
"""

import csv
import os

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "..", "data")
os.makedirs(DATA, exist_ok=True)

SCORE_FILE = os.path.join(DATA, "月考成绩.csv")
REPORT_FILE = os.path.join(DATA, "成绩分析报告.txt")

SUBJECTS = ["物理", "数学", "英语"]


# ============================================================
# 第 1 步：准备一份数据（如果还没有就生成一份）
# ============================================================

def create_sample_data():
    rows = [
        ["姓名", "物理", "数学", "英语"],
        ["小明", "92", "88", "85"],
        ["小红", "88", "95", "91"],
        ["小刚", "58", "62", "55"],
        ["小丽", "96", "92", "89"],
        ["小强", "73", "80", "78"],
        ["小美", "85", "76", "94"],
        ["小华", "45", "50", "60"],
    ]
    with open(SCORE_FILE, "w", encoding="utf-8-sig", newline="") as f:
        csv.writer(f).writerows(rows)
    print(f"已生成示例数据：{SCORE_FILE}")


if not os.path.exists(SCORE_FILE):
    create_sample_data()


# ============================================================
# 第 2 步：读数据，算总分和平均分
# ============================================================

def load_students(path):
    """读取成绩表，返回一个学生字典的列表"""
    students = []
    with open(path, "r", encoding="utf-8-sig") as f:
        for row in csv.DictReader(f):
            student = {"姓名": row["姓名"]}
            for subject in SUBJECTS:
                student[subject] = int(row[subject])
            student["总分"] = sum(student[s] for s in SUBJECTS)
            student["平均分"] = round(student["总分"] / len(SUBJECTS), 1)
            students.append(student)
    return students


students = load_students(SCORE_FILE)
print(f"共读取 {len(students)} 名学生\n")


# ============================================================
# 第 3 步：统计每个科目的指标
# ============================================================

def subject_stats(students, subject):
    """返回某一科目的 最高分、最低分、平均分、及格率"""
    scores = [s[subject] for s in students]
    passed = [s for s in scores if s >= 60]
    return {
        "最高分": max(scores),
        "最低分": min(scores),
        "平均分": round(sum(scores) / len(scores), 1),
        "及格率": f"{len(passed) / len(scores) * 100:.1f}%",
    }


print("========== 各科统计 ==========")
for subject in SUBJECTS:
    stat = subject_stats(students, subject)
    print(f"【{subject}】最高 {stat['最高分']}  "
          f"最低 {stat['最低分']}  "
          f"平均 {stat['平均分']}  "
          f"及格率 {stat['及格率']}")


# ============================================================
# 第 4 步：按总分排名
# ============================================================

ranked = sorted(students, key=lambda s: s["总分"], reverse=True)

print("\n========== 总分排名 ==========")
for rank, student in enumerate(ranked, start=1):
    print(f"第 {rank} 名  {student['姓名']}  "
          f"总分 {student['总分']}  平均 {student['平均分']}")


# ============================================================
# 第 5 步：找出需要关注的学生（有科目不及格）
# ============================================================

print("\n========== 需要关注 ==========")
for student in students:
    failed = [s for s in SUBJECTS if student[s] < 60]
    if failed:
        detail = "，".join(f"{s} {student[s]}" for s in failed)
        print(f"{student['姓名']}：{len(failed)} 科不及格（{detail}）")


# ============================================================
# 第 6 步：把结果导出成一份 txt 报告
# ============================================================

lines = ["物理组 · 月考成绩分析报告", "=" * 30, ""]
lines.append(f"参考人数：{len(students)} 人")
lines.append("")
lines.append("【各科统计】")
for subject in SUBJECTS:
    stat = subject_stats(students, subject)
    lines.append(f"  {subject}：最高 {stat['最高分']}，最低 {stat['最低分']}，"
                 f"平均 {stat['平均分']}，及格率 {stat['及格率']}")
lines.append("")
lines.append("【总分排名】")
for rank, student in enumerate(ranked, start=1):
    lines.append(f"  {rank}. {student['姓名']}  总分 {student['总分']}  "
                 f"平均 {student['平均分']}")

with open(REPORT_FILE, "w", encoding="utf-8") as f:
    f.write("\n".join(lines))

print(f"\n报告已导出：{REPORT_FILE}")

print("\n==== 第 6 课结束 ====")


# ============================================================
# 【练习】
# ============================================================
# 练习 6-1：把及格线从 60 改成 65，重新统计及格率，看看差别有多大。
#
# 练习 6-2：再加一项「优秀率」（>= 85 分算优秀）。
#
# 练习 6-3：把科目换成你实际教的科目，换成你真实班级的数据，
#           生成一份能直接用的工作报告。
#
# 练习 6-4（进阶）：不用 sorted，自己写一个冒泡排序，
#           把学生按总分从高到低排好，再和 sorted 的结果对比。
#
# 练习 6-5（进阶）：把报告改成导出 Word。本机已装 python-docx，大致用法：
#               from docx import Document
#               doc = Document()
#               doc.add_paragraph("报告标题")
#               doc.save("报告.docx")
#           试着让它生成一份带表格的成绩报告。
