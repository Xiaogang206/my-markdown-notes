在 Obsidian 的 **Minimal** 主题下，文件的路径（folder path / breadcrumb）显示方式主要取决于几个设置和 Obsidian 版本（当前 2026 年 2 月，大多是 1.10+ 到 1.11+）：

### 1. **最常见的位置：Tab 标题栏（标签页顶部）**
Minimal 主题默认 **只在鼠标悬停（hover）** 时显示完整路径（文件夹 + 文件名），平时只显示文件名。这是 Minimal 的设计选择（为了保持简洁）。

**想让路径一直显示（不需悬停）**：
1. 安装社区插件 **Style Settings**（设置 → 社区插件 → 浏览 → 搜索 "Style Settings" → 安装启用）
2. 确保已启用 Minimal 主题（设置 → 外观 → 主题）
3. 进入 **设置 → Style Settings**
4. 向下滚动找到 **Minimal** 部分（通常在很下面）
5. 展开：**Minimal → Titles → Tab title bar**
6. 找到选项 **Tab title visibility**（标签标题可见性）
   - 默认是 **Hover only**（仅悬停）
   - 改成 **Visible**（始终可见）

改完后，**每个标签页顶部**就会一直显示类似这样的路径：

```
FolderA / Subfolder / 文件名.md
```

（路径是相对 vault 根目录的）

**前提**：确保核心设置里 **Appearance → Show tab title bar** 是开启的（默认是开）。

### 2. **笔记内部的路径显示（Header 区域 / breadcrumb）**
- Minimal 主题本身不强制在笔记正文顶部（inline title 下方）一直显示路径。
- Obsidian 核心从 1.11 开始调整了行为：
  - 如果你开了 **Inline title**（内联标题，设置 → 编辑器 → Inline title），路径通常**不显示**或只在 hover 时出现。
  - 如果**关闭 Inline title**，文件名会移到 tab 标题栏，路径有时会跟着显示（但 Minimal 可能仍隐藏）。

想在笔记顶部强制显示路径的话，常见方案：
- 用插件：**Show Current File Path**（在状态栏显示完整路径，可点击复制）
- 或 **Tab File Path**（直接把路径塞进 tab 里）
- 或自己写很短的 CSS snippet（.view-header-breadcrumb { display: block !important; } 等，具体类名可右键检查元素）

### 3. **其他快速查看路径的方式（不改主题）**
- 命令面板（Ctrl/Cmd + P）输入：**File explorer: Reveal active file in navigation** → 文件在左侧文件树自动展开定位
- 右键标签页标题 → **Copy file path**（复制路径）
- 状态栏插件（如上面提到的 Show Current File Path）

### 小结（Minimal 主题下路径显示速查）

| 显示位置          | 默认行为              | 如何改成一直显示                          | 需要插件          |
|-------------------|-----------------------|-------------------------------------------|-------------------|
| Tab 标题栏        | 悬停才显示完整路径    | Style Settings → Minimal → Titles → Tab title bar → Tab title visibility = Visible | Style Settings（必装） |
| 笔记顶部 Header   | 通常不显示或 hover    | 关闭 Inline title + CSS snippet 或插件    | 可选              |
| 状态栏            | 不显示                | 安装 Show Current File Path 插件          | Show Current File Path |
| 文件树定位        | 无                    | 命令：Reveal active file                  | 无                |

大多数 Minimal 用户最终都装了 Style Settings，然后把 Tab title visibility 改成 Visible，这样最直观。

如果改了还是看不到路径，或者你用的是移动端（iOS/Android），可以告诉我更多细节（比如 Obsidian 版本、是否开了 inline title、桌面还是手机），我再帮你细调。