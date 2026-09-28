# ub-portability — 未定义行为与可移植性

## 判据要点

- UB 不是「崩溃」而是「编译器可假设不发生」：有符号溢出、越界、空指针解引用、
  悬垂引用、未初始化读、数据竞争、双重释放、`delete` 与 `new[]` 不匹配、
  访问对象生命周期外、违反严格别名、`va_arg` 类型不匹配。[std]
- 有符号溢出 UB → 优化下可能整段循环被消除；用 `unsigned` 或 `__builtin_add_overflow`
  / `std::add_sat`（C++26）表达回绕/饱和意图。
- 严格别名：`*(int32_t*)&f` 是 UB；类型双关用 `std::memcpy` 或 C++20 `std::bit_cast`。
- 对象生命周期：placement new 后必须显式析构；`std::launder` 处理 const 成员替换；
  引用绑定临时量仅在表达式内有效（`auto& s = std::string() + "x";` 立即悬垂）。
- 未初始化：`int i;` 读即 UB；C++ 无「默认毒值」，用 `-fsanitize=memory`、
  MSVC `/RTC1`、`-Wuninitialized -Wmaybe-uninitialized`，或 `std::numeric_limits<T>::quiet_NaN()` 哨兵。
- 求值顺序：C++17 起部分表达式有确定顺序（赋值右先于左、函数参数仍**未定序**）；
  `f(g(), h())` 中 g/h 顺序不定，副作用依赖即 UB。
- 可移植性差异：`char` 是否有符号、`wchar_t` 宽度、位域布局、对齐与填充、字节序、
  浮点 `FLT_EVAL_METHOD`、`sizeof(long)`（LLP64 vs LP64）——跨平台序列化必须显式类型
  （`int32_t`/`uint64_t`）与显式编码（网络序、定长）。
- 平台扩展：`#pragma pack`、`__attribute__`、`__declspec`、匿名 union 初始化差异；
  用特性测试宏（`__cpp_lib_*`、`__cplusplus` 真实值需 MSVC `/Zc:__cplusplus`）而非 `_MSC_VER` 猜测。
- 与并发交叉：`volatile` 语义在 C++ 中只保证「每次访问都发生」，**不保证原子性与顺序**；
  多线程必须 `std::atomic` 或锁。
- 诊断顺序：UBSan（`-fno-sanitize-recover=all`）→ ASan → `-Wall -Wextra -Werror` →
  clang-tidy `bugprone-*`；复现最小化后再谈修复。

## 取证

`ub_scan.py <files>` 找模式 → `sanitizer_cmd.py --kind ubsan --run` 定罪；
跨平台结论必须在目标平台实跑，否则标 `evidence=none`。
