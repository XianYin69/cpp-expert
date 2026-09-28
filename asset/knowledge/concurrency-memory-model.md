# concurrency-memory-model — 并发与内存模型

## 判据要点

- 数据竞争定义：两个线程访问同一内存位置，至少一个是写，且无同步 → **UB**（不是「偶发错值」）。[std]
- 默认锁方案：`std::scoped_lock`（多锁防死锁）/ `std::lock_guard`（单锁）/
  `std::unique_lock`（需延迟、条件变量、转移所有权）；读写比悬殊用 `std::shared_mutex`
  但注意写者饥饿与「共享锁只保护读，不保护写」。
- 永远不要手写 `m.lock()/m.unlock()` 配对（异常路径漏解锁）；`recursive_mutex` 是设计缺陷信号。
- 条件变量必须带谓词：`cv.wait(lk, []{ return ready_; })`，否则虚假唤醒；
  改谓词状态**必须在持锁时**并 `notify` 前决定是否需解锁。
- `std::atomic` 提供**单个对象**的原子性，不提供多对象事务；跨字段不变量仍需锁。
- 内存序：默认 `seq_cst`；`acquire/release` 配对建立同步（发布-订阅）；
  `relaxed` 只保证原子性与单线程修改序，**不建立 happens-before**，用错即 UB——
  使用 `relaxed` 必须写明理由（如引用计数递减、统计计数器）。
- 引用计数：`shared_ptr` 的控制块计数是原子的，但**指向的对象不是**；
  同一 `shared_ptr` 实例被多线程读写仍需锁（对象级 vs 指针级锁）。[cppref]
- `volatile` **不是**原子、不是同步、不禁止重排；与 `std::atomic` 混用是常见误判。
- 线程生命周期：`std::thread` 析构时既未 join 也未 detach → `std::terminate`；
  C++20 `std::jthread` 自动 join + `stop_token` 协作停止。
- `std::async` 默认 `launch::async | launch::deferred`：deferred 可能永不执行，
  依赖副作用时必须显式 `launch::async`。
- 逃逸检查：把 `this`/引用交给线程前确保对象存活（用 `shared_from_this` 或值捕获）。
- 死锁四条件与破解：固定加锁顺序、`std::scoped_lock(a,b)`、超时 `try_lock_for`、避免持锁回调。
- 无锁结构：只在实测证明锁是瓶颈后引入，且必须 TSan + 形式化推理 + ABA 处理（`tagged_ptr`/epoch GC）。
- C++20 协程：`co_await` 挂起点即线程切换点，局部变量生命周期由帧管理；
  默认执行器语义、`promise_type` 与异常传播是主要坑区。

## 取证

`concurrency_probe.py` 出嫌疑 → `sanitizer_cmd.py --kind tsan --run` 定罪；
`Helgrind/DRD`（valgrind）与 MSVC `/fsanitize=address` 无 TSan 时用 clang-cl。
