template <typename T>
concept Numeric = std::integral<T> || std::floating_point<T>;

template <Numeric T>
T clamp(T v, T lo, T hi) noexcept { return v < lo ? lo : (v > hi ? hi : v); }
