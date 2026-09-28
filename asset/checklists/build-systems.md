# 评审清单 · build-systems

- [ ] blocking | 跨 DLL/SO 边界传 C++ 类型且 ABI 不一致 | [std]
- [ ] blocking | 标准档未固定（依赖编译器默认） | [cse]
- [ ] major | 全局 include_directories/link_libraries 而非 target 级 | [book Modern CMake]
- [ ] major | PUBLIC/PRIVATE/INTERFACE 可见性用错方向 | [cmake docs]
- [ ] major | file(GLOB) 收集源文件（不触发重配置） | [cmake docs]
- [ ] major | 依赖无版本锁定（手动 clone 第三方） | [cse PF.1]
- [ ] minor | 未生成 compile_commands.json（阻断 clang-tidy） | [clang docs]
- [ ] verify | cmake_probe.py --dir <proj> + cmake -S . -B build 实跑
