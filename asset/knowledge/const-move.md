# const-move — const 正确性与移动语义

## 判据要点

- 默认：不修改对象状态的成员函数一律 `const`；`this` 逃逸（存进容器、交给线程）是 const 泄漏主因。
- 逻辑 const vs 位 const：缓存、互斥锁用 `mutable`，语义上仍算只读。[cse Con.3]
- 顶层 `const` 参数（`void f(const T)`）无意义且破坏模板推导；只关心**指针/引用指的东西**是否 const。
- 返回 `const T` 的按值结果会阻断移动（旧技巧，C++11 起**不要**这么写）。
- `std::move` 只是 `static_cast<T&&>`，不产生任何机器码；移动后对象处于「有效但未指定」状态，
  只可析构或重新赋值。[cppref]
- 不要 `std::move` 局部返回值：会**抑制** NRVO/copy elision，通常更慢。
- 转发引用 `T&&` + `std::forward<T>` 只出现在模板里；非模板的 `Widget&&` 是右值引用。
- 完美转发陷阱：`0`/`nullptr`/字面量丢失类型、数组退化为指针、
  重载决议把转发引用吸成万能匹配（应加 `requires`/`static_assert` 收窄）。
- `constexpr`：能在编译期算就标；C++20 起 `constexpr` 虚函数、`consteval`（强制编译期）、
  `constinit`（避免静态初始化顺序问题）各有明确用途。
- `std::string_view` / `std::span`：非拥有视图，**生命周期由调用方保证**；
  不要返回指向局部字符串的 view，不要把它当「参数类型万能解」。
- 移动赋值要处理自赋值并释放旧资源；移动操作应把源置为可析构状态（通常置空）。

## 常见误判

- 给 `const` 成员函数加锁却用非 `mutable` mutex → 编译失败后改用 `const_cast`（UB 风险）。
- `std::move` 后继续读原对象（值未指定）。
- 用 `forward<T>(x)` 两次（第二次已是 moved-from）。

## 取证

`const_audit.py` + clang-tidy `readability-*,performance-*`；
`-Wreturn-type-c-linkage -Wuninitialized -Wpessimizing-move -Wredundant-move`。
