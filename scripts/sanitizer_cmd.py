"""sanitizer_cmd.py — 生成可直接执行的 sanitizer 编译+运行命令（ASan/UBSan/TSan/LSan）。"""
import argparse

G = {
    "gcc": {"asan": "-fsanitize=address -fno-omit-frame-pointer -g",
            "ubsan": "-fsanitize=undefined -fno-sanitize-recover=all -g",
            "tsan": "-fsanitize=thread -pie -fPIE -g",
            "lsan": "-fsanitize=leak -g"},
    "clang": {"asan": "-fsanitize=address -fno-omit-frame-pointer -g",
              "ubsan": "-fsanitize=undefined -fno-sanitize-recover=all -g",
              "tsan": "-fsanitize=thread -fPIE -g",
              "lsan": "-fsanitize=address -fsanitize-recover=address -g"},
    "msvc": {"asan": "/fsanitize=address /Zi /Od",
             "ubsan": "/fsanitize=address /Zi  (MSVC: no UBSan; use clang-cl)",
             "tsan": "MSVC has no TSan: use clang-cl -fsanitize=thread",
             "lsan": "/fsanitize=address /Zi (ASan covers leaks on MSVC)"},
}
ENV = {"asan": "ASAN_OPTIONS=detect_leaks=1:abort_on_error=1",
       "ubsan": "UBSAN_OPTIONS=print_stacktrace=1:halt_on_error=1",
       "tsan": "TSAN_OPTIONS=halt_on_error=1:second_deadlock_stack=1",
       "lsan": "LSAN_OPTIONS=verbosity=1"}

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--kind", default="asan", choices=sorted(G["gcc"]))
    ap.add_argument("--compiler", default="g++", choices=["g++", "clang++", "cl"])
    ap.add_argument("--src", default="main.cpp")
    ap.add_argument("--std", default="17"); ap.add_argument("--run", action="store_true")
    ap.add_argument("--extra", default="")
    a = ap.parse_args()
    key = {"g++": "gcc", "clang++": "clang", "cl": "msvc"}[a.compiler]
    flags = G[key][a.kind]
    if a.compiler == "cl":
        print(f"cl /EHsc /std:c++{a.std} {flags} {a.src} /Fe:app.exe")
        print(f"REM {ENV.get(a.kind, '')}")
        if a.run: print("app.exe")
    else:
        std = f"-std=c++{a.std}" if a.std != "latest" else "-std=c++latest"
        print(f"{a.compiler} {std} -O1 -g {flags} {a.extra} {a.src} -o app")
        print(f"# env: {ENV.get(a.kind, '')}")
        if a.run: print(f"{ENV.get(a.kind, '')} ./app")
    print("# note: ASan/TSan are mutually exclusive; build separate targets")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
