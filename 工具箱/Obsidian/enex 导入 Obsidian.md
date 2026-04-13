**不可以直接双击或拖入 .enex 文件就导入 Obsidian**，Obsidian 本身没有原生内置的 ENEX 导入功能（不像一些 app 那样能直接打开 .enex）。

但通过官方的免费插件 **Importer**，可以非常方便地导入 .enex 文件（这是目前最推荐、最官方的方式）。

### 官方推荐步骤（2025-2026 年最新方式）

1. **先从 Evernote 导出 .enex 文件****（用brew下的**evernote-backup功能）

在 Evernote 桌面客户端（Windows/Mac）中，选择笔记本 → 导出 → 格式选 **ENEX**（.enex）。

可以一次导出一个笔记本，也可以全选所有笔记导出（大 vault 建议分批，避免单个文件太大）。

2. **在 Obsidian 安装 Importer 插件**

打开 Obsidian → 设置（齿轮图标）

→ 社区插件 → 关闭安全模式（如果还没开）

→ 浏览 → 搜索 “Importer” → 安装并启用（开发者是 Obsidian 官方团队）。

3. **使用 Importer 导入** **（会导致丢失笔记本组，如果用Yarle就可以保留）**

按 Cmd + P 打开命令面板，输入 “Importer” 。

选择 **File format** → **Evernote (.enex)**

选择你的 .enex 文件位置

可以设置输出文件夹（默认会建一个 Evernote 文件夹）

点击 Import，等待完成（笔记会转为 Markdown 文件，带标题、创建/修改日期、标签、附件等）。


导入后：

笔记变成纯 Markdown 文件（.md）

标签会转为 YAML frontmatter 或文件夹/标签形式

附件（如图片）通常会提取到附件文件夹，并用 !\[\[图片名\]\] 链接

支持批量，但如果 .enex 非常大（几万笔记），建议分多个 .enex 文件导入，避免卡顿或内存问题。


### 注意事项 & 常见小问题

**iPhone/iPad 上也能导入**：Importer 插件在移动端也支持，但建议用电脑先导入（文件选择更方便，处理大文件更快）。

**格式保留程度**：基本文本、列表、代码块、图片都能很好保留；复杂表格、手写笔记、音频附件可能有丢失或需手动调整。

**如果 Importer 不顺利**：可以用第三方工具先转一次，比如 Yarle（https://github.com/akosbalasko/yarle），它保留更多元数据（创建日期、地理位置等），然后把生成的 Markdown 文件夹拖进 Obsidian vault。

**测试建议**：先导出一个小笔记本的 .enex 测试一下，看效果是否满意。


官方文档（最准）：

https://help.obsidian.md/import/evernote

如果你已经导出好 .enex 文件了，或者导入时遇到具体报错，告诉我细节，我可以帮你排查～


Created at: 2026-02-08
Last updated at: 2026-02-09

 notebook:工具箱


---
./工具箱/Obsidian/enex 导入 Obsidian.md ---这是以上内容的文件名

---
