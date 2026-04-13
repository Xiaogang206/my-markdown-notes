针对 MacBook 上 FaceTime 无法激活或使用的故障，你可以按照以下结构化的排查流程进行操作。这些步骤已经过优化，方便你直接复制到 **Obsidian** 中存档。

---

## FaceTime 故障排查清单

### 1. 基础状态检查

在进行复杂操作前，先确认以下三点：

- **Apple 服务状态：** 访问 [Apple System Status](https://www.apple.com/support/systemstatus/)，确认 "FaceTime" 旁边是绿灯。
    
- **网络环境：** 尝试切换 Wi-Fi 或连接手机热点。部分校园网或公司内网可能会屏蔽 FaceTime 所需的端口。
    
- **日期与时间：** 前往 **系统设置 > 通用 > 日期与时间**，确保勾选了“自动设置日期和时间”。如果时间不准，验证服务器会拒绝登录。
    

---

### 2. 账号与激活配置 (针对无手机号环境)

既然你只使用 Apple ID，请重点排查：

- **重新登录：**
    
    1. 打开 FaceTime，点击菜单栏 **FaceTime 通话 > 设置**。
        
    2. 点击“退出登录”，等待 30 秒后重新输入 Apple ID 登录。
        
- **检查受达方式：**
    
    - 确保在“你可通过以下方式接受 FaceTime 通话”列表中，你的**电子邮件地址**已被勾选。
        
    - 如果显示“正在验证”，请登录 [appleid.apple.com](https://www.google.com/search?q=https://appleid.apple.com) 检查该邮箱是否已完成验证。
        

---

### 3. 系统底层排查 (针对 Mac)

如果账号正常但依然无法连接，请尝试以下操作：

#### A. 重置 FaceTime 进程

打开 **终端 (Terminal)**，输入以下命令并回车（这会强制重启负责身份验证的后台服务）：

Bash

```
sudo killall avconferenced
```

#### B. 清理缓存文件

1. 在访达 (Finder) 中按下 `Command + Shift + G`。
    
2. 输入 `~/Library/Preferences/` 并回车。
    
3. 找到并删除 `com.apple.FaceTime.plist`（系统会自动重建该文件）。
    
4. 重启 FaceTime。
    

---

### 4. 常见错误代码与对策

|**现象**|**可能原因**|**解决方法**|
|---|---|---|
|**一直显示“正在登录”**|激活服务器连接受阻|修改 DNS 为 `8.8.8.8` 或 `114.114.114.114`。|
|**呼叫失败 (Failed)**|对方未激活或防火墙拦截|确认对方已开启 FaceTime；检查系统防火墙是否允许 FaceTime 传入连接。|
|**找不到语音通话选项**|地区限制|**注意：** 如果你的设备或账号属于中国大陆，Mac 版 FaceTime 默认屏蔽语音入口，仅保留视频。|

---

