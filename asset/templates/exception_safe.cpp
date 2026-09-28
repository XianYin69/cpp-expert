// strong guarantee via copy-and-swap
void Container::push_back(Value v) {   // nothrow-move or basic guarantee
  Container tmp(*this);                // strong: work on copy
  tmp.data_.push_back(std::move(v));
  swap(tmp);                           // noexcept commit point
}
