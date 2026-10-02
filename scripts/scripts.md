# scripts（脚本库）

本目录存放可执行辅助脚本：校验、生成、检索、机制兜底。工具本身不限行数（50 行红线只约束 markdown），
文件名英文、小写、下划线分隔。

## 当前内容

- [`check_links.py`](check_links.py)：悬空链接校验（红线：悬空 = 0）。
- [`lint_check.py`](lint_check.py)：体量与坏味道自查（.md ≤50 行；脚本不计行数，查裸 except、print 残留、长行）。
- [`logic_chain.py`](logic_chain.py)：逻辑链 add/verify/debate（正反双链）。
- [`process_chain.py`](process_chain.py)：过程链 save/load/interrupt/resume。
- [`penalty.py`](penalty.py)：惩罚计数，达 10 次熔断。
- [`garbage_collect.py`](garbage_collect.py)：tmp 过期产物回收（默认预览）。
- [`context_compress.py`](context_compress.py)：按关键词压缩上下文。
- [`sandbox.py`](sandbox.py)：固定路径沙盒 create/list/deliver/clean。
- [`deps_check.py`](deps_check.py)：dependence/ 声明项可达性自检。
- [`browser_learn.py`](browser_learn.py)：派 file_ops 联网取证（须 :grant network）。
- [`knowledge_fetch.py`](knowledge_fetch.py)：白名单文献抓取（落 tmp）。
- [`knowledge_convert.py`](knowledge_convert.py)：HTML→md 摘要与出处。
- [`scaffold_project.py`](scaffold_project.py)：src/tests 工程脚手架。
- [`run_tests.py`](run_tests.py)：构建与测试执行 + 报告。
- [`flowchart_helper.py`](flowchart_helper.py)：需求模糊时出流程草稿。
- [`self_update.py`](self_update.py)：report/compare 版本比对。

## 运行约定

1. 用项目默认 Python：`python -B scripts/<name>.py`。
2. 任何写盘脚本默认预览，落盘须显式 `--yes`。
3. 运行前先读 [resistance](../resistance/resistance.md) 确认权限与回滚策略。
4. 缓存与临时产物一律落 tmp 或用户缓存目录，禁止写入 skill 目录。

## C++ 探针（本技能专有）
- [`classify_topic.py`](classify_topic.py)：问题/源码 → 十二叶映射（关键词加权）。
- [`knowledge_index.py`](knowledge_index.py)：取叶要点与权威出处锚点。
- [`review_checklist.py`](review_checklist.py)：按叶输出评审清单。
- [`ownership_audit.py`](ownership_audit.py)：裸 new/delete、拥有型裸指针。
- [`const_audit.py`](const_audit.py)：const 正确性与移动语义缺口。
- [`concurrency_probe.py`](concurrency_probe.py)：锁/原子/内存序/detach 嫌疑。
- [`ub_scan.py`](ub_scan.py)：UB 与可移植性静态特征。
- [`cmake_probe.py`](cmake_probe.py)：工具链与 CMake 现状探测。
- [`sanitizer_cmd.py`](sanitizer_cmd.py)：ASan/LSan/TSan/UBSan 命令生成。
- [`tidy_config_gen.py`](tidy_config_gen.py)：clang-tidy 配置生成。
- [`perf_advice.py`](perf_advice.py)：容器/拷贝/遍历/分配启发式。
- [`template_gen.py`](template_gen.py)：骨架输出（数据在 asset/templates/）。
- [`advice_compose.py`](advice_compose.py)：结构化交付组装（结论/证据/清单/风险/引用）。
