# 评审清单 · special-members
- [ ] blocking | 有所有权却未写全部特殊成员（浅拷贝双释放） | [cse C.66]
- [ ] blocking | 多态基类缺 virtual 析构且经基类指针 delete -> UB | [cppref]
- [ ] major | 手写析构但未同时提供拷贝/移动（Rule of 3/5 不一致） | [cse C.67]
- [ ] major | 移动构造/赋值未标 noexcept（容器扩容退化为拷贝） | [book EMC]
- [ ] major | 拷贝赋值未处理自赋值或未用 copy-and-swap | [cse]
- [ ] major | 禁用拷贝用 = delete 而非私有未实现 | [cse C.14]
- [ ] minor | 靠成员语义消除手写特殊成员（Rule of 0） | [cse C.67]
- [ ] verify | const_audit.py + clang-tidy cppcoreguidelines-special-member-functions
