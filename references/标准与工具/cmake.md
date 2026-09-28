# CMake（构建系统）

- 已确证入口（[联网] 检索 2026-09-28）：
  - 官网 https://cmake.org/ （标题「CMake - Upgrade Your Software Build System」）
  - 中文文档镜像 https://cmake.com.cn/cmake/help/latest/index.html （CMake 4.4.0 参考文档）
- 映射知识叶：build-systems · headers-modules · tooling-static-analysis

## 用法与边界

1. 目标（target）为中心的写法：`target_include_directories`/`target_link_libraries` 的
   作用域关键字与传播语义，以官方文档措辞为准，不凭记忆写参数。
2. 版本相关：`cmake --version` 先确认可用特性（如 `PREVIEW` 变量、`FetchContent` 行为）。
3. 取证脚本：`python -B scripts/cmake_probe.py`（探测生成器与编译器）；
   参数不确定时走 [浏览器学习](../../branch/流程/浏览器学习/浏览器学习.md)。

## 相关

- [build-systems](../../asset/knowledge/build-systems.md) · [references](../references.md)
