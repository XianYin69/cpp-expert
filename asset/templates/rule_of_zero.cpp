struct Widget {
  std::vector<int> data;            // value semantics: Rule of 0
  ~Widget() = default;
};
