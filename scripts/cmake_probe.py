"""cmake_probe.py — 探测工具链与 CMake 现状（编译器/版本/生成器/标准档/目标）。"""
import os, re, shutil, subprocess, argparse

def run(cmd):
    try:
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=25)
        return (r.stdout + r.stderr).strip().splitlines()
    except Exception as e:
        return [f"ERR {e}"]

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--dir", default="."); a = ap.parse_args()
    print("== compilers")
    for c in ("g++", "clang++", "cl", "ninja"):
        p = shutil.which(c)
        print(f"  {c}: {p or 'MISSING'}" + (f" | {run([c, '--version'])[0][:70]}" if p else ""))
    cm = shutil.which("cmake")
    print(f"  cmake: {cm or 'MISSING'}" + (f" | {run([cm, '--version'])[0][:70]}" if cm else ""))
    for pkg in ("vcpkg", "conan"):
        print(f"  {pkg}: {shutil.which(pkg) or 'MISSING'}")
    print("== project")
    cml = os.path.join(a.dir, "CMakeLists.txt")
    if not os.path.exists(cml):
        print(f"  no CMakeLists.txt in {a.dir}"); return 0
    src = open(cml, encoding="utf-8", errors="ignore").read()
    std = sorted(set(re.findall(r"CXX_STANDARD\s+(\d+)", src)))
    print(f"  CXX_STANDARD found: {std or 'unset (default 98/11 -> pin explicitly)'}")
    print(f"  targets: {len(re.findall(r'add_(?:executable|library)\s*\(\s*(\w+)', src))}")
    for flag, why in (("target_compile_features", "ok"), ("INTERFACE", "ok"),
                      ("include_directories", "prefer target_include_directories (global leakage)"),
                      ("link_libraries", "prefer target_link_libraries with PUBLIC/PRIVATE"),
                      ("GLOB", "file(GLOB) hides rebuild deps; enumerate sources"),
                      ("-Wall", "present"), ("compile_options",
                          "prefer target_compile_options per-target")):
        if flag in src and ("prefer" in why or "hides" in why):
            print(f"  WARN {flag}: {why}")
    print("  note: verify with `cmake -S . -B build --graphviz` / `cmake --preset` if present")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
