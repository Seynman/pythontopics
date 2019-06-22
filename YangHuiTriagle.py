import numpy as np


def generate_triangle(row):
    chart = np.zeros((row, row), dtype=int)
    for i in range(row):
        for j in range(row):
            if j == 0 or i == j:
                chart[i][j] = 1
            else:
                chart[i][j] = chart[i-1][j-1] + chart[i-1][j]
    return chart


def print_triangle(chart):
    for i in range(len(chart)):
        for j in range(len(chart[0])):
            if chart[i][j] != 0:
                print(chart[i][j], end="\t")
            if j == i:
                print()


row_number = int(input("请输入行数："))
chart = generate_triangle(row_number)
print_triangle(chart)