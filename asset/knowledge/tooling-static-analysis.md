# tooling-static-analysis — 静态分析与 sanitizer

## 判据要点

- 分层闸门（顺序不可颠倒）：编译器警告 → sanitizer（动态）→ clang-tidy/cppcheck（静态）→
  覆盖率 → fuzzing。静态工具报的是「模式」，sanitizer 报的是「已发生」。
- 警告基线：`-Wall -Wextra -Wpedantic -Werror` + `-Wshadow -Wconversion -Wsign-conversion
  -Wold-style-cast -Wuseless-cast -NonVirtualDtor -Wdocumentation`；
  MSVC `/W4 /permissive- /Zc:__cplusplus /w14242 /w14263 /w14265`。
- clang-tidy 需要 `compile_commands.json`（`-p build`），否则宏与标准档判断失真。
  分组：`bugprone-*`（真 bug）、`cppcoreguidelines-*`（规范）、`modernize-*`、`performance-*`、
  `readability-*`、`concurrency-*`、`misc-*`。`strict` 全开会产生大量噪音，
  新项目从 `min` 起步、按目录逐步收紧。
- ASan（地址）：堆越界、use-after-free、double-free、栈溢出、泄漏（Linux 默认开 LeakSanitizer）。
  必须 `-g -fno-omit-frame-pointer`，`ASAN_OPTIONS=detect_leaks=1:abort_on_error=1`。
- UBSan（未定义行为）：有符号溢出、除零、空指针解引用、非法枚举、对齐错误、类型双关。
  `-fno-sanitize-recover=all` 让首次命中即终止；`-fsanitize-trap` 体积更小。
- TSan（数据竞争）：与 ASan **互斥**，必须独立构建目标；`halt_on_error=1`。
  MSVC 无 TSan → 用 clang-cl 或 Windows 上 WSL。
- MSan（未初始化读）：要求**全部**依赖都被插桩，否则假阳性泛滥；实践中常改用
  `valgrind --tool=memcheck` / `MSVC /RTC1`。
- cppcheck：`--enable=warning,performance,portability --inconclusive --std=c++20`，
  擅长未使用变量、越界、内存泄漏模式；对模板与宏弱。
- 覆盖率：`-fprofile-instr-generate -fcoverage-mapping`（clang）或 `--coverage`（gcc）+
  `llvm-cov report`；行覆盖不等于分支覆盖，评审时看分支与条件覆盖。
- 工具结论必须落进交付：报告「已跑 ASan 无报错」需附命令与退出码，否则标 `evidence=none`。

## 取证

`tidy_config_gen.py --level balanced --out .clang-tidy`；
`sanitizer_cmd.py --kind asan|ubsan|tsan --compiler clang++ --run`。
