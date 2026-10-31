# 第0周 环境配置与基线报告

## 1. 基础环境版本
- 操作系统：Windows 10 (64位)
- Python 版本：Python 3.12.4
- Git 版本：2.56.0
- 代码编辑器/工具：VS Code, Zotero

## 2. 大模型 API 配置
- 使用平台：Kimi 开放平台
- 模型名称：kimi-k3.1-pro
- 测试结果：成功调用 API，返回了结构化的 JSON 格式漏洞分析数据，并记录了 Token 消耗与耗时。

## 3. 遇到的报错与解决方案
- **报错1：Python 环境缺失**。解决：从官网下载安装 Python 3.12.4，并在安装时勾选 "Add python.exe to PATH"。
- **报错2：Git 提示 dubious ownership**。解决：因为项目从 C 盘迁移至 D 盘，需执行 `git config --global --add safe.directory D:/Research` 添加信任。
- **报错3：Git 推送超时**。解决：通过开启网络代理并配置浏览器 OAuth 授权成功解决。

## 4. InjecAgent 仓库基线复现记录
- **克隆与依赖安装**：成功克隆官方仓库，并使用国内镜像源（清华源）成功安装了包括 `torch`、`transformers` 在内的所有 requirements.txt 依赖。
- **运行测试**：尝试运行 `python main.py --help` 报错 `No such file or directory`；尝试运行 `python -m injecagent --help` 报错 `No module named injecagent`。
- **原因分析**：经使用 `ls` 命令排查，发现源码位于 `src` 目录下。推测该项目需要通过 `pip install -e .` 进行本地可编辑安装，或者在 `src` 目录下运行，才能正确识别模块。
- **后续计划**：将在下一阶段仔细阅读官方 README，配置正确的环境变量或运行入口。