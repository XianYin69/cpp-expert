"""advice_compose.py — 组装结构化交付（结论/证据/清单/重构/风险/引用）。"""
import argparse, json, os, sys, time

SEC = ["结论摘要", "证据与复现", "评审清单", "重构建议", "风险与边界", "引用"]

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--topic", default=""); ap.add_argument("--std", default="17")
    ap.add_argument("--evidence", default="none", choices=["none", "probe", "sanitizer",
        "compiler"])
    ap.add_argument("--findings", help="JSON 数组: [{level,item,cite,cmd}]")
    ap.add_argument("--out"); a = ap.parse_args()
    items = json.loads(a.findings) if a.findings else []
    order = {"blocking": 0, "major": 1, "minor": 2, "info": 3}
    items.sort(key=lambda x: order.get(x.get("level", "info"), 9))
    out = [f"# cpp-expert 交付 · {a.topic or '未命名问题'}",
           f"- 标准档: C++{a.std}  · 取证级别: {a.evidence}  · 时间: {time.strftime('%Y-%m-%d %H:%M')}",
           "", "## 结论摘要"]
    out += [f"- [{i.get('level','info')}] {i.get('item','')}" for i in items[:8]] or ["- （无条目）"]
    out += ["", "## 证据与复现"]
    out += [f"- {i.get('cmd','')}" for i in items if i.get("cmd")] or ["- evidence=none：未实测，仅知识判断"]
    out += ["", "## 评审清单"]
    out += [
        f"- [ ] {i.get('item','')}  <!-- {i.get('cite','')} -->" for i in items] or [
            "- [ ] 运行 review_checklist.py --all"]
    out += ["", "## 重构建议", "- 顺序：正确性 → 所有权 → const/移动 → 性能；最小 diff，一次一判据。"]
    out += ["", "## 风险与边界"]
    out += ["- 未取证项须由 sanitizer/编译器复现后方可升级为 blocking。",
            "- 结论失效条件：-fno-exceptions、-fno-rtti、跨 ABI、嵌入式无堆。"]
    out += ["", "## 引用"]
    out += [
        f"- {i.get('cite','[cse]')}" for i in items if i.get(
            "cite")] or ["- [cse] C++ Core Guidelines"]
    txt = "\n".join(out) + "\n"
    if a.out:
        os.makedirs(os.path.dirname(os.path.abspath(a.out)), exist_ok=True)
        open(a.out, "w", encoding="utf-8").write(txt); print(f"[OK] {a.out}")
    else:
        print(txt)
    return 0

if __name__ == "__main__":
    sys.exit(main())
