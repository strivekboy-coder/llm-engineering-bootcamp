from typing import Callable, Any, Tuple, Type
from functools import wraps
import time


def retry(
    max_retries: int = 3,
    delay: float = 0.2,
    backoff: float = 2.0,
    exceptions: Tuple[Type[Exception], ...] = (Exception,)
) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    """带参数的 retry 装饰器：自动重试、延迟、指数退避"""

    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:

        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            attempts = 0
            current_delay = delay

            while True:
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    attempts += 1

                    if attempts > max_retries:
                        raise  # 把原始异常原样抛出去

                    print(
                        f"[retry] {func.__name__} failed with {e!r}, "
                        f"attempts={attempts}/{max_retries}, "
                        f"sleeping for {current_delay:.2f}s then retrying..."
                    )
                    time.sleep(current_delay)
                    current_delay *= backoff

        return wrapper

    return decorator


# =========================
# 测试代码（仅在直接运行此文件时执行）
# =========================
if __name__ == "__main__":
    import random

    @retry(max_retries=3, delay=0.2)
    def unstable_add(a: int, b: int) -> int:
        """测试函数：随机失败"""
        if random.random() < 0.7:
            raise ConnectionError("Random failure")
        return a + b

    print("Testing retry decorator...")
    try:
        result = unstable_add(3, 4)
        print("Result:", result)
    except Exception as e:
        print("Final Exception:", e)
