# templates-concepts — 模板、概念与重载决议

## 判据要点

- C++20 起优先 **concepts** 而非 SFINAE：`requires` 子句给出可读约束与干净报错。[cppref]
- SFINAE 仅用于「替换失败是软错误」的上下文；`typename T::type` 之外的硬错误不受 SFINAE 保护。
  旧代码 `std::enable_if_t<>` 迁移到 `requires` 时保留行为等价性验证。
- 两阶段名字查找：非依赖名在定义期查找，依赖名在实例化期查找；基类依赖时需 `this->` 或显式限定。
- ADL（实参依赖查找）：对 `std::swap`/`operator<<` 等钩子，用「using 声明 + 非限定调用」惯用法。
- 重载决议顺序：完全匹配 > 转换 > 用户定义转换 > 模板实参推导；
  非模板函数优先于模板特化（同签名时）——这是「特化不是重载」的经典误判源。
- 函数模板**不能**偏特化；要分派请用重载或 `if constexpr` + tag。
- `if constexpr` 在编译期丢弃分支（要求条件为常量表达式），替代标签分发。
- CTAD 与推导指南：无括号默认构造在 C++17/20 的歧义（`T x{};` vs `T x();`）注意 most vexing parse。
- 变参模板：折叠表达式（C++17）优先于递归展开；`sizeof...` 用于诊断。
- 模板报错可读性：约束前置、`static_assert(false, "...")` 在依赖上下文中才合法（C++20 未实例化分支）。
- 概念设计原则：约束应表达**语义**（`Range`、`Invocable`）而非语法巧合；避免过度约束阻碍可组合性。

## 常见误判

- 用 `std::is_same_v<T, int>` 排除类型而非用 `integral` 概念。
- 忘记 `template<>` 或写了全特化却期望偏特化生效。

## 取证

`g++ -std=c++20 -fsyntax-only` + `static_assert` 契约；`template_gen.py --kind concept` 出骨架。
