import numpy as np
from scipy.integrate import quad
def main():
    {
        print(123)
    }

    
def calculate_average(f, a, b):
    """
    计算函数 f 在区间 [a, b] 上的积分平均值。
    
    参数:
    f: 可调用函数 f(x)
    a: 积分起始点
    b: 积分结束点
    
    返回:
    f 在 [a, b] 上的平均值
    """
    if a == b:
        # 处理区间宽度为零的特殊情况
        # 此时，一个点的“平均值”就是该点的值 f(a)
        return f(a)
    
    # scipy.integrate.quad 返回 (积分值, 估算误差)
    integral_value, error = quad(f, a, b)
    
    # quad 正确处理 a > b 的情况 (积分值为负)
    # 此时 (b - a) 也为负，所以平均值计算依然正确
    average = integral_value / (b - a)
    
    return average