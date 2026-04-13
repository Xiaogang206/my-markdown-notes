**我最终选择了阿里云OSS**，以下内容仅仅作为记录。
Cloudflare R2 是目前搭建个人图床的“神仙级”选择，它的核心优势只有两个字：**省钱**（甚至完全免费）。

与阿里云 OSS 或腾讯云 COS 不同，R2 **不收取流量流出费用（Egress Fees）**，且拥有极其慷慨的免费额度。

---

### 1. 为什么选 Cloudflare R2？（价格优势）

|**计费项**|**免费额度（每月）**|**超出部分费用**|
|---|---|---|
|**存储空间**|**10 GB**|$0.015 / GB|
|**A 类操作** (上传/修改)|**100 万次**|$4.50 / 百万次|
|**B 类操作** (查看/下载)|**1000 万次**|$0.36 / 百万次|
|**流量流出 (Egress)**|**完全免费**|**$0.00**|

> **一句话总结**：对于个人笔记和小型博客，你几乎不可能用超这个免费额度。

---

### 2. 搭建三步走

#### 第一步：创建存储桶 (Bucket)

1. 登录 [Cloudflare 控制台](https://dash.cloudflare.com/)，点击左侧菜单栏的 **R2**。
    
2. 点击 **Create bucket**，起一个名字（如 `my-obsidian-images`）。
    
3. 创建完成后，点击进入该桶的 **Settings** 选项卡。
    
4. 找到 **Public Access**（公共访问）：
    
    - **方法 A (推荐)**：绑定一个你自己的域名（例如 `img.yourdomain.com`）。
        
    - **方法 B (快速)**：开启 `r2.dev` 临时域名（注意：这个域名有时会有访问限制，仅建议测试使用）。
        

#### 第二步：获取 API 密钥 (钥匙)

你需要让 PicGo 有权限往 R2 桶里放东西：

1. 回到 R2 首页，点击右侧的 **Manage R2 API Tokens**。
    
2. 点击 **Create API token**。
    
3. **权限设置**：选择 `Object Read & Write`。
    
4. **Bucket 选择**：指定你刚才创建的那个桶。
    
5. 创建后，你会得到三个关键信息：**Access Key ID**、**Secret Access Key** 以及一个 **S3 Endpoint**。
    
    - _注意：Secret Access Key 只会出现一次，务必复制保存！_
        

#### 第三步：配置 PicGo

1. 打开 PicGo，在插件设置中搜索并安装 **`s3`** 插件（因为 R2 完美兼容 S3 协议）。
    
2. 在图床设置中找到 **Amazon S3**（或其他 S3 插件），填入信息：
    
    - **Access Key ID / Secret Key**：填入你刚才生成的。
        
    - **Bucket**：你的桶名。
        
    - **Endpoint**：填入 Cloudflare 给你的 S3 Endpoint 地址。
        
    - **Region**：填 `auto`。
        
    - **Custom Path**：建议开启，可以按日期分类图片，如 `images/{year}/{month}/`。
        

---

### 3. 如何在 Obsidian 里无缝体验？

安装 **`Image Auto Upload Plugin`** 插件后：

1. 插件设置 -> **Uploader** 选择 `PicGo-Core` 或 `PicGo (app)`。
    
2. 只要你在笔记里粘贴图片，它就会自动排队上传到 Cloudflare R2。
    
3. 链接会自动变成 `https://img.yourdomain.com/2026/02/pic.png`。
    

---

### ⚠️ 一个非常关键的“坑”

**支付验证**：虽然 R2 是免费的，但 Cloudflare 要求你的账户必须绑定一个**有效的支付方式**（信用卡或 PayPal）才能开启 R2 服务。它不会扣你钱，但这一步是必须的。

---
