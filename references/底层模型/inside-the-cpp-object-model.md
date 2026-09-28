# 深度探索C++对象模型

- 原作名：Inside the C++ Object Model
- 作者：[美] Stanley B. Lippman；译 侯捷
- 出版：华中科技大学出版社，2001-5
- 出处：https://book.douban.com/subject/1091086/ （[联网] 取证 2026-09-28）
- 映射知识叶：special-members · ub-portability · headers-modules · performance-cache

## 摘要（要点为 [本地] 常识，书目信息为 [联网] 确证）

1. 对象布局、vptr/vtbl、构造与析构序列、name mangling、成员指针的底层机制讲法。
2. 支撑「虚析构必要性」「多继承布局代价」「隐式拷贝开销」类判断。
3. 具体布局是实现相关（ABI），不得当作跨编译器事实；须以 `-fdump-`/`/d2` 或实测取证。
4. 局限：成书于 C++98，无移动语义、无 `constexpr`、无 C++11 对象模型变化。

## 相关

- [知识树索引](../知识树/知识树.md) · [special-members](../../asset/knowledge/special-members.md)
