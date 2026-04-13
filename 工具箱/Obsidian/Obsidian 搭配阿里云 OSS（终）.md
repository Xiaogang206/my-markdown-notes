---
share_link: https://share.note.sx/i0xu0fsc#ubOhx7wUI7GvSmiQ+ZWB/y12xmCkFiVYDFQIsTq4J2U
share_updated: 2026-02-11T21:28:22+08:00
---
用 Obsidian 搭配阿里云 OSS 搭建图床，是目前追求**极速访问**和**数据自主权**的最优解之一。

目前最主流、最丝滑的方式是：**Obsidian + Image Auto Upload 插件 + PicGo-Core**。这套方案能实现“粘贴图片即自动上传并替换链接”。

---

## 第一步：准备阿里云 OSS 环境

1. **创建 Bucket**：
    
    - 登录阿里云控制台，进入 **OSS 对象存储**。
        
    - 新建一个 Bucket（存储桶），权限设为 **公共读**（这点很重要，否则 Obsidian 里看不了图）。
        
    - 记下你的 **Bucket 名称** 和 **Endpoint**（如 `oss-cn-hongkong.aliyuncs.com`）。
        
2. **获取访问密钥 (AK)**：
    
    - 鼠标移至头像，选择 **AccessKey 管理**。
        
    - 创建一个 AccessKey，保存好 **AccessKey ID** 和 **AccessKey Secret**（切记不要泄露）。
        

---

## 第二步：配置 PicGo-Core（核心引擎）

虽然你可以下载 PicGo 的窗口程序，但为了轻量化，建议直接在 Obsidian 插件里调用内核。

1. **安装 Node.js**（如果电脑没装）：前往 [Node.js 官网](https://nodejs.org/) 下载安装。
    
2. **安装 PicGo 核心**：
    
    打开终端（CMD 或 Terminal），输入：
    
    Bash
    
    ```
    npm install picgo -g
    ```
    
3. **安装阿里插件**：
    
    Bash
    
    ```
    picgo install ali-oss
    ```
    

---

## 第三步：在 Obsidian 中“一键联动”

1. **安装插件**：
    
    - 进入 Obsidian `设置` -> `社区插件` -> `浏览`。
        
    - 搜索并安装 **Image Auto Upload Plugin**。
        
2. **插件参数配置**：
    
    - 在插件设置中，将 **Uploader** 选择为 `PicGo-Core`。
        
    - 找到 **PicGo path**，填入你的 PicGo 程序路径（通常在终端输入 `where picgo` 即可找到）。
        
3. **配置阿里云参数**：
    
    你可以直接修改 PicGo 的配置文件（`~/.picgo/config.json`），格式如下：
    

JSON

```
{
  "picBed": {
    "uploader": "aliyun",//这里不修改
    "aliyun": {
      "accessKeyId": "你的ID",
      "accessKeySecret": "你的Secret",
      "bucket": "存储桶名",
      "area": "oss-cn-hangzhou", // 对应你的地域，我的是oss-cn-hongkong
      "path": "img/", // 存储路径,这是阿里云oss的文件夹
      "customUrl": "", // 如果有备案域名可填，没有就留空，用阿里云自己的就好
      "options": ""
    }
  }
}
```

---

## 第四步：使用体验

配置完成后，你只需要：

- **截图** -> 在 Obsidian **Ctrl+V 粘贴**。
    
- 插件会瞬间接管动作，上传到阿里云，并将本地路径自动替换为 `https://xxx.oss.../image.png`。
    

---

### 💡 避坑小贴士

- **防盗链设置**：如果你担心流量被刷，可以在阿里云 OSS 后台设置“防盗链”，将你的博客域名或本地开发环境加入白名单。
    
- **图片压缩**：OSS 支持“图片处理”规则。你可以在 URL 后面加 `?x-oss-process=style/compressed` 来加载压缩后的图，节省流量费。
    
- **价格提示**：OSS 存储空间很便宜，但**下行流量**是收费的。对于个人笔记来说，每月几毛钱通常就足够了。
    
---

## 修改 PicGo 的配置文件

修改配置文件是很多新手卡壳的地方，因为它是一个**隐藏的 JSON 文件**。根据你的操作系统，路径略有不同。

### 1. 找到文件的具体路径

- **直接前往文件夹（最快）**
        
    - **macOS**: 打开 Finder，按 `Command + Shift + G`，输入 `~/.picgo/`。

---

### 2. 如何编辑它？

不要直接双击打开（可能会用浏览器打开导致无法编辑）。

1. **右键点击** `config.json`。
    
2. 选择 **“打开方式”** -> **“记事本”** 或 **“VS Code”**。
    
3. 将我上一个回答中的代码块复制进去，替换掉原有的全部内容，然后修改成你自己的 `accessKeyId` 等参数。

---

### 💡 一个小技巧：验证是否成功

配置完成后，你可以随便找一张图片，在终端执行：

Bash

```
picgo upload C:\path\to\your\test_image.png
```

如果返回了阿里云的 URL，说明你的配置文件写对了。

---

## 提示出错：upload failed, check dev console

出现这个错误提示，说明 **PicGo 尝试上传但被拦截了**。因为 PicGo-Core 在后台运行，我们无法直接看到报错细节，所以需要通过“手动模拟上传”来抓取真正的错误代码。

请按以下步骤操作，90% 的错误都能在第一步现形：

---

### 第一步：排查真正的“报错代码”

打开你电脑的终端（CMD 或 PowerShell），输入以下命令并回车：

Bash

```
picgo upload  你的图片路径
```

_(可以直接输入 `picgo upload` 然后把电脑里的一张图片拖进窗口，路径会自动补全)_

**查看返回的报错信息（重点）：**

- **`AccessDenied`**: 你的 `AccessKey` 填错了，或者该 Key 没有 OSS 的管理权限。
    
- **`NoSuchBucket`**: `bucket`（桶名）填错了，或者 `area`（地域）与桶所在的实际地域不符。
    
- **`SocketTimeout`**: 网络连接超时，检查你的电脑能否正常访问阿里云域名，或是否挂了代理。
    
- **`SignatureDoesNotMatch`**: 签名不匹配。通常是 `accessKeySecret` 复制时多了空格。
    

---

### 第二步：对照检查 `config.json` 常见死穴

请再次检查你的配置文件，确认以下细节：

1. **地域代码 (Area)**：
    
    必须是类似 `oss-cn-shanghai` 这种格式。注意：**不要带 `https://`**。
    
2. **权限设置**：
    
    进入阿里云 OSS 控制台，确认你的 Bucket 权限是 **“公共读” (Public Read)**。
    
3. **JSON 格式自检**：
    
    确保你填写的配置里，所有的标点符号都是**英文半角**。
    

---

### 第三步：Obsidian 内部设置检查

如果命令行（第二步）上传成功了，但 Obsidian 里还是报错，请检查：

1. **PicGo 路径**：
    
    在 Obsidian 插件设置里，确保 **PicGo Path** 填写的是 `picgo` 的完整绝对路径。你可以通过在命令行输入 `where picgo` (Windows) 或 `which picgo` (Mac) 来获取。
    
2. **Uploader 选择**：
    
    确保插件里的 `Uploader` 选的是 `PicGo-Core` 而不是 `PicGo (app)`。
    

---

## 阿里云OSS设置注意点


这种方式几乎能做到“像本地一样粘贴图片 → 自动/一键上传到 OSS → 笔记里自动变成外链”，使用体验最好。

### 最推荐的详细步骤（PicGo方案）

1. **阿里云 OSS 准备**（最重要一步，很多新手卡在这里）
   - 登录阿里云 → 开通 OSS（选标准存储，40GB/80GB 套餐很便宜）
   - 创建 Bucket
     - 读写权限：**公共读**（Public Read）---这一点很重要，不要选错了。
     - 防盗链：**允许空 Referer**（非常重要！否则 Obsidian 预览看不到图）
   - 创建 RAM 子用户（强烈建议不要用主账号 AK）
     - 授予权限：AliyunOSSFullAccess----这一点很重要。
     - 记录 AccessKey ID 和 AccessKey Secret



4. **使用方式**
   - 正常 Ctrl+V / 拖入 / 粘贴图片
   - 插件会自动（或按快捷键）调用 PicGo → 上传到 OSS → 把笔记里的本地路径替换成阿里云OSS的路径。
   - 如果没自动：Ctrl+P → 搜索 “Upload all images” 一键全传

---
