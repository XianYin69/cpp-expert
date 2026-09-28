# STL源码剖析

- 作者：侯捷
- 出版：华中科技大学出版社，2002-6
- 出处：https://book.douban.com/subject/1110934/ （[联网] 取证 2026-09-28）
- 映射知识叶：stl-algorithms · performance-cache · raii-ownership

## 摘要（要点为 [本地] 常识，书目信息为 [联网] 确证）

1. 以 SGI 实现为样本剖析容器内部结构：allocator、迭代器萃取、空间配置与两阶段构造。
2. 支撑「选型看复杂度与内存局部性」类结论：`vector` 连续布局 vs `list` 节点跳转。
3. 时代局限：基于 C++98/SGI，不代表 libstdc++/libc++/MSVC STL 现状，性能结论须实测。
4. 现代容器行为（`pmr`、`reserve` 策略、移动语义）须查 cppreference 与实现源码。

## 相关

- [知识树索引](../知识树/知识树.md) · [performance-cache](../../asset/knowledge/performance-cache.md)
