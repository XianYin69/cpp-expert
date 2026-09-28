# 评审清单 · tooling-static-analysis

- [ ] blocking | 声称已验证无泄漏/无竞争却无 sanitizer 命令与退出码 | [本技能红线]
- [ ] major | 未开 -Wall -Wextra -Wpedantic -Werror 基线 | [cse P.8]
- [ ] major | clang-tidy 未用 -p build（缺 compile_commands 失真） | [clang docs]
- [ ] major | ASan 与 TSan 混在同一构建（互斥） | [llvm sanitizer api]
- [ ] major | UBSan 未加 -fno-sanitize-recover=all | [llvm]
- [ ] minor | 一次性全开 strict 规则（噪音淹没真问题） | [cse P.10]
- [ ] verify | tidy_config_gen.py --check + sanitizer_cmd.py --kind asan|ubsan|tsan
