# 评审清单 · const-move
- [ ] blocking | const 对象经 const_cast 修改 -> UB | [std]
- [ ] major | 不修改状态的成员函数缺 const | [cse Con.1]
- [ ] major | 锁成员未 mutable 导致 const 方法无法加锁 | [cse Con.3]
- [ ] major | 大对象按值传参（应 const&/string_view/span） | [cse F.16]
- [ ] major | 对局部返回加 std::move（抑制 NRVO） | [book EMC 25]
- [ ] major | std::move 后继续使用源对象（状态未指定值） | [cppref]
- [ ] major | 万能引用模板无约束，吞掉所有重载 | [cse T.43]
- [ ] minor | 可编译期求值的函数未加 constexpr | [cse]
- [ ] verify | const_audit.py + -Wpessimizing-move -Wredundant-move
