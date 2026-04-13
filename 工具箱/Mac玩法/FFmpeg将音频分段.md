要在 Mac 终端高效处理音频文件，最专业且稳定的工具是 **FFmpeg**。

你的需求是将 380MB 的文件平分成两份。由于音频文件的“容量”是由**比特率（Bitrate）和时长（Duration）决定的，直接按字节切割可能会损坏文件头，因此标准做法是按时长**对半切。

### 1. 安装工具

如果你的 Mac 还没有安装 FFmpeg，请先通过 Homebrew 安装：

Bash

```
brew install ffmpeg
```

---

### 2. 自动化分割脚本

我为你写了一个 Bash 脚本。它会自动获取音频总时长，计算中点，然后精确地将其切分为两部分。

你可以直接将以下代码复制并保存为 `split_audio.sh`，或者直接在终端分段执行：

Bash

```
#!/bin/bash

# 输入文件名（请确保文件名正确，或将文件拖入终端获取路径）
INPUT="你的文件名.m4a"
OUTPUT1="part1.m4a"
OUTPUT2="part2.m4a"

# 1. 获取总时长（秒）
DURATION=$(ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 "$INPUT")

# 2. 计算中点
HALF=$(echo "$DURATION / 2" | bc -l)

echo "总时长: $DURATION 秒"
echo "正在切分中点: $HALF 秒..."

# 3. 执行切分（使用 -c copy 模式，速度极快且无损）
# 第一部分：从 0 开始，持续时间为 HALF
ffmpeg -i "$INPUT" -t "$HALF" -c copy "$OUTPUT1" -y

# 第二部分：从 HALF 开始，直到结束
ffmpeg -i "$INPUT" -ss "$HALF" -c copy "$OUTPUT2" -y

echo "切分完成：$OUTPUT1 和 $OUTPUT2"
```

---

### 3. 注意事项（一针见血的建议）

- **不要尝试按字节切割：** 如果你用 `split` 命令按二进制大小切割，得到的 `part2.m4a` 将因为缺少元数据和文件头而无法播放。必须使用 FFmpeg 这种感知编码的工具。
    
- **关于“-c copy”：** 上述代码使用了 `-c copy` 参数。这意味着它只是“搬运”数据流而不重新编码。
    
    - **优点：** 速度极快（几秒钟完成），音质完全无损。
        
    - **潜在问题：** M4A 容器对切分点比较敏感，有时 `-c copy` 可能导致切分点附近几秒钟出现静音或定位不准。如果发现播放异常，请将 `-c copy` 删掉，让它重新编码（速度变慢，但兼容性最好）。
        
- **文件路径：** 在终端运行脚本前，确保你已经 `cd` 到了文件所在的文件夹。如果文件名包含空格，请务必在脚本中用双引号包裹变量。
    

### 4. 进阶：如果你想一步到位（一行命令）

如果你不想写脚本，手动查一下时长（假设是 60 分钟），直接运行这两行即可：

Bash

```
ffmpeg -i input.m4a -t 00:30:00 -c copy part1.m4a
ffmpeg -i input.m4a -ss 00:30:00 -c copy part2.m4a
```

如果你需要针对这 380MB 文件进行更复杂的压缩处理，可以告诉我。