"""ub_scan.py — UB 与可移植性反模式静态扫描（对齐 UBSan 检查项）。"""
import re, sys, argparse
P = [
    (r"\bstrcpy\s*\(|\bstrcat\s*\(|\bsprintf\s*\(", "unbounded C string copy",
        "std::string / bounded snprintf"),
    (r"\breinterpret_cast\b", "aliasing / strict-aliasing UB risk",
        "std::bit_cast / gsl::as_bytes [std]"),
    (r"\b(?:malloc|realloc|calloc)\s*\(", "C allocator with C++ types: no ctor/dtor",
        "make_unique [cse R.11]"),
    (r"return\s+&\s*\w+\s*;", "dangling return of local address", "return by value"),
    (r"\b(?:int|long|char)\s+\w+\s*\[\s*\]", "C-style array, size erased on decay",
        "std::array / std::span"),
    (r"\bvolatile\b", "volatile is not atomic: data race UB", "std::atomic [std]"),
    (r"\b(?:switch)\s*\([^)]*\)[^{]*\{(?![^}]*default)",
        "switch without default: fallthrough UB-ish", "add default"),
    (r"\b\w+\s*\[\s*\w+\s*\+\s*1\s*\]", "off-by-one indexing candidate", "span::subspan / at()"),
    (r"\bunsigned\b[^;]*[-+]\s*1", "unsigned wraparound candidate", "signed or explicit guard"),
    (r"\bdelete\s+\w+\s*;[^/]*\bdelete\s+\w+\s*;", "double delete candidate", "unique_ptr"),
    (r"\bva_arg|__attribute__\s*\(|#ifdef\s+_MSC_VER", "non-portable extension",
        "standard C++ / feature test macro"),
]

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("files", nargs="+"); a = ap.parse_args()
    tot = 0
    for f in a.files:
        src = open(f, encoding="utf-8", errors="ignore").read()
        hits = []
        for i, line in enumerate(src.splitlines(), 1):
            s = line.split("//")[0]
            for pat, why, fix in P:
                if re.search(pat, s):
                    hits.append((i, why, fix, s.strip()[:100])); break
        print(f"== {f}: {len(hits)} finding(s)")
        for ln, why, fix, txt in hits[:30]:
            print(f"  L{ln}: {why} -> {fix}\n      {txt}")
        tot += len(hits)
    print(f"\ntotal: {tot}; confirm with -fsanitize=undefined,undefined-trap via sanitizer_cmd.py")
    return 0

if __name__ == "__main__":
    sys.exit(main())
