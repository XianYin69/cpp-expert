# special-members — Rule of 0/3/5 与特殊成员函数

## 判据要点

- **Rule of 0（首选）**：成员全是值语义或标准库/智能指针类型时，一个特殊成员都不写，
  编译器生成的即正确。[cse C.67]
- **Rule of 3**：一旦手写析构函数，几乎必然也要手写拷贝构造与拷贝赋值（否则浅拷贝双释放）。
- **Rule of 5**：C++11 起在 Rule of 3 之上补移动构造与移动赋值；
  两个移动操作必须 `noexcept`，否则 `vector` 扩容退化为拷贝（`std::move_if_noexcept`）。[cppref]
- 析构函数默认已是 `noexcept`；显式写 `throw()`/`noexcept(false)` 需极强理由。
- 多态基类：`virtual ~Base() = default;`，且**禁用拷贝**（`Base(const Base&) = delete;`）
  防止切片；允许移动则需 `noexcept`。[cse C.67]
- 自赋值安全：拷贝赋值先构造临时再 `swap`（copy-and-swap），或显式 `if (this == &o) return *this;`。
- `= delete` 优于「私有未定义」：报错更早且意图明确。
- 只写移动、禁拷贝的「移动专用类型」（如句柄、`unique_ptr` 成员）：
  拷贝 `= delete` + 移动 `= default`，编译器不会替你生成拷贝。
- 生成被抑制的规则：声明任一拷贝操作会抑制移动生成；声明移动会抑制拷贝生成（反之亦然）；
  用户声明析构会抑制移动生成。[cppref]
- 可复制/可移动性要写进接口意图：`static_assert(std::is_move_constructible_v<T>)` 当契约。

## 常见误判

- 只写析构不写拷贝 → 浅拷贝 double free（ASan 报 heap-use-after-free / double-free）。
- 移动构造里 `noexcept` 缺失 → 容器扩容性能腰斩却无人察觉。
- 用 `= default` 的析构管理裸资源 → 资源泄漏。

## 取证

`const_audit.py` 报 Rule-of-5 缺口；`-Wdeprecated-copy-dtor`、clang-tidy
`cppcoreguidelines-special-member-functions` / `*-copy-move` 系列定罪。
