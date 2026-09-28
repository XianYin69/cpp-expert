// non-owning view: caller guarantees lifetime
void render(std::span<const std::string_view> lines) noexcept;
class Node;
struct Parent { std::unique_ptr<Node> owned; };   // owner
struct Child  { Node* view; };                     // observer, never deletes
