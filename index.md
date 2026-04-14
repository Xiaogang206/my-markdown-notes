
---
title: 首页
enableToc: false
---

# 👋 欢迎来到我的 Quartz 笔记库

这里是我所有知识、阅读、思考与研究的数字花园。  
内容来自我的日常学习、阅读笔记、思考记录、主题研究等。

---

## 🕒 最近更新

```Dataview
TABLE file.mtime AS "更新时间"
FROM ""
SORT file.mtime DESC
LIMIT 10
```

```Dataview
LIST
FROM ""
GROUP BY file.folder
```

```Dataview
LIST
FROM ""
WHERE file.tags
GROUP BY file.tags
```

```Dataview
TABLE file.link AS "文档", file.folder AS "分类", file.mtime AS "更新时间"
FROM ""
SORT file.name ASC
```
