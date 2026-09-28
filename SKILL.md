---
name: cpp-expert
description: >
  现代 C++（C++11/14/17/20/23）专家顾问：RAII 与所有权建模、Rule of 0/3/5、const 与移动语义、
  模板与概念、STL 容器与算法选型、并发与内存模型、异常安全、编译防火墙、CMake/包管理、
  静态分析与 sanitizer、性能与缓存局部性、UB 与可移植性的可执行判断与评审清单；
  薄技能（能力经 dependence/ 声明），遇不明处强制派发 file_ops 联网学习并沉淀知识链。
license: MIT
metadata:
  category: development
---
# cpp-expert
> 使用 `cpp-expert` skill 来完成用户请求。

## 工作原则
1. **先取证后判断**：结论只来自标准条文、工具实测输出或用户原文；未运行的不得写「已验证」。
2. **判据非偏好**：blocking 须引权威依据或可复现 UB；风格偏好只作 advisory。
3. **按流程执行**：不跳步、不静默越权；决策节点留逻辑链；审查节点跑正反双链（logic_chain.py debate）。
4. **返回机制**：审查失败记中断（process_chain.py interrupt），修复后 resume；任一路径完成＝收口返回调度方整合续排。
5. **惩罚熔断**：重试达 10 次即熔断，强制回退或求助用户。
6. **垃圾回收**：tmp 收尾后释放到目标 skill 并删除；未指定目录时固定路径沙盒作业。
7. **薄技能**：本体不内嵌他技能内容，能力经 [dependence/](dependence/dependence.md) 声明；UI/数据库/并发架构专项转派。

## 执行路径
**创建路径**：初始化→需求确认→经验查询→大纲构建→分支分析→脚本构建→构建测试→知识库构建→浏览器学习→约束编写→整体审查→收尾→**完成**
**修改路径**：初始化→修改流程→**完成**
> 浏览器学习为横切节点：任一步遇到不明白即触发，取证沉淀后回原节点。

## 可用工具（scripts/）
探针：classify_topic · knowledge_index · review_checklist · ownership_audit · const_audit · concurrency_probe ·
ub_scan · cmake_probe · sanitizer_cmd · tidy_config_gen · perf_advice · template_gen · advice_compose；
机制：check_links · browser_learn · knowledge_fetch · knowledge_convert · deps_check · run_tests · lint_check ·
logic_chain · process_chain · garbage_collect · context_compress · penalty · sandbox · self_update

## 知识树（十二叶·不可再拓扑）
raii-ownership · special-members · const-move · templates-concepts · stl-algorithms · concurrency-memory-model ·
exception-safety · headers-modules · build-systems · tooling-static-analysis · performance-cache · ub-portability；
索引 [references/知识树/](references/知识树/知识树.md) · 机读 [asset/knowledge_tree.json](asset/knowledge_tree.json)

## 红线
- 无编译器、无实测不得断言「更快」「无数据竞争」，须给可复现取证命令。
- 不得把 C 风格习惯（裸 new/delete、宏、C 数组、typedef 别名所有权）当默认推荐。
- 不得以 `volatile` 代 `std::atomic`、以 sleep 代同步、以 `shared_ptr` 当默认所有权。
- 遇不明必派 file_ops 联网学习（[浏览器学习约束](resistance/浏览器学习约束/浏览器学习约束.md)），禁凭记忆臆造 API/签名；未确证条目标 `[本地]`，严禁臆造 URL。
- 悬空链接必须为 0；所有 .md 与脚本 ≤50 行；缓存文件不得写入 skill 目录。
- 只维护本技能目录，不得改动 concurrency-design、general-programming 等既有技能。
- Git 工作流：每步功能分支提交→审核通过合 `dev`→整体审查通过 `dev` 合 `main`（推送前须用户确认）。

## 详细流程
- 流程节点：[branch/流程/](branch/流程/流程.md)；约束兜底：[resistance/](resistance/resistance.md)
