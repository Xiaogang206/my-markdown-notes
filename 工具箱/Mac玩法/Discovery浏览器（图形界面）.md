 
 用**Discovery**浏览器（图形界面）

Mac 上安装 Bonjour Browser 或 **Discovery** （App Store 免费），

它会自动列出局域网内所有启用 Bonjour 的设备（Mac 默认启用）。

你能看到：

- 设备名称
- 服务类型
- IP 地址
- 

经测试，得到如下结果：

ping MacBook-Neo.local

Last login: Sat Mar 21 12:18:58 on ttys001

xiaogang206@Mac ~ % ping MacBook-Neo.local

PING macbook-neo.local (192.168.31.50): 56 data bytes

---

# **🟦 方法四：如果你知道对方的主机名（例如 “MacBook-Neo.local”）**

你可以直接解析它的 mDNS 名称：

```bash
ping MacBook-Neo.local
```

如果它在线，会直接显示 IP。

---

# **🟦 方法五：用 Bonjour 浏览器（图形界面）**

Mac 上安装 **Bonjour Browser** 或 **Discovery**（App Store 免费）， 它会自动列出局域网内所有启用 Bonjour 的设备（Mac 默认启用）。

你能看到：

- 设备名称
- 服务类型
- IP 地址

---

# **🍎 Bonjour 是什么？**

**Bonjour 是 Apple 的“零配置网络（Zero‑configuration networking）技术”。** 它让局域网内的设备可以**自动发现彼此**，不需要你手动输入 IP、端口或做任何复杂设置。

简单说：

> **Bonjour = 局域网内设备自动互相发现的系统**

只要设备支持 Bonjour（Mac、iPhone、iPad、部分打印机、NAS 等），它们就能自动广播自己的服务，让其他设备看到。

---

# **🔍 Bonjour 设备是什么意思？**

当你看到“Bonjour 设备”时，它指的是：

> **在局域网中通过 Bonjour 广播自己、并能被自动发现的设备**

例如：

- 另一台 Mac
- iPhone / iPad
- 支持 AirPrint 的打印机
- NAS（如 Synology）
- Apple TV
- HomePod
- 共享文件的电脑
- 共享屏幕的电脑
- 提供 Web 服务的设备（如某些路由器）

这些设备会自动告诉局域网：

- 我是谁（设备名）
- 我提供什么服务（文件共享、AirPlay、打印等）
- 我的 IP 地址是什么

你无需知道它的 IP，它自己会“喊出来”。

---

# **🧠 Bonjour 是如何做到的？**

它主要依赖两个协议：

|**技术**|**作用**|
|---|---|
|**mDNS（Multicast DNS）**|让设备通过名字（如 `MacBook-Pro.local`）互相找到|
|**DNS‑SD（DNS Service Discovery）**|让设备广播自己提供的服务（如 AirPlay、打印）|

所以你能直接：

```bash
ping MacBook-Pro.local
```

而不需要知道它的 IP。

---

# **🖥 举个最直观的例子**

你在 Finder 左侧看到：

- “隔空投送”
- “共享”里的其他 Mac
- “网络”里的打印机

这些都是 Bonjour 自动发现的。

你没有输入 IP，它们就出现了。

---

# **🧭 你为什么会看到“Bonjour 设备”？**

因为你正在扫描局域网或使用某些工具（如 Discovery、LanScan、nmap）， 它们会显示所有通过 Bonjour 广播自己的设备。

这类设备通常是：

- Mac
- iPhone
- 打印机
- NAS
- Apple TV

---

# **📌 如果你想找到另一台 Mac 的 IP**

Bonjour 反而是最简单的方式。

只要你知道对方的主机名（例如 `MacBook-Pro.local`），你可以直接：

```bash
ping MacBook-Pro.local
```

它会返回：

```
PING MacBook-Pro.local (192.168.1.23)
```

这就是它的 IP。

如果你不知道主机名，我也可以教你如何自动发现它。

---

