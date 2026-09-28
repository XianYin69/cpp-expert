# headers-modules — 头文件、编译防火墙与模块

## 判据要点

- 头文件必须**自包含**（自己 include 所需，不依赖包含顺序）且用 `#pragma once` 或
  include guard（guard 名全局唯一，避免不同文件同宏名导致静默丢内容）。[cse SF.7]
- ODR 违规是链接期/运行期诡异 bug 的主因：函数/类在多个 TU 中定义不同 → UB；
  内联函数与模板必须定义在头文件且各 TU 一致。[cppref]
- 编译防火墙（减少重编与耦合）：
  1) **PIMPL**：`struct X { struct Impl; std::unique_ptr<Impl> p; };` 隐藏实现细节与第三方类型；
  2) **前向声明**：指针/引用成员与参数只需声明，值成员/基类必须完整定义；
  3) 头文件里避免 `using namespace std;`（污染所有包含者）。[cse SF.1/SF.11]
- 头文件里不要放静态全局变量定义（每 TU 一份，语义意外）；用 `inline` 变量（C++17）或
  函数返回局部静态。
- 匿名命名空间 = 内部链接（.cpp 内私有）；`static` 函数是旧写法。
- 宏的代价：无类型、无作用域、调试不可见、易与函数调用语法冲突；
  用 `constexpr` 函数/变量、`inline` 函数、模板替代；确需宏时用 `do{}while(0)` 包裹多语句。
- 头文件依赖爆炸的度量：`include-what-you-use` 报告 + 编译时间基线；
  解法顺序：前向声明 → 拆分接口头 → PIMPL → 模块。
- C++20 modules：`import:` 取代文本包含，消除宏泄漏与重复解析；
  但工具链（MSVC/Clang/GCC 支持度差异）、BMI 缓存与混合 TU 规则仍不成熟——
  引入前必须实测目标编译器版本，不得凭「模块更好」下结论。
- 循环依赖破解：抽出共同接口到头文件 A，或引入第三方薄头 C；不要用「包含顺序技巧」。

## 取证

`tidy_config_gen.py --check` 看 iwyu 可用性；`cmake_probe.py` 看目标级 include 作用域；
编译时间对比须实测（`-ftime-trace` / `ccache -s`）。
