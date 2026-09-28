# 评审清单 · stl-algorithms
- [ ] blocking | 迭代器失效后继续使用（erase/insert/扩容） | [cppref]
- [ ] blocking | 谓词不满足严格弱序或遍历时改动序列 | [cppref]
- [ ] major | 默认容器不是 vector（list/map 无充分理由） | [cse SL.1]
- [ ] major | unordered_* 未 reserve 或自定义 hash/eq 不一致 | [cse]
- [ ] major | 手写循环替代标准算法/ranges（语义更清晰） | [cse SL.6]
- [ ] major | 二分在未排序序列或谓词不一致上执行 | [cppref]
- [ ] minor | 用 std::erase_if / erase-remove 惯用法删元素 | [cse]
- [ ] minor | C 数组改 std::array/std::span | [cse SL.10]
- [ ] verify | -D_GLIBCXX_DEBUG 或 MSVC _ITERATOR_DEBUG_LEVEL=2 实跑
