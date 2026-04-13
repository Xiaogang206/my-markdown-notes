目前（2026年）把 **Evernote 的 .enex 文件** 转换成适合 **Obsidian** 使用的 Markdown 格式，**Yarle** 仍然是最强大、最可定制的工具之一（Obsidian 官方 Importer 插件其实底层也用了 Yarle 的部分逻辑，但独立使用 Yarle 能获得更多控制权）。

以下是目前最推荐的两种主要路径（推荐优先用第2种，能得到更好的 Obsidian 体验）：

### 方法一：最简单（适合小规模或不想折腾配置的人）

1. 在 Obsidian 里安装官方插件 **Importer**（Community plugins → 浏览 → 搜索 Importer → 安装并启用）

* 打开 Importer 插件
* 选择 **Evernote** 导入
* 选择你的 .enex 文件（可以一次选多个）
* 选择输出文件夹（建议新建一个空文件夹作为 vault 或子文件夹）
* 点 Import 运行

优点：超级简单
缺点：可定制性很低，frontmatter 和文件名规则比较固定，复杂笔记（表格、代码块、高亮、附件命名）有时处理得不够完美

### 方法二：推荐方式（使用独立 Yarle，效果最好）

**步骤概览**

1. 从 Evernote 导出 .enex（已完成）
2. 安装 Node.js（如果还没装）
3. 安装 Yarle
4. 准备配置文件（最重要一步！）
5. 运行转换
6. 把生成的文件夹作为 Obsidian vault 打开（或拖进已有 vault）

#### 详细操作（2025–2026 最新推荐做法）

**1\. 安装 Node.js**
官网下载 LTS 版：https://nodejs.org/
（Windows / macOS / Linux 都支持）

**2\. 安装 Yarle**（两种方式任选）

**方式A：全局安装（推荐）**
打开终端 / 命令提示符，执行：

    npm install -g yarle
    

**方式B：直接用 npx（不用全局安装）**
每次运行时用 `npx yarle ...`


**3\. 创建配置文件（最关键，强烈建议）**

新建一个文件叫 `yarle-config.json`，内容至少包含这些（可复制后修改）：

    {
      "enexSources": [
        "C:/你的路径/笔记本1.enex",
        "C:/你的路径/笔记本2.enex"
        // 可以放多个 .enex
      ],
      "outputFolder": "C:/Obsidian-Vaults/从Evernote转换",
      "isZettelkastenNeeded": false,
      "useZettelId": false,
      "plainTextNotesOnly": false,
      "skipWebClips": false,
      "skipEnexFileNameFromOutputPath": false,
      "useLevenshteinForLinks": false,
      "currentTemplate": "Obsidian",
      "obsidianSettings": {
        "omitLinkDisplayName": false
      },
      "keepOriginalHtml": false,
      "generateNakedUrls": true,
      "urlEncodeFileNames": false,
      "replaceSpaceWithDashInTags": false,
      "nestedTags": {
        "separatorInEN": ".",
        "replaceSeparatorWith": "/"
      },
      "keepEvernoteLinkIfNoNoteFound": true,
      "keepImageSize": true,
      "keepOriginalAmountOfNewlines": true,
      "monospaceIsCodeBlock": false,
      "keepMDCharactersOfENNotes": false,
      "trimStartingTabs": true,
      "removeEnexSourceURL": false,
      "logseqSettings": {
        "journalNotes": false
      }
    }
    

最常修改的几项：

* `enexSources` → 改成你实际的 .enex 文件路径
* `outputFolder` → 转换后 Markdown 文件存放的位置
* `currentTemplate` → 保持 "Obsidian" 即可
* `nestedTags` → 如果你的标签是 `工作.项目.子项` 这种层级风格，保持默认就好，会自动转成 `工作/项目/子项`

更多高级选项参考官方 wiki：
https://github.com/akosbalasko/yarle/wiki

**4\. 运行转换**

终端里执行：

    yarle --configFile "C:/你的路径/yarle-config.json"
    

或者用 npx：

    npx yarle --configFile "你的配置文件路径.json"
    

转换完成后，outputFolder 里会出现一堆 .md 文件 + 资源文件夹（图片、附件等）。

**5\. 打开 Obsidian**

* 新建 vault → 选择刚才的 outputFolder
* 或者把整个文件夹拖进已有 vault 的某个子目录

**小技巧 / 常见优化**

* 想让文件名 = 笔记标题：保持默认即可（Yarle 默认就是这样）
* 想把创建/更新日期写入 frontmatter：用模板自定义
* 标签带层级：上面 nestedTags 配置已支持
* 附件/图片不显示？确认资源文件和 md 文件在同一层目录结构
* 中文文件名乱码？试试把 `urlEncodeFileNames` 设为 `true`

如果你的笔记量非常大（上万篇），建议先拿 1–2 个小笔记本的 .enex 测试配置，调好后再全量跑。

有任何具体报错或需求（比如想自定义 frontmatter 格式），可以贴出来，我再帮你调整配置。祝迁移顺利～



Created at: 2026-02-08
Last updated at: 2026-02-08

 notebook:工具箱


---
./工具箱/其他/enex转换Markdown.md ---这是以上内容的文件名

---
