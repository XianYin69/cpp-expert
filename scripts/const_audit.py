"""const_audit.py - const-correctness / move-semantics gaps (Rule of 5)."""
import re, sys, argparse
SIG = re.compile(
    r"^\s*(?:virtual\s+)?(?:static\s+)?"
    r"[\w:<>,\s*&\[\]]*?\b(\w+)\s*\(([^)]*)\)"
    r"\s*(const)?\s*(override)?\s*(noexcept)?")
BYVAL = re.compile(r"\b(?:std::)?(string|vector|map|unordered_map|set|deque|list)\s+\w+\s*[,)]")
COPY = re.compile(r"operator=\s*\(\s*(?:const\s+)?[\w:]+\s*&")
MOVE = re.compile(r"(operator=\s*\(\s*[\w:]+\s*&&|\b\w+\s*\(\s*[\w:]+\s*&&\s*\w*\s*\))")
SKIP = ("if", "for", "while", "return", "switch", "catch", "sizeof", "operator")

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("files", nargs="+"); a = ap.parse_args()
    for f in a.files:
        src = open(f, encoding="utf-8", errors="ignore").read()
        hits = []
        if COPY.search(src) and not MOVE.search(src):
            hits.append((0, "Rule of 5 gap: copy-assignment without move operations [cse C.66]",
                ""))
        for i, line in enumerate(src.splitlines(), 1):
            s = line.split("//")[0]
            m = SIG.match(s)
            if m and m.group(3) is None and m.group(1) not in SKIP and re.search(r"[{;]\s*$", s):
                hits.append((i, "non-const member fn - verify no mutation, then const-ify",
                    s.strip()[:90]))
            if BYVAL.search(s) and "const" not in s and "&&" not in s:
                hits.append((i, "large object passed by value -> string_view/span/const&",
                    s.strip()[:90]))
        print(f"== {f}: {len(hits)} finding(s)")
        for ln, why, txt in hits[:30]:
            print(f"  L{ln}: {why}" + (f"\n      {txt}" if txt else ""))
    print(
        "\nnote: heuristic; confirm with clang-tidy readability-*/performance-* and -Wall -Wextra")
    return 0

if __name__ == "__main__":
    sys.exit(main())
