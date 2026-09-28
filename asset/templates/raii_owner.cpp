class Conn {
 public:
  explicit Conn(std::string host) : host_(std::move(host)) {}
  Conn(const Conn&) = delete;        // non-copyable resource
  Conn& operator=(const Conn&) = delete;
  Conn(Conn&&) noexcept = default;
  Conn& operator=(Conn&&) noexcept = default;
  ~Conn() { close(); }               // single release point
 private:
  void close() noexcept {}
  std::string host_;
};
