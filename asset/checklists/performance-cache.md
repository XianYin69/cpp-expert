# 评审清单 · performance-cache

- [ ] blocking | 无基准数据即断言更快或更慢 | [本技能红线]
- [ ] major | 热路径存在未量化的堆分配（每帧 new） | [cse Per.4]
- [ ] major | 指针追逐型容器出现在热循环 | [book]
- [ ] major | 多线程写同一缓存行未填充/分片（伪共享） | [cse]
- [ ] major | 移动操作缺 noexcept 导致容器退化拷贝 | [cppref]
- [ ] major | 未查向量化报告即声称已优化 | [compiler docs]
- [ ] minor | 字符串拼接/endl 可换 string_view 与 '\n' | [cse]
- [ ] verify | perf stat -e cycles,instructions,cache-misses + Google Benchmark
