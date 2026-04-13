import os
import json
import re

def generate():
    posts = []
    categories = {}
    
    # 获取所有 md 文件，排除公共文件
    files = [f for f in os.listdir('.') if f.endswith('.md') and f not in ['index.md', 'categories.md', 'search.md', 'timeline.md']]
    
    for file in files:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
            
            # 提取 YAML 属性
            title_match = re.search(r'^title:\s*(.*)', content, re.M)
            cat_match = re.search(r'^category:\s*(.*)', content, re.M)
            
            title = title_match.group(1).strip() if title_match else file
            category = cat_match.group(1).strip() if cat_match else "未分类"
            
            # 存入搜索索引
            posts.append({
                "title": title,
                "path": f"./{file}",
                "content": re.sub(r'\s+', ' ', content)[:500] # 截断内容减小体积
            })
            
            # 存入分类
            if category not in categories: categories[category] = []
            categories[category].append(f"- [{title}](./{file})")

    # 1. 生成 search.json
    with open('search.json', 'w', encoding='utf-8') as f:
        json.dump(posts, f, ensure_ascii=False)

    # 2. 生成 categories.md
    with open('categories.md', 'w', encoding='utf-8') as f:
        f.write("# 分类目录\n\n")
        for cat, links in categories.items():
            f.write(f"## {cat}\n" + "\n".join(links) + "\n\n")

if __name__ == "__main__":
    generate()
