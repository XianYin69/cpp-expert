# build-systems — 构建系统与包管理

## 判据要点

- CMake 现代写法：**target 为中心**，`target_compile_features(target PUBLIC cxx_std_20)`
  或 `set_target_properties(CXX_STANDARD 20 CXX_STANDARD_REQUIRED ON CXX_EXTENSIONS OFF)`；
  避免全局 `include_directories` / `link_libraries` / 裸 `add_definitions`。
- 可见性三态必须显式：`PUBLIC`（要求者也要传递）/ `PRIVATE`（实现细节）/ `INTERFACE`（头文件库）。
  搞错方向 = 隐藏依赖或过度暴露。
- 头文件库：`add_library(hdr INTERFACE)` + `target_include_directories(hdr INTERFACE
  $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}> $<INSTALL_INTERFACE:include>)`。
- `file(GLOB)` / `GLOB_RECURSE` 默认禁用：新增文件不触发重新配置，产生陈旧构建；
  确需则 `CONFIGURE_DEPENDS` 并说明代价。
- 依赖获取优先级：`find_package`（系统/已安装）→ `FetchContent`（固定 tag + `GIT_SHALLOW`）→
  vcpkg manifest（`vcpkg.json` + toolchain file）→ Conan 2（`conanfile.py` + lockfile）。
  禁止「手动 clone 到第三方目录再 include」的不受控形态。
- 可复现性：锁定依赖版本（vcpkg baseline / conan lock / `FETCHCONTENT_QUIET` + 显式 tag），
  编译器与标准档写进 `CMakePresets.json`，不靠开发者记忆。
- ABI 风险：跨 DLL/SO 边界传 C++ 类型（`std::string`/容器/异常）在不同编译器或不同
  `_GLIBCXX_USE_CXX11_ABI`/运行时（/MD vs /MT）下是未定义；边界用 C ABI 或明确同工具链约束。
- 导出与安装：`install(TARGETS ... EXPORT)` + `install(EXPORT ... NAMESPACE pkg::)` +
  `CMakePackageConfigHelpers`，让下游能 `find_package(pkg CONFIG)`。
- 并行与缓存：Ninja + `compile_commands.json`（供 clang-tidy）+ ccache/sccache；
  开启 `CMAKE_EXPORT_COMPILE_COMMANDS=ON` 是静态分析前置条件。
- 警告即质量闸门：`-Wall -Wextra -Wpedantic -Werror`（或 MSVC `/W4 /permissive- /Zc:__cplusplus`），
  第三方目标用 `SYSTEM` include 或 `NO_SYSTEM_FROM_IMPORTED` 控制范围。

## 取证

`cmake_probe.py --dir <proj>` 探测工具链/标准档/目标数与反模式；
`cmake -S . -B build -G Ninja` 实跑一次才算验证。
