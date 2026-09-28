"""template_gen.py — 输出可编译的现代 C++ 模板骨架（数据在 asset/templates/<kind>.cpp）。"""
import argparse, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
TD = os.path.join(ROOT, "asset", "templates")
KINDS = sorted(os.path.splitext(f)[0] for f in os.listdir(TD) if f.endswith(".cpp"))
VERIFY = "// verify: g++ -std=c++20 -fsyntax-only -Wall -Wextra -Werror <file>"


def render(kind):
    p = os.path.join(TD, kind + ".cpp")
    if not os.path.isfile(p):
        raise SystemExit("[ERR] 模板缺失: %s（可选 %s）" % (p, ", ".join(KINDS)))
    return "// cpp-expert template: %s\n%s\n%s\n" % (kind, VERIFY, open(p,
        encoding="utf-8").read().rstrip())


def main():
    ap = argparse.ArgumentParser(description="emit modern C++ skeleton from asset/templates")
    ap.add_argument("--kind", required=True, choices=KINDS)
    ap.add_argument("--out", help="write to file (default stdout, no silent write)")
    a = ap.parse_args()
    body = render(a.kind)
    if a.out:
        open(a.out, "w", encoding="utf-8").write(body)
        print("[OK] " + a.out)
    else:
        print(body)
    return 0


if __name__ == "__main__":
    sys.exit(main())
