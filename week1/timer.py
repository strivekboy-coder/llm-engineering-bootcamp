import time
from typing import Callable, Any
from functools import wraps


def timer(func: Callable[..., Any]) -> Callable[..., Any]:
    """简单计时装饰器：打印函数执行耗时"""

    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        elapsed = end - start
        print(f"{func.__name__} took {elapsed:.4f} seconds")
        return result

    return wrapper


# =========================
# 测试代码（仅在直接运行此文件时执行）
# =========================
if __name__ == "__main__":
    import time

    @timer
    def slow_add(a: int, b: int) -> int:
        time.sleep(0.5)
        return a + b

    print("Testing timer decorator...")
    print("Result:", slow_add(10, 20))
