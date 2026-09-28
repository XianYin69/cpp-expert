"""perf_advice.py — 性能与缓存局部性静态启发式（容器/拷贝/遍历/分配）。"""
import re, sys, argparse
P = [
    (r"\bstd::list\b|\bstd::forward_list\b", "node-based container: poor locality",
     "prefer std::vector/deque unless iterators must be stable [book]"),
    (r"\bstd::(map|set)\b", "tree container: pointer chasing per lookup",
     "prefer unordered_* + reserve, or sorted vector + binary search [cse]"),
    (r"\bstd::(unordered_map|unordered_set)\b(?![^;]*reserve)", "hash container without reserve",
     "call reserve(n) to avoid rehash + pointer churn"),
    (r"for\s*\(\s*(?:const\s+)?(?:std::)?string\s+\w+\s*:", "by-value range-for over strings",
     "use auto&& / string_view; avoid per-iteration copy"),
    (r"\.size\s*\(\s*\)\s*(?:<=|<|!=|==)\s*\w+\s*\)|for[^;]*;\s*\w+\.size\s*\(\s*\)",
        "size() in loop condition",
     "hoist, or use ranges; watch signed/unsigned compare"),
    (r"\bpush_back\s*\(", "push_back without reserve / may copy",
     "reserve(n) first; prefer emplace_back for in-place ctor"),
    (r"\bsubstr\s*\(|\bstd::string\s*\(\s*\w+\s*,\s*\w+\s*,", "substr allocates per call",
     "use std::string_view for non-owning slices [cse]"),
    (r"\bnew\s+\w+\s*\(", "per-object heap allocation in hot path",
     "arena/pool or vector of values for locality"),
    (r"\bstd::endl\b", "endl flushes stream each time", "use '\\n'"),
    (r"\bpow\s*\(\s*\w+\s*,\s*2\s*\)|\bx\s*\*\s*x\b.*pow", "pow for integer square",
        "multiply directly"),
    (r"\bvector\s*<\s*(?:std::)?(string|vector)\b", "vector of heap-allocated elements",
     "consider struct-of-arrays / string_view interning"),
]

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("files", nargs="+"); a = ap.parse_args()
    for f in a.files:
        src = open(f, encoding="utf-8", errors="ignore").read()
        hits = []
        for i, line in enumerate(src.splitlines(), 1):
            s = line.split("//")[0]
            for pat, why, fix in P:
                if re.search(pat, s):
                    hits.append((i, why, fix, s.strip()[:90])); break
        print(f"== {f}: {len(hits)} candidate(s)")
        for ln, why, fix, txt in hits[:25]:
            print(f"  L{ln}: {why} -> {fix}\n      {txt}")
    print("\nnote: heuristics only. Measure first: perf stat -e cache-misses,LLC-load-misses "
          "/ hotwords / valgrind --tool=cachegrind. Never claim 'faster' without numbers.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
