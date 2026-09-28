# 评审清单 · headers-modules

- [ ] blocking | 头文件不自包含或 include guard 宏名冲突 | [cse SF.7]
- [ ] blocking | 同一实体在不同 TU 定义不一致 (ODR -> UB) | [cppref]
- [ ] major | 头文件里 using namespace std; 或静态全局定义 | [cse SF.7/SF.25]
- [ ] major | 仅用指针/引用却完整 include（应前向声明） | [cse SF.1]
- [ ] major | 公共头泄漏第三方类型导致重编风暴（PIMPL） | [cse SF.11]
- [ ] major | 多语句宏未用 do{}while(0) 包裹 | [cse]
- [ ] minor | 未量化编译时间/依赖深度就引入 modules | [book]
- [ ] verify | include-what-you-use + -ftime-trace 实测
