# LLM Engineering Bootcamp

This repository contains my progress in a 20-week plan to become an AI / LLM Engineer.

## 📅 Current Week

**Week 1** – Python engineering foundations
(Decorators, type hints, testing, basic LeetCode)

## 📂 Structure

```
llm-engineering-bootcamp/
│
├── week1/
│   ├── base_client.py
│   ├── retry1.py
│   └── timer.py
│
├── study-diary.md
└── 20-week-plan.md
```

## 🎯 Goal

Build clean, tested, typed Python utilities and develop into a full-stack LLM engineer.

---

# Week 1 — Custom BaseClient with Retry & Timer

本周目标是实现一个工程级 API 调用底座 —— **BaseClient**。
它具备：

* 自动重试（retry 装饰器）
* 请求耗时统计（timer 装饰器）
* URL 安全拼接
* 类型标注完整
* 干净可扩展的类结构

这是后续学习（API、RAG、Agent）的基础模块。

---

## 🚀 Features

### ✅ 1. Retry（自动重试）

* 参数：

  * `max_retries`: 最大重试次数
  * `delay`: 初始延迟
  * `backoff`: 指数退避倍率
  * `exceptions`: 仅捕获指定异常才会重试
* 行为：

  * 捕获 transient 错误（如网络抖动）
  * 按 backoff 越来越慢地重试
  * 最终失败时 re-raise 原始异常

---

### ✅ 2. Timer（耗时统计）

* 使用 `time.perf_counter()` 高精度计时
* 自动打印每次 request 的耗时
* 使用 `functools.wraps` 保留函数元信息

---

### ✅ 3. BaseClient（API 客户端基础类）

* 保存：

  * `base_url`
  * `timeout`
  * `api_key`

* 自动拼接 URL：

* request 方法默认被 @retry 和 @timer 包裹

---

## 📄 示例代码

```python
from base_client import BaseClient

client = BaseClient("https://api.example.com", timeout=5.0)

resp = client.request("GET", "/users", q="alice")

print(resp)
```

输出示例：

```json
{
  "method": "GET",
  "url": "https://api.example.com/users",
  "timeout": 5.0,
  "sent_kwargs": {"q": "alice"}
}
```

---

## 🧠 学习总结

1. **本周最难的部分是什么？你最终是怎么理解的？**
   最难的其实不是某一行代码，而是第一次看到一整块完全没见过的工程代码时的挫败感——装饰器、类型标注、BaseClient 这些一开始都非常抽象。一开始会有“这玩意我根本写不出来”的感觉，但把代码拆成一个一个小函数、一个一个参数去啃之后，会发现每一块本身其实都不复杂，难的是一下子堆在一起。拆开、重构、加打印、反复运行，是我最后理解的方式。

2. **你现在如何理解 retry 的异常处理逻辑？为什么不能重试所有异常？**
   我现在理解的 retry 是：只对“有可能下一次会成功”的异常重试，比如网络抖动、超时这类暂时性的错误；而对代码逻辑错误（TypeError、ValueError 这种）不重试，因为它们多重试 N 次也不会变对，只会掩盖真正的问题。所以才需要 `exceptions=(ConnectionError, ...)` 这种设计，只重试“有价值的异常”，其他错误要尽快暴露出来。

3. **timer 装饰器让你理解了什么是“高阶函数”和“装饰器”本质？**
   通过 timer 我对装饰器的本质更清楚了：装饰器就是一个**高阶函数**——它接收一个函数，返回一个新的函数，中间在不改变原函数调用方式的前提下“加料”（比如计时）。以前我只知道“装饰器是语法糖”，现在更能从代码层面理解：`@timer` 其实就是 `func = timer(func)`，装饰器是用高阶函数把横切逻辑（计时、重试、日志）抽出来复用的一种模式。

4. **BaseClient 的核心价值是什么？它和 OpenAI 官方 Client 的关系是什么？**
   BaseClient 的核心价值不是“把 URL 打印出来”，而是：统一存放 `base_url` / `timeout` / `api_key` 这些配置，并提供一个带重试和计时的 `request()` 入口，让所有 API 调用都走同一套逻辑。可以理解成：OpenAI 官方 Client 是为 OpenAI 这一个服务封装好的特化版客户端，而我的 BaseClient 是一个通用的底座，未来可以用来包 OpenAI、自己的 FastAPI 服务，或者任意 HTTP API。

5. **你觉得自己 Week1 最大的进步是什么？**
   最大的进步是从“只会跑别人示例代码”迈出第一步，开始接触真正的工程写法：装饰器、类型标注、`if __name__ == "__main__"`、模块拆分、以及 GitHub 仓库管理。这一周对 Python 的语法和工程风格都熟悉了一点，也终于有了自己的一个仓库，能把每天的代码和心路记录下来，这是一个很重要的起点。

---

## 🧪 运行方式

```
python week1/base_client.py
```

---

## 🔮 Week 2 预告

* 真正发 HTTP 请求（requests / httpx）
* 异步客户端（async + aiohttp）
* Pydantic 模型校验
* 并发性能对比

Week1 的 BaseClient 会作为 Week2 的底座继续升级。
