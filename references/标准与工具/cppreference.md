# cppreference（标准库与语言参考）

- 已确证入口（[联网] 检索 2026-09-28）：
  - 中文站 https://zh.cppreference.com/%E9%A6%96%E9%A1%B5
  - 中文镜像 https://cppreference.cn/w/ 与 https://cppreference.cn/w/cpp/language
  - 英文站 https://en.cppreference.com/ （检索命中；本环境直取常 WinError 10060，优先中文镜像）
- 映射知识叶：全部十二叶（签名/复杂度/保证级别的规范表述层）

## 用法与边界

1. 函数签名、模板参数、复杂度保证、`noexcept` 规格、缺陷报告（DR）状态以此为准。
2. 它是**标准条文的转述**，不是 ISO 文档本身；争议结论回指 [isocpp](isocpp.md)。
3. 抓取须走 `scripts/browser_learn.py`，摘要+URL+抓取时间落本目录，禁存整页正文。
4. 禁止凭记忆写签名：未取证的签名一律标 [本地] 并降级为「待确证」。

## 相关

- [references](../references.md) · [浏览器学习约束](../../resistance/浏览器学习约束/浏览器学习约束.md)
