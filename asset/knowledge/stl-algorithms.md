# stl-algorithms — STL 容器、迭代器与算法选型

## 判据要点

- 默认容器 `std::vector`：连续内存、缓存友好、摊销 O(1) 尾部插入。[cse SL.1]
- `deque`：两端 O(1) 且块状连续；`list`/`forward_list` 仅在「迭代器/引用必须长期稳定」或
  已知需频繁中间插删且不在乎局部性时使用。
- 有序 `map`/`set`：需要稳定引用、有序遍历或范围查询时用；纯查找优先
  `unordered_*` + `reserve()`，或「排序 vector + `std::lower_bound`」（局部性更好）。
- 迭代器失效是首要 UB 源：`vector` 扩容全失效；`insert/erase` 其后失效；
  `unordered_*` rehash 使迭代器失效但**元素引用/指针仍有效**；`list` 仅失效被删元素。
- 算法优先于手写循环：`std::transform`/`find_if`/`any_of`/`accumulate`/`reduce`/`for_each`。
  C++20 ranges：`std::views::filter|transform|take` 组合可惰性求值，注意重复遍历代价与
  `dangling` view（`ref_view` 指向临时）。
- 二分前提：序列已按同一比较器排序；`equal_range`/`lower_bound` 与 `binary_search` 别混用不同谓词。
- 比较谓词必须建立**严格弱序**（`<` 而非 `<=`），否则 `std::sort` 是 UB（可越界）。
- `std::sort`（快排，O(n log n) 平均，不稳定）vs `std::stable_sort`（归并，需额外内存，保序）。
- 拷贝 vs 交换：容器整体替换用 `std::swap`（O(1)）；`erase-remove` 惯用法
  （C++20 用 `std::erase_if`）。
- `std::array` 替代 C 数组；`std::span` 作参数接收连续序列（含 C 数组/vector 片段）。
- 小对象优化：`std::string` 短字符串、`std::variant` 替代继承层次（值语义 + 无堆）。

## 取证

`perf_advice.py` 找容器/局部性问题；`-D_GLIBCXX_DEBUG` / `_LIBCPP_DEBUG` / MSVC `_ITERATOR_DEBUG_LEVEL=2` 抓失效。
