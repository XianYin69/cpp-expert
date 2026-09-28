# Effective Modern C++（中文版）

- 原作名：Effective Modern C++
- 作者：[美] Scott Meyers；译 高博
- 出版：中国电力出版社，2018-4
- 出处：https://book.douban.com/subject/30178902/ （[联网] 取证 2026-09-28）
- 映射知识叶：const-move · raii-ownership · special-members · templates-concepts

## 摘要（要点为 [本地] 常识，书目信息为 [联网] 确证）

1. 42 条针对 C++11/14 的判据式条目：auto 类型推导、移动与完美转发、智能指针选型、lambda。
2. 常用作 advisory（建议）级结论出处：`std::move`/`std::forward` 语义边界、
   `unique_ptr` 作默认所有权、`const` 正确性与 Rule of 0/5/6。
3. 判 blocking（阻塞）仍须标准条文或工具实测，条目式论断不单独充当规范依据。
4. 局限：不覆盖并发内存序、构建系统与静态分析器实操。

## 相关

- [知识树索引](../知识树/知识树.md) · [cpp-primer](../语言基础/cpp-primer.md)
