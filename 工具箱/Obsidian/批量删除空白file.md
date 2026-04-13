<center></center># 结论：
用**File Cleaner Redux** 最简单，每次只需要执行命令即可
# <font color="#c00000">File Cleaner Redux: Clean files</font>
其他方法未测试。

---
在 Obsidian 中批量删除**新建的空白笔记**（通常指 0 字节或内容完全为空/只有空白字符的 .md 文件），目前（2026 年）最实用、最安全的几种方法如下，按推荐顺序排列：

| 优先级 | 方法                              | 需要插件 | 操作难度 | 安全性    | 适用场景说明                          |
| --- | ---------- | ---- | ---- | ------ | ---------- |
| 1   | **File Cleaner Redux** 插件（最推荐）  | 是    | 低    | 高（有预览） | 专门清理空文件 + 未使用附件，支持预览、排除文件夹、自动运行 |
| 2   | **Janitor** 插件（经典老方案）           | 是    | 低    | 中等     | 启动时/手动一键删 0 字节文件，很多人用了很多年       |
| 3   | 系统文件管理器排序删除                     | 否    | 中    | 高（可恢复） | 适合少量或想手动确认                      |
| 4   | 社区脚本 / Templater / QuickAdd 自定义 | 是    | 高    | 需小心    | 想完全自定义规则（例如只删 Untitled 开头 + 空）  |
| 5   | 搜索 + 手动多选删除                     | 否    | 中    | 高      | 数量不多时凑合用                        |

### 最推荐做法（2026 年主流方案）

#### 方法 1：安装 File Cleaner Redux 插件（强烈推荐）

1. 社区插件搜索 → 安装启用 **File Cleaner Redux**（或直接搜 "file cleaner"，redux 是更新维护版）
2. 进入插件设置：
   - 勾选 “Process empty Markdown files” 或类似选项（处理 0 字节 md 文件）
   - 可选：勾选 “Process files with only whitespace” （只含空格/换行的也算空）
   - 设置删除方式：推荐 “Move to Obsidian trash” 或 “Move to system trash”
   - 可设置排除某些文件夹（如 templates、attachments 等）
   - 开启 “Preview before delete” （超级重要，先预览！）
3. 命令面板（Ctrl/Cmd+P）搜索：
   - “File Cleaner: Scan and clean” 或 “Clean vault”
4. 预览列表 → 确认无误 → 执行删除

→ 一次可清几百上千个空文件，非常干净。

#### 方法 2：用 Janitor 插件（如果已经装了或喜欢极简）

1. 安装 **Janitor**
2. 设置里只开启：
   - Process empty files
   - Run at startup（可选，每次启动自动清）
   - Ask for confirmation → 关掉（或开着看情况）
3. 重启 Obsidian → 它会自动扫描并删除 0 字节文件

很多人反馈用了这个后“瞬间清掉几百个 Untitled 垃圾文件”。

#### 方法 3：不装插件，手动批量删（最安全但稍慢）

1. 打开你电脑的文件管理器（Windows 资源管理器 / macOS Finder）
2. 进入 Obsidian 仓库（vault）文件夹
3. 在搜索框输入：`大小：0 KB` 或 `size:0`（不同系统叫法略不同）
   - Windows：右上角搜索 → 大小 → 空（0 字节）
   - macOS：右上角搜索 → 文件大小 → 其他 → 文件大小 = 0 字节
4. 筛选出 .md 文件 → 全选 → 删除（或移到回收站）

→ 因为 Obsidian 的笔记就是普通 md 文件，删了就没了，但系统回收站可以救回。

#### 小提醒与注意事项

- **先备份**：任何批量删除前，强烈建议把 vault 整个复制一份到别处。
- **0 字节 vs 只含空格/换行**：有些“看起来空”的文件其实有隐藏的空格或换行符，只有少数插件（如 File Cleaner Redux）能识别并清理。
- **Untitled 开头的自动删**：目前核心没有这个功能，但 File Cleaner Redux 的新版本支持按文件名模式删（可设置规则删 “Untitled*” 且内容为空的）。
- 如果你经常新建空白笔记却不写，建议：
  - 改用 `Ctrl/Cmd + O` + 直接输入标题回车（避免产生 Untitled）
  - 或用 QuickAdd 插件做“智能新建”代替 Ctrl+N

你现在空白笔记大概有多少个？集中在某个文件夹吗？还是全库散布？告诉我具体情况，我可以给你更精确的操作路径～
---
./工具箱/Obsidian/批量删除空白file.md ---这是以上内容的文件名

---
