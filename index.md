---
layout: default
title: 我的 Markdown 笔记索引
---

## 目录
- [书籍](#书籍)
- [书籍目录](#书籍目录)
- [人物](#人物)
- [哲学～大问题](#哲学大问题)
- [圆桌讨论](#圆桌讨论)
- [播客](#播客)
- [文学](#文学)
- [王志安](#王志安)
- [社科类](#社科类)
- [英语](#英语)
- [话题](#话题)

---

## 书籍
{% for file in site.pages %}
{% if file.path contains '书籍/' %}
- [{{ file.name | replace: '.md', '' }}]({{ file.path }})
{% endif %}
{% endfor %}

---

## 书籍目录
{% for file in site.pages %}
{% if file.path contains '书籍目录/' %}
- [{{ file.name | replace: '.md', '' }}]({{ file.path }})
{% endif %}
{% endfor %}

---

## 人物
{% for file in site.pages %}
{% if file.path contains '人物/' %}
- [{{ file.name | replace: '.md', '' }}]({{ file.path }})
{% endif %}
{% endfor %}

---

## 哲学～大问题
{% for file in site.pages %}
{% if file.path contains '哲学～大问题/' %}
- [{{ file.name | replace: '.md', '' }}]({{ file.path }})
{% endif %}
{% endfor %}

---

## 圆桌讨论
{% for file in site.pages %}
{% if file.path contains '圆桌讨论/' %}
- [{{ file.name | replace: '.md', '' }}]({{ file.path }})
{% endif %}
{% endfor %}

---

## 播客
{% for file in site.pages %}
{% if file.path contains '播客/' %}
- [{{ file.name | replace: '.md', '' }}]({{ file.path }})
{% endif %}
{% endfor %}

---

## 文学
{% for file in site.pages %}
{% if file.path contains '文学/' %}
- [{{ file.name | replace: '.md', '' }}]({{ file.path }})
{% endif %}
{% endfor %}

---

## 王志安
{% for file in site.pages %}
{% if file.path contains '王志安/' %}
- [{{ file.name | replace: '.md', '' }}]({{ file.path }})
{% endif %}
{% endfor %}

---

## 社科类
{% for file in site.pages %}
{% if file.path contains '社科类/' %}
- [{{ file.name | replace: '.md', '' }}]({{ file.path }})
{% endif %}
{% endfor %}

---

## 英语
{% for file in site.pages %}
{% if file.path contains '英语/' %}
- [{{ file.name | replace: '.md', '' }}]({{ file.path }})
{% endif %}
{% endfor %}

---

## 话题
{% for file in site.pages %}
{% if file.path contains '话题/' %}
- [{{ file.name | replace: '.md', '' }}]({{ file.path }})
{% endif %}
{% endfor %}
