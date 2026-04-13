### 已经制作完成，在文件夹下执行即可。
要把這條命令：

```bash
find . -name "*.md" -exec cat {} + > ../merged_$(date +%Y%m%d_%H%M%S).md
```

變成一個**可執行文件**（在 Mac 上隨時輸入名字就能跑），最簡單且推薦的方式是做成 **shell 腳本**，步驟如下：

### 步驟（最常用做法）

1. 在你常用的地方建立一個 bin 資料夾（如果還沒有）

```bash
mkdir -p ~/bin
```

2. 建立腳本檔案（取一個你喜歡的名字，例如 `merge-md`）

```bash
nano ~/bin/merge-md
# 或者用 code、vim、TextEdit 都可以
```

3. 把下面內容完整貼進去（**第一行 shebang 千萬不要漏**）

```bash
#!/usr/bin/env bash
set -euo pipefail   # 建議加上，比較安全

echo "正在合併當前資料夾內所有 .md 檔案..."

output="../merged_$(date +%Y%m%d_%H%M%S).md"

find . -name "*.md" -exec cat {} + > "$output"

echo "合併完成 → $output"
echo "總共 $(wc -l < "$output") 行"
```

4. 存檔後，給予執行權限（**這步最重要**）

```bash
chmod +x ~/bin/merge-md
```

5. 確認你的 PATH 已經包含 `~/bin`（新版 macOS 通常預設有）

```bash
# 查看目前 PATH
echo $PATH

# 如果沒有 ~/bin，可以加進去（加到 ~/.zshrc 最後面）
echo 'export PATH="$HOME/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
```

完成！以後只要進入任何有 .md 檔案的資料夾，直接輸入：

```bash
merge-md
```

就會自動產生類似 `../merged_20260211_143022.md` 這樣的檔案。

---

---
./工具箱/Mac玩法/merge-md.md ---这是以上内容的文件名

---
