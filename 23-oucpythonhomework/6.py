import math

def solve_quadratic_equation(a, b, c):
    delta = b**2 - 4*a*c
    if delta > 0:
        root1 = (-b + math.sqrt(delta)) / (2*a)
        root2 = (-b - math.sqrt(delta)) / (2*a)
        return f"实数解为：{root1:.2f},{root2:.2f}"
    elif delta == 0:
        root = -b / (2*a)
        return f"实数解为：{root:.2f}"
    else:
        return "无实根"

input_str = input()
try:
    a, b, c = map(float, input_str.split(','))
    if a == 0:
        print("系数a不能为0")
    else:
        result = solve_quadratic_equation(a, b, c)
        print(result)
except ValueError:
    print("输入格式错误，请输入三个用逗号分隔的数字。")
