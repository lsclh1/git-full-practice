# 工具函数

def format_result(operation, a, b, result):
    """格式化输出结果"""
    return f"{a} {operation} {b} = {result}"

def validate_number(value):
    """检查是否是数字"""
    try:
        float(value)
        return True
    except ValueError:
        return False
