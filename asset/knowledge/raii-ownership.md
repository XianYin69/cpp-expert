# raii-ownership — RAII 与所有权建模

## 判据要点

- 默认所有权是**值语义**；只有确实需要堆、多态或共享时才引入智能指针。[cse R.1/R.3]
- `unique_ptr` = 独占所有权，零开销（与裸指针同尺寸、同 ABI，删除器为空时）。[cppref]
- `shared_ptr` = 共享所有权，代价是控制块（两次分配，除非 `make_shared`）、原子引用计数、
  循环引用风险。默认**不是** `shared_ptr`；用它必须能回答「谁最后释放」。[cse R.32]
- `weak_ptr` = 观察者，不延长生命周期；用于缓存、回指父节点、`enable_shared_from_this` 前的探测。
- 非拥有指针参数：优先 `T&` / `const T&` / `std::span<T>` / `std::string_view`；
  需可空时用 `gsl::not_null<T*>` 表达「绝不空」，或 `T*` 明确注释为观察者。[cse F.9/F.23]
- 禁止 `new`/`delete` 出现在业务代码：用 `make_unique` / `make_shared`；数组用 `std::vector`/`std::array`/`std::span`。[cse R.11]
- 自定义删除器场景：C API 句柄（`FILE*`、`sqlite3*`、`HWND`）→ `unique_ptr<T, Deleter>` 包一层，
  删除器必须 `noexcept`。
- `shared_ptr<T[]>` 存在但笨重；数组共享优先 `vector` 装进 `shared_ptr<vector<T>>`。
- 跨线程转移所有权：`std::move` 进队列/`std::packaged_task`；**不要**把 `unique_ptr` 的引用交给线程。
- 悬垂三大来源：返回局部对象引用/指针、`string_view`/`span` 指向已析构容器、
  lambda 捕获 `this` 后对象先亡。[cppref]
- 容器与迭代器失效：`vector` 扩容使全部指针失效；`unordered_map` rehash 使迭代器失效但**引用仍有效**；
  `list`/`deque` 规则各异——存指针前先确认失效语义。
- 对象生命周期：`std::optional` 内建/析构对象，避免「半构造 + 裸指针」状态。

## 常见误判

- 把「共享」当默认：`shared_ptr` 满天飞导致所有权不可推理、释放点不可预测。
- `shared_ptr<T> p; p.reset(new T)` 与 `make_shared` 混用（异常安全差异 + 分配次数差异）。
- 在头文件里 `inline` 删除器捕获状态：`unique_ptr` 尺寸被撑大。

## 取证

`ownership_audit.py <files>` 找嫌疑 → `sanitizer_cmd.py --kind asan --run` 定罪（leak/use-after-free）。
