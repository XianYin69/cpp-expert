# 评审清单 · exception-safety

- [ ] blocking | 析构/移动/swap 可能抛异常 -> terminate | [cse E.15]
- [ ] blocking | catch 后静默返回成功或吞掉异常 | [cse E.16]
- [ ] blocking | 异常路径资源泄漏（无 RAII 守卫） | [cse]
- [ ] major | 公开接口未声明保证等级（基本/强/noexcept） | [book HAC 29]
- [ ] major | 强保证未走 copy-and-swap 提交点 | [cse E.15]
- [ ] major | 构造函数内做多步可失败工作（无法回滚） | [cse]
- [ ] major | 同一层混用异常与错误码两种风格 | [cse E.1/E.4]
- [ ] minor | 可恢复错误未考虑 std::expected (C++23) | [std]
- [ ] verify | -Wnoexcept + clang-tidy bugprone-exception-escape
