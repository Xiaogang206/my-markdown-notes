在 Obsidian 中使用 **Epub Importer** 插件导入一本 EPUB 书籍是最直接的方式之一。这个插件会把 EPUB 转换成一个文件夹，里面按章节拆分成多个 Markdown 文件（.md），方便你在 Obsidian 里阅读、标注、高亮、做双向链接和知识管理。

插件作者：aoout  
GitHub：https://github.com/aoout/obsidian-epub-importer  
（目前仍在维护，2025–2026 年仍有更新）

### 步骤详解（2026 年最新流程）

1. **安装插件**  
   - 打开 Obsidian → 点击左下角齿轮（设置）  
   - 进入「Community plugins」→ 如果「Restricted mode」是开启的，先点「Turn off restricted mode」  
   - 点击「Browse」  
   - 在搜索框输入 **Epub Importer**（或直接搜 "epub"）  
   - 找到 "Epub Importer"（作者 aoout）→ Install → Enable  

2. **两种导入方式，任选一种**（插件支持两种，第二种更方便批量）

   **方式 A：单本导入（最简单，推荐新手先试这个）**  
   - 按 `Ctrl/Cmd + P` 打开命令面板（Command Palette）  
   - 输入并选择：**Epub Importer: Import epub to your vault**  
   - 插件会弹出一个输入框，要求你粘贴 **EPUB 文件的绝对路径**  
     示例（Windows）：  
     `C:\Users\你的用户名\Downloads\我的书.epub`  
     示例（Mac）：  
     `/Users/你的用户名/Downloads/我的书.epub`  
     示例（Linux）：  
     `/home/你的用户名/书籍/我的书.epub`  
   - 回车 → 插件开始转换  
   - 转换完成后，会在你的 vault 根目录（或你设置的路径）自动创建一个文件夹，通常以书名命名，里面是：  
     - 00-元数据.md（书名、作者、出版社、简介等）  
     - 01-章节1.md  
     - 02-章节2.md  
     ……  
     - 图片会提取到子文件夹（如 assets/ 或 media/）

   **方式 B：配置图书馆路径（适合多本书、长期使用）**  
   - 进入设置 → Community plugins → Epub Importer → Options / Settings  
   - 找到 "Library paths" 或 "EPUB libraries" 这一项  
   - 添加你存放 EPUB 的文件夹路径（可以加多个）  
     示例：`D:\Books\EPUBs` 或 `/Users/你/Books`  
   - 保存设置  
   - 以后再运行 **Epub Importer: Import epub to your vault** 命令  
   - 插件会列出该路径下所有 .epub 文件供你选择（下拉菜单或列表）  
   - 选书 → 导入，过程同上

3. **导入后怎么用**  
   - 打开书对应的文件夹 → 从 00-元数据.md 开始读  
   - 想高亮/注释：直接在 md 文件里用 Obsidian 原生高亮（==文本==）或安装 **Highlightr** / **Annotator** 等插件增强  
   - 想做读书笔记：新建一个笔记，用 [[ ]] 链接到书里的章节句子  
   - 目录导航：很多用户会再装 **Dataview** 或 **Outline** 插件，自动生成全书目录  
   - 搜索整本书：Obsidian 全局搜索直接搜关键词即可

### 常见问题 & 小贴士
- **图片不显示？** → 插件通常会自动提取图片到相对路径的子文件夹，确保 vault 设置里「Attachment folder path」没冲突。  
- **章节顺序乱？** → 文件名前缀是数字的，按文件名排序即可（插件一般已处理好）。  
- **转换很慢/卡？** → 大书（>500页或很多图片）正常，耐心等；或先试一本小书测试。  
- **脚注/目录丢失？** → 插件处理得还可以，但复杂排版书可能不完美。备选方案：用 Pandoc 命令行先转一次再导入。  
- **想保留原 EPUB 阅读体验（翻页感）？** → 这个插件是“转 Markdown”派，如果你更想直接阅读 EPUB 文件而不转换，可以试 **Annotator** 插件（支持直接打开 EPUB 阅读 + 高亮，但不转成 md）。  

导入成功后，你就拥有了一本“可链接、可搜索、可联网”的电子书了，这是 Obsidian 做阅读管理最爽的地方之一。

有具体报错、系统（Win/Mac）、书类型（小说/技术书）或其他问题，随时补充，我再帮你细调！
---
./工具箱/其他/导入epub.md ---这是以上内容的文件名

---
