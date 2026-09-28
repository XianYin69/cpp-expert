"""review_checklist.py — 按知识叶生成分级评审清单（blocking/major/minor/info）。"""
import json, os, re, sys, argparse
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TREE = os.path.join(ROOT, "asset", "knowledge_tree.json")
CHK = os.path.join(ROOT, "asset", "checklists")
BASE = [
    "blocking | 无裸 new/delete（分配器层除外并注明理由） | [cse R.11]",
    "blocking | 无返回局部对象引用/指针、无 this 逃逸进异步回调 | [cppref]",
    "blocking | 共享可变状态有同步且内存序有理由 | [std]",
    "major | 特殊成员函数成组（Rule of 0/3/5） | [cse C.66]",
    "major | 移动操作 noexcept、公共接口 const 正确 | [book]",
    "minor | 命名规范与头文件自包含（IWYU） | [google]",
]

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--leaf"); ap.add_argument("--file"); ap.add_argument("--out")
    ap.add_argument("--all", action="store_true"); a = ap.parse_args()
    leaves = [l["id"] for l in json.load(open(TREE, encoding="utf-8"))["leaves"]]
    sel = leaves if a.all else ([a.leaf] if a.leaf else [])
    if not sel:
        print("usage: --leaf <id> | --all | --file <src>", file=sys.stderr); return 2
    out = ["# C++ review checklist", "", f"scope: {a.file or 'n/a'}", ""]
    for lf in sel:
        p = os.path.join(CHK, lf + ".md")
        if not os.path.exists(p):
            continue
        out.append(f"## {lf}")
        for l in open(p, encoding="utf-8"):
            if l.strip().startswith("-"):
                out.append("- [ ] " + re.sub(r"^-\s*", "", l.strip()))
        out.append("")
    out += ["## baseline"] + ["- [ ] " + b for b in BASE]
    txt = "\n".join(out) + "\n"
    if a.out:
        os.makedirs(os.path.dirname(os.path.abspath(a.out)), exist_ok=True)
        open(a.out, "w", encoding="utf-8").write(txt); print(f"[OK] {a.out}")
    else:
        print(txt)
    return 0

if __name__ == "__main__":
    sys.exit(main())
