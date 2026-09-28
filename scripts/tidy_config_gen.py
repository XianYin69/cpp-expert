"""tidy_config_gen.py - generate .clang-tidy / cppcheck config and runnable check commands."""
import argparse, os, shutil

CHECKS = {
    "strict": ["modernize-*", "performance-*", "readability-*", "bugprone-*", "cppcoreguidelines-*",
               "concurrency-*", "misc-*", "-modernize-use-trailing-return-type",
               "-readability-magic-numbers", "-cppcoreguidelines-avoid-magic-numbers"],
    "balanced": ["bugprone-*", "performance-*", "modernize-use-*",
        "cppcoreguidelines-owning-memory",
                 "cppcoreguidelines-pro-type-*", "concurrency-*",
                     "-modernize-use-trailing-return-type"],
    "min": ["bugprone-*", "cppcoreguidelines-owning-memory", "concurrency-*"],
}
TOOLS = ["clang-tidy", "clang-format", "cppcheck", "include-what-you-use", "clang-query"]

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--level", default="balanced", choices=sorted(CHECKS))
    ap.add_argument("--std", default="17"); ap.add_argument("--out")
    ap.add_argument("--check", action="store_true"); a = ap.parse_args()
    if a.check:
        for t in TOOLS:
            print(f"  {t}: {'found' if shutil.which(t) else 'MISSING'}")
        return 0
    body = ("---\nName: cpp-expert\nUseColor: true\n"
            + f"Checks: '{', '.join(CHECKS[a.level])}'\n"
            + "CheckOptions:\n  - key: ModernizeUseAutoForSimpleTypes\n    value: 'true'\n"
            + "HeaderFilterRegex: '.*'\nCompileCommands: build/compile_commands.json\n")
    if a.out:
        open(a.out, "w", encoding="utf-8").write(body); print(f"[OK] {a.out}")
    else:
        print(body)
    print("# run: clang-tidy -p build <files>")
    print(f"# cppcheck: cppcheck --enable=warning,performance,portability --std=c++{a.std} "
          "--inconclusive --suppress=missingIncludeSystem src/")
    print("# iwyu: include-what-you-use -Xiwyu --mapping_file=iwyu.imp <file>")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
