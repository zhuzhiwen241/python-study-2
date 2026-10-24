# -*- coding: utf-8 -*-
"""
多组数的加法（累加求和）

功能说明：
    不断从键盘输入数字，程序每输入一个数字就把它累加起来，
    直到输入 0 为止，最后输出所有数字的总和。

知识点：
    1. while True 死循环 + break 退出循环
    2. 累加器（accumulator）：total = total + num，简写为 total += num
    3. try/except 捕获非法输入，避免程序报错崩溃
    4. input() 返回的是字符串，需要用 float() 转换成数字
"""


def main():
    total = 0  # 累加器，用来保存最终的和，初始值为 0

    print("=" * 30)
    print("      多组数累加求和")
    print("=" * 30)
    print("请不断输入数字（支持整数和小数），")
    print("程序会自动累加，输入 0 结束并显示总和。\n")

    while True:
        user_input = input("请输入一个数字（输入 0 结束）：")

        # 把输入的字符串转换成数字；如果输入的不是数字，提示后重新输入
        try:
            num = float(user_input)
        except ValueError:
            print("⚠ 输入无效，请输入一个数字！\n")
            continue  # 跳过本次循环，回到输入处重新开始

        if num == 0:      # 输入 0 表示结束
            break         # 跳出 while 循环

        total += num      # 累加：total = total + num

    # 如果总和其实是整数（例如 10.0），就显示成 10，去掉多余的 .0
    if total == int(total):
        total = int(total)

    print("\n" + "=" * 30)
    print(f"所有数字的最终和为：{total}")
    print("=" * 30)


# 当直接运行本文件时才执行 main()；被其他文件导入时不会自动执行
if __name__ == "__main__":
    main()
