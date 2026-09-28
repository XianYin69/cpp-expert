"""ownership_audit.py — 扫描所有权反模式（裸 new/delete、拥有型裸指针、缺智能指针）。"""
import re, sys, argparse
NEW = re.compile(r"\bnew\s+[A-Za-z_][\w:<>]*|\bdelete\s+[\w\-> ]*|\bdelete\[\]")
RAW = re.compile(r"^\s*(?:const\s+)?[A-Za-z_][\w:]*\s*\*\s*(?:const\s+)?\w+\s*(?:[=;]|,)", re.M)
SMART = re.compile(r"\b(unique_ptr|shared_ptr|weak_ptr|make_unique|make_shared)\b")
RAWARR = re.compile(r"\bmalloc\s*\(|\bcalloc\s*\(|\brealloc\s*\(|\bfree\s*\(")
OWN = re.compile(r"\b(std::)?(vector|string|map|unordered_map|set)\s+\w+\s*\*")

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("files", nargs="+"); a = ap.parse_args()
    total = 0
    for f in a.files:
        try:
            src = open(f, encoding="utf-8", errors="ignore").read()
        except OSError as e:
            print(f"SKIP {f}: {e}", file=sys.stderr); continue
        hits = []
        for i, line in enumerate(src.splitlines(), 1):
            s = line.split("//")[0]
            if NEW.search(s): hits.append((i,
                "raw new/delete -> use make_unique/make_shared [cse R.11]", s.strip()))
            elif RAWARR.search(s): hits.append((i,
                "C allocator -> use RAII container [cse R.11]", s.strip()))
            elif OWN.search(s): hits.append((i, "owning raw pointer -> unique_ptr [cse F.9]",
                s.strip()))
            elif RAW.search(s) and not SMART.search(s):
                hits.append((i,
                    "raw pointer: classify owner vs observer (gsl::not_null/weak_ptr)", s.strip()))
        print(f"== {f}: {len(hits)} finding(s)")
        for ln, why, txt in hits[:40]:
            print(f"  L{ln}: {why}\n      {txt[:110]}")
        total += len(hits)
    print(f"\ntotal findings: {total}  (findings are suspicions; confirm with ASan/valgrind)")
    return 0

if __name__ == "__main__":
    sys.exit(main())
