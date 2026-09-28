# C++并发编程实战（第 2 版）

- 原作名：C++ Concurrency in Action, Second Edition
- 作者：[英] Anthony M. Williams；译 吴天明
- 出版：人民邮电出版社（异步图书），2021-11
- 出处：https://book.douban.com/subject/35653912/ （[联网] 取证 2026-09-28）
- 映射知识叶：concurrency-memory-model · ub-portability · exception-safety

## 摘要（要点为 [本地] 常识，书目信息为 [联网] 确证）

1. `std::thread`/`mutex`/`lock_guard`/`future` 与线程安全数据结构的系统讲法。
2. 内存模型部分：`memory_order_*` 语义、happens-before、数据竞争的定义与后果（UB）。
3. 判「有无数据竞争」须以 TSan 实测或标准条文为据，本书属解释性材料。
4. 局限：第 2 版止于 C++17/20 前沿，coroutine 与 `std::jthread` 细节需查 cppreference。

## 相关

- [知识树索引](../知识树/知识树.md) · [cpp-programming-language](../语言基础/cpp-programming-language.md)
