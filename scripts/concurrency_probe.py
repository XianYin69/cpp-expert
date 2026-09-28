"""concurrency_probe.py — 并发嫌疑清单：锁、原子、内存序、detach 与轮询风险。"""
import re, sys, argparse
LOCK = re.compile(
    r"\b(lock_guard|scoped_lock|unique_lock|shared_lock|shared_mutex|recursive_mutex)\b")
ATOMIC = re.compile(r"\bstd::atomic|memory_order_(relaxed|acquire|release|acq_rel|seq_cst)\b")
VOLATILE = re.compile(r"\bvolatile\b")
DETACH = re.compile(r"\.detach\s*\(")
COND = re.compile(r"condition_variable|\.wait\s*\(|notify_(one|all)")
SLEEP = re.compile(r"\b(sleep_for|sleep_until|usleep|Sleep)\s*\(")
GET = re.compile(r"\.get\s*\(\s*\)")

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("files", nargs="+"); a = ap.parse_args()
    for f in a.files:
        src = open(f, encoding="utf-8", errors="ignore").read()
        hits = []
        for i, line in enumerate(src.splitlines(), 1):
            s = line.split("//")[0]
            if VOLATILE.search(s): hits.append((i,
                "volatile is NOT synchronization -> std::atomic [std]", s))
            elif DETACH.search(s): hits.append((i, "thread::detach: lifetime/shutdown risk", s))
            elif SLEEP.search(s) and not LOCK.search(s): hits.append((i,
                "sleep-based waiting: prefer condvar/atomic wait", s))
            elif COND.search(s): hits.append((i,
                "condvar wait: must use predicate (spurious wakeup)", s))
            elif ATOMIC.search(s) and "relaxed" in s: hits.append((i,
                "memory_order_relaxed: justify ordering", s))
            elif GET.search(s) and LOCK.search(s): hits.append((i,
                "shared_ptr::get under lock: check object- vs pointer-mutex", s))
        print(f"== {f}: {len(hits)} finding(s)")
        for ln, why, txt in hits[:30]:
            print(f"  L{ln}: {why}\n      {txt.strip()[:100]}")
    print("\nnote: suspicions only; confirm with TSan (-fsanitize=thread) via sanitizer_cmd.py")
    return 0

if __name__ == "__main__":
    sys.exit(main())
