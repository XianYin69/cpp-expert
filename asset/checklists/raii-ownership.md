# 评审清单 · raii-ownership
- [ ] blocking | 业务代码无裸 new/delete/malloc/free（分配器层除外并注明） | [cse R.11]
- [ ] blocking | 无返回局部对象引用/指针；无 string_view/span 指向已析构对象 | [cppref]
- [ ] blocking | 容器元素指针在扩容/rehash 后仍被使用 -> 复核失效语义 | [cppref]
- [ ] major | 独占资源用 unique_ptr，而非把 shared_ptr 当默认所有权 | [cse R.32]
- [ ] major | shared_ptr 能回答「谁最后释放」，回指用 weak_ptr 破环 | [cse R.32]
- [ ] major | 非拥有参数用 T&/span/string_view/not_null 而非裸指针 | [cse F.9/F.23]
- [ ] minor | 可缺省对象用 std::optional 取代「指针为空判断」 | [cse]
- [ ] verify | python -B scripts/ownership_audit.py <file> 取证后再判
