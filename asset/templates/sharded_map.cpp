template <typename K, typename V, std::size_t N = 16>
class ShardedMap {
 public:
  void insert(K k, V v) {
    auto& s = shard(k); std::scoped_lock lk(s.mu); s.m.insert_or_assign(std::move(k), std::move(v));
  }
  std::optional<V> find(const K& k) const {
    const auto& s = shard(k); std::scoped_lock lk(s.mu);
    if (auto it = s.m.find(k); it != s.m.end()) return it->second; return std::nullopt;
  }
 private:
  struct Shard { mutable std::shared_mutex mu; std::unordered_map<K, V> m; };
  mutable std::array<Shard, N> shards_;
  Shard& shard(const K& k) const { return shards_[std::hash<K>{}(k) % N]; }
};
