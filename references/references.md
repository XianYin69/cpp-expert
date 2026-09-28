# references（知识库索引）

本目录只存**摘要与出处**，不存受版权保护的正文。来源标注两类：

- `[联网]`＝经 file_ops 的 ff_lite 检索/取页确证（取证时间 2026-09-28，豆瓣读书 book.douban.com 与官网）。
- `[本地]`＝模型既有常识，**未经联网确证**，禁止当作已验证事实引用，禁止附 URL。

## C++ 权威书目（与知识树十二叶映射）

| 领域 | 条目 | 来源 |
|---|---|---|
| 语言基础 | [cpp-primer](语言基础/cpp-primer.md) · [cpp-programming-language](语言基础/cpp-programming-language.md) · [principles-and-practice](语言基础/principles-and-practice.md) | [联网] |
| 工程实践 | [effective-modern-cpp](工程实践/effective-modern-cpp.md) · [clean-code](工程实践/clean-code.md) | [联网] |
| 并发 | [cpp-concurrency-in-action](并发/cpp-concurrency-in-action.md) | [联网] |
| 底层模型 | [stl-source-code](底层模型/stl-source-code.md) · [inside-the-cpp-object-model](底层模型/inside-the-cpp-object-model.md) | [联网] |
| 调试取证 | [cpp-debugging](调试取证/cpp-debugging.md) | [联网] |
| 调试取证 | [using-and-debugging-cpp](调试取证/using-and-debugging-cpp.md) | [本地]（豆瓣无同名条目，故不附 URL） |
| 标准与工具 | [cppreference](标准与工具/cppreference.md) · [isocpp](标准与工具/isocpp.md) · [cmake](标准与工具/cmake.md) | [联网] |

## 知识树（十二叶）

- [知识树索引](知识树/知识树.md)：叶 → `asset/knowledge/`（细则）＋ `asset/checklists/`（评审清单）

## 专项能力索引（外置薄技能·只引用不内嵌）

并发设计 → concurrency-design；编码规范 → code-guidelines；已验证范式 → pavedpath-code；
UI → ui-design；数据库 → database-management；文件与联网取证 → file_ops。
声明见 [dependence/](../dependence/dependence.md)。

## 取证方法（本环境可达性）

`python -B scripts/browser_learn.py --query "<书名> 豆瓣读书" --out tmp/learn`
境外源（en.cppreference.com / wikipedia）在本环境 WinError 10060 不可达；
优先 book.douban.com、zh.cppreference.com、cppreference.cn、cmake.com.cn、isocpp.org。
≥4 词英文书名会被 Bing 切成词典页，改用中文书名或 `site:book.douban.com <词>`。

## 相关

- [resistance](../resistance/resistance.md) · [知识库构建](../branch/流程/知识库构建/知识库构建.md)
- [浏览器学习约束](../resistance/浏览器学习约束/浏览器学习约束.md)
