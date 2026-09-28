# 代码整洁之道

- 原作名：Clean Code: A Handbook of Agile Software Craftsmanship
- 作者：[美] Robert C. Martin；译 韩磊
- 出版：人民邮电出版社（异步图书），2010-1
- 出处：https://book.douban.com/subject/4199741/ （[联网] 取证 2026-09-28）
- 映射知识叶：headers-modules · tooling-static-analysis · exception-safety

## 摘要（要点为 [本地] 常识，书目信息为 [联网] 确证）

1. 命名、函数尺寸、注释取舍、错误处理与边界的通用工程准则，语言无关。
2. 在 C++ 语境用于评审「可读性/可维护性」维度；不得据此判 UB 或性能结论。
3. 与 C++ 专项判据冲突时（如头文件极简 vs 模板实例化成本），以 C++ 条目为准。
4. 局限：示例以 Java/C++03 为主，现代 C++ 惯用法不在此书覆盖。

## 相关

- [知识树索引](../知识树/知识树.md) · [effective-modern-cpp](effective-modern-cpp.md)
