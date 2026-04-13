在 Chrome 浏览器中直接渲染（预览）本地或远程的 **.md** Markdown 文件，目前（2026年）最常用、最方便的方式是安装 Chrome 扩展程序。原生 Chrome 仍然不会自动渲染 Markdown 文件（只会显示纯文本）。

以下是目前主流且好用的几种方案，按推荐顺序排列：

### 1. 最推荐（2025–2026年主流选择）—— Markdown Viewer / Markdown Reader 系列

这些扩展功能最全、更新活跃、支持本地文件渲染。

| 扩展名称            | 主要特点             | GitHub风格 | 自动刷新 | Mermaid图表 | Math公式 | 主题数量 | 推荐指数  |
| --------------- | ---------------- | -------- | ---- | --------- | ------ | ---- | ----- |
| Markdown Viewer | 功能最全面、安全、支持本地+远程 | 是        | 是    | 是         | 是      | 30+  | ★★★★★ |
| Markdown Reader | 速度快、界面极简、支持多种协议  | 是        | 是    | 是         | 是      | 多    | ★★★★☆ |
| MarkView (新兴)   | 2026年新星，现代界面、性能好 | 是        | 是    | 是         | 是      | 多    | ★★★★☆ |

**安装和使用步骤（以 Markdown Viewer 为例）**：

1. 打开 Chrome 网上应用店，搜索：**Markdown Viewer**  
   常用链接（可直接复制到地址栏）：
   - https://chromewebstore.google.com/detail/markdown-viewer/ckkdlimhmcjmikdlpkmbgfkaikojcbjk

2. 点击「添加至 Chrome」→ 安装完成

3. **重要**：安装后要手动开启对本地文件的访问权限（2021年后Chrome安全策略要求）
   - 右上角扩展图标 → 右键「Markdown Viewer」→「管理扩展程序」
   - 打开「允许访问文件网址」开关

4. 使用方式：
   - 直接在 Chrome 地址栏输入本地文件路径，例如：
     ```
     file:///D:/笔记/project.md
     ```
     或拖拽 .md 文件到 Chrome 窗口
   - 插件会自动渲染成美观的排版（标题、代码高亮、表格、列表等）

### 2. 经典但仍活跃的选择（适合需要 LaTeX 公式很重的用户）

- **Markdown Preview Plus**（老牌，但部分用户反馈2025年后更新变少）
- 商店搜索：Markdown Preview Plus
- 优点：支持每秒自动刷新 + 强 LaTeX 渲染
- 缺点：界面稍老

### 3. 极简零安装方案（不想装扩展时用）

把下面这个单文件 HTML 保存为 `md-reader.html`，以后遇到 .md 文件就拖到这个页面里即可渲染（支持拖拽）：

```html
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <title>极简 Markdown 阅读器</title>
  <script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/highlight.js@11.9.0/lib/highlight.min.js"></script>
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/github-markdown-css@5.5.0/github-markdown.min.css">
  <style>
    body { margin: 0; padding: 40px; font-family: -apple-system, BlinkMacOSystemFont, "Segoe UI", Helvetica, Arial, sans-serif; }
    .markdown-body { max-width: 900px; margin: auto; }
  </style>
</head>
<body class="markdown-body">
  <div id="content"></div>

  <script>
    const content = document.getElementById('content');
    const render = () => {
      const file = document.querySelector('input[type=file]');
      if (file && file.files[0]) {
        const reader = new FileReader();
        reader.onload = e => {
          content.innerHTML = marked.parse(e.target.result);
          hljs.highlightAll();
        };
        reader.readAsText(file.files[0]);
      }
    };
  </script>

  <input type="file" accept=".md,.markdown" onchange="render()">
  <p style="text-align:center; color:#666;">把 .md 文件拖到这里 或 点击选择</p>
</body>
</html>
```

### 4. 快速对比总结（2026年2月主流选择）

| 需求                     | 推荐方案                  |
|--------------------------|---------------------------|
| 最美观、最全功能         | Markdown Viewer           |
| 极简、速度最快           | Markdown Reader           |
| 需要强 LaTeX + 自动刷新  | Markdown Preview Plus     |
| 不想装任何扩展           | 上面那个单文件 HTML       |
| 日常写笔记 + 偶尔预览    | 直接用 VS Code + 浏览器预览 |

你现在最常用来写 Markdown 的编辑器是哪一个？我可以根据你的使用习惯再推荐更精确的搭配方式～