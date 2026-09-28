# performance-cache — 性能与缓存局部性

## 判据要点

- 铁律：**先测量再优化**。任何「更快」结论必须附基准数字与机器/编译器/标准档；
  禁止凭直觉断言（本技能红线）。
- 局部性优先：L1 命中 ~1ns、主存 ~80ns、跨核缓存行迁移更贵；
  连续遍历（SoA、`vector<T>`）通常胜过指针追逐（AoP、`list<Node*>`）。
- 数据结构布局：热字段集中、冷字段分离（SoA / 冷热拆分）；
  `alignas(64)` 或填充避免**伪共享**（多线程写同一缓存行）。
- 分配是隐形成本：`reserve()` 预估容量、对象池/arena 批量分配、避免每帧 new；
  小对象频繁分配考虑 `pmr::monotonic_buffer_resource` / `pmr::pool_options`。
- 拷贝成本：按值传大对象 → `const&`/`string_view`/`span`；返回视图避免分配；
  移动需 `noexcept` 才能在容器中获益。
- 分支与预测：可预测分支优于虚函数间接调用（热循环内）；
  `[[likely]]/[[unlikely]]`（C++20）辅助布局；避免数据依赖分支（查表替代）。
- 向量化：连续内存、无别名（`std::restrict` 非标准，用 `__restrict` 或保证不重叠）、
  循环内无函数调用/异常；`-O2 -ftree-vectorize`，用编译器报告（`-fopt-info-vec`、
  `/Qvec-report:2`、`-Rpass=loop-vectorize`）验证，不靠猜。
- 别名与严格别名：`reinterpret_cast` 双关破坏别名规则会阻止优化并引入 UB → `std::bit_cast`（C++20）。
- 字符串：`string_view` 切片、避免 `+` 链式拼接（多次分配）、`fmt::format`/`std::format` 优于
  `stringstream`；`std::endl` 会 flush。
- 并发性能：锁粒度、读写锁误用（`shared_mutex` 写者饥饿）、原子 CAS 循环退化；
  并行算法 `std::execution::par`（C++17）需评估线程创建与数据规模阈值。
- 基准方法学：Google Benchmark / Catch2 benchmark，注意 DCE（`benchmark::DoNotOptimize`）、
  频率抖动、多次运行取分布；`perf stat` 看 IPC、cache-miss、branch-miss。

## 取证

`perf_advice.py` 找候选；实测用 `perf stat -e cycles,instructions,cache-misses ./app` 或
Google Benchmark 输出，未跑不得写数字。
