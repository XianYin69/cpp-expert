# 评审清单 · templates-concepts
- [ ] blocking | 依赖名未加 this->/显式限定（两阶段查找错误） | [cppref]
- [ ] blocking | 传给 std::sort 的比较谓词非严格弱序 -> UB | [cppref]
- [ ] major | C++20 目标仍用 enable_if 而非 concepts | [cse T.43]
- [ ] major | 想「偏特化」函数模板（非法）应改重载或 if constexpr | [cppref]
- [ ] major | 完美转发对 0/nullptr/数组/字面量失真 | [book EMC 26]
- [ ] major | 公开模板接口缺 requires/static_assert 契约 | [cse T.1]
- [ ] minor | ADL 钩子用 using 声明 + 非限定调用惯用法 | [cppref]
- [ ] verify | g++ -std=c++20 -fsyntax-only + static_assert 契约
