# 评审清单 · ub-portability

- [ ] blocking | 有符号溢出/越界/空指针解引用/未初始化读 | [std]
- [ ] blocking | reinterpret_cast 类型双关违反严格别名 | [std]
- [ ] blocking | 悬垂引用（绑定临时量、返回局部地址） | [cppref]
- [ ] blocking | placement new 后未显式析构或生命周期外访问 | [cppref]
- [ ] major | 跨平台序列化用 int/long 而非 int32_t/uint64_t | [cse I.1]
- [ ] major | 依赖求值顺序（函数参数副作用）或位域布局 | [cppref]
- [ ] major | 用 _MSC_VER 猜测特性而非 __cpp_lib_* 测试宏 | [cse I.3]
- [ ] minor | char 符号性/字节序假设未显式处理 | [book]
- [ ] verify | ub_scan.py -> sanitizer_cmd.py --kind ubsan --run
