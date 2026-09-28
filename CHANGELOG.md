# CHANGELOG

本文件遵循 [Keep a Changelog](https://keepachangelog.com/zh-CN/1.1.0/) 与语义化版本。

## 0.1.0 - 2026-09-28

### Added
- **流程复刻**：`branch/流程/` 按 general-programming 复刻为创建路径 13 节点
  （初始化→需求确认→经验查询→大纲构建→分支分析→脚本构建→构建测试→知识库构建→
  浏览器学习→约束编写→整体审查→收尾→完成）＋修改路径 3 节点（初始化→修改流程→完成）。
- **知识库**：`references/` 十二叶知识树索引 + 9 条 C++ 权威书目；
  书目经 file_ops `ff_lite.py` 联网确证（豆瓣读书 subject 页，取证 2026-09-28），
  未确证条目（Using and Debugging C++）标 `[本地]` 且不附 URL。
- **约束**：`resistance/` 齐备——浏览器学习约束（遇不明强制派 file_ops 检索学习后再答）、
  薄技能依赖约束、git 工作流约束、审查约束、约束部分、沙盒机制、
  垃圾回收/上下文压缩/逻辑链/过程链存取/惩罚五大机制。
- **依赖声明**：`dependence/dependence.md` 薄技能只引用不内嵌
  （file_ops|skill|local:skill_manage_system、code-guidelines、pavedpath-code、ui-design、
  database-management、concurrency-design、python|software|system、git|software|system）＋用途映射表。
- **脚本**：`scripts/` 13 个 C++ 探针 + 17 个机制脚本；`template_gen.py` 模板数据外移至
  `asset/templates/*.cpp` 以满足单文件 ≤50 行红线。
- **资产**：`asset/knowledge/`（12 叶细则）＋ `asset/checklists/`（12 叶评审清单）＋
  `asset/knowledge_tree.json` 机读索引。
- **许可**：MIT `LICENSE`（技能目录、工作区根、tmp 各一份）。

### Changed
- 目录迁移：`general-programming/tmp/cpp-expert` → `skills/cpp-expert`（含 `.git` 历史，
  迁移后 `git log` HEAD 与 `git status` 校验一致）。
- `SKILL.md` 重写为 50 行内（含 YAML frontmatter、执行路径、红线）。
- `branch/流程/分支分析/分支分析.md` 参考链接改指本技能已存在的书目条目，消除悬空链接。

### Removed
- `general-programming/tmp/cpp-expert` 残留（迁移后源目录不存在）。
