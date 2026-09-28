# exception-safety — 异常安全与错误处理

## 判据要点

- 三级保证：**基本**（不泄漏、对象处于有效状态）、**强**（操作要么成功要么完全回滚，
  通常 copy-and-swap）、**noexcept**（不抛，失败即终止/错误码）。每个公开接口应声明属于哪一级。
- 强保证标准实现：在副本上完成全部可能失败的工作，最后用 `noexcept` 的 `swap` 提交。[cse E.15]
- 析构函数、`swap`、移动操作、`noexcept` 函数中抛异常 → `std::terminate`；
  资源释放路径必须吞掉或转成错误码。
- 不要在构造函数里做可失败的多步工作（无法回滚）；用工厂函数 + `optional`/`expected` 或两阶段初始化。
- 错误选择规则：可恢复且调用方需处理 → 返回值（`std::expected<T, E>` C++23 / `error_code`）；
  罕见且需跨层传播 → 异常；性能关键且失败可预测 → `error_code`/`status`。
  同一 API 层不要混用两种风格。[cse E.1/E.4/E.6]
- 捕获：优先 `catch (const T&)`（按值捕获会切片、按引用捕获临时会悬垂于重抛）；
  不要 `catch (...)` 后静默返回成功；重抛用裸 `throw;`（保留原始异常）。
- 异常对象必须可拷贝（跨线程 `std::exception_ptr` 传播用 `current_exception`/`rethrow_exception`）。
- `-fno-exceptions` 环境（嵌入式/游戏热路径）：本叶结论多数失效，改用 `expected`/错误码，
  并在交付里标注边界。
- 容器与异常：`vector` 扩容抛异常时原内容不变（强保证）；`std::map::insert_or_assign` 基本保证。

## 取证

`ub_scan.py` 找析构抛出与吞异常；`-fexceptions -frtti` 与 `-Wnoexcept`、clang-tidy
`bugprone-exception-escape`、`performance-no-automatic-move`。
