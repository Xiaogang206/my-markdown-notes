# 简化版本

## 4.1 初始化数据库

自己的 开发者令牌，登录并访问 DeveloperToken
```
evernote-backup init-db --backend china -t <你的开发者令牌DeveloperToken>
```

## 4.2 令牌再次授权

由于 印象笔记（国内版） DeveloperToken 有效期只有 7 \* 24 小时有效期，因此超期时需要重新授权，对应命令如下：（疑问：这时候需要去官网获取还是用旧的token再次授权），如果是后者，我需要保存一下我的token。

格式：

```
evernote-backup reauth --token <your_developer_token>
```

## 4.3 同步笔记数据（token在有效期内）

```
evernote-backup sync
```

## 4.4 导出为 \*.enex 文件

```
evernote-backup export output_dir/
```

其中 output\_dir 需要修改为自己需要输出的文件目录。

# 1 缘由

国际版印象笔记（Evernote）可以把笔记导出为自由开放的 .enex 文件，但印象笔记（中国）已经无法使用该格式导出了，这导致无法将自己的笔记从中导出并导入到其他笔记软件中，或者将自己的笔记作为AI模型的知识库使用，如转为 Markdown。

但好在 Vlad 大佬提供了一款名为evernote-backup 的开源工具，能够将笔记通过同步备份方式将数据下载下来，并提供了导出为  .enex 文件的方法。

# 2 Evernote-backup 介绍

Evernote-backup 是能够将 Evernote 从远程服务器备份到你的电脑上的开源软件，并且支持随时导出。包含以下能力

快速将所有笔记同步到本地的 SQLite 数据库中进行备份。

以 \*.enex 格式导出所有备份笔记，可以是整个笔记本或单个笔记。

支持 Evernote（国际版） 和 印象笔记（国内版）。

# 3 下载与安装

  GitHub下载或者Homebrew下载。

# 4 操作方法

## 4.1 初始化数据库

打开命令行，该步骤只需要执行一次

教程中的以下命令行指令方式目前不生效了：

```
evernote-backup init-db --backend china
```

会报错：

evernote.edam.error.ttypes.EDAMUserException: EDAMUserException(errorCode=8, parameter='consumerKey')

解决方法是采用自己的 开发者令牌，具体步骤如下：

登录并访问 DeveloperToken

获得对应的code 形如

S=T3I:U=wNnMC:E=Gi9fzR0k8lr:C=H8d2itP14G1:P=YW9S:A=eF0BPwgRiDM:V=q:H=OZDPLnUVQ56R3MSHObdJQZtVrTCn53JS

修改在原来的基础上增加

\-t S=T3I:U=wNnMC:E=Gi9fzR0k8lr:C=H8d2itP14G1:P=YW9S:A=eF0BPwgRiDM:V=q:H=OZDPLnUVQ56R3MSHObdJQZtVrTCn53JS

格式：

```
evernote-backup init-db --backend china -t <你的开发者令牌DeveloperToken>
```

示例：

evernote-backup init-db --backend china -t S=T3I:U=wNnMC:E=Gi9fzR0k8lr:C=H8d2itP14G1:P=YW9S:A=eF0BPwgRiDM:V=q:H=OZDPLnUVQ56R3MSHObdJQZtVrTCn53JS

完整示例：

```
$ evernote-backup init-db --force --backend china -t S=T3I:U=wNnMC:E=Gi9fzR0k8lr:C=H8d2itP14G1:P=YW9S:A=eF0BPwgRiDM:V=q:H=OZDPLnUVQ56R3MSHObdJQZtVrTCn53JS
```

Authorizing auth token, china backend...

Successfully authenticated as YOUR\_USER\_NAME!

Current login will expire at 2024-05-13 15:43:53.

Initializing database en\_backup.db...

Reading database en\_backup.db...

Successfully initialized database for YOUR\_USER\_NAME!

## 4.2 令牌再次授权

由于 印象笔记（国内版） DeveloperToken 有效期只有 7 \* 24 小时有效期，因此超期时需要重新授权，对应命令如下：

格式：

```
evernote-backup reauth --token <your_developer_token>
```

示例：

```
evernote-backup reauth --token S=T3I:U=wNnMC:E=Gi9fzR0k8lr:C=H8d2itP14G1:P=YW9S:A=eF0BPwgRiDM:V=q:H=OZDPLnUVQ56R3MSHObdJQZtVrTCn53JS
```

完整示例：

evernote-backup reauth --token S=T3I:U=wNnMC:E=Gi9fzR0k8lr:C=H8d2itP14G1:P=YW9S:A=eF0BPwgRiDM:V=q:H=OZDPLnUVQ56R3MSHObdJQZtVrTCn53JS

Reading database en\_backup.db...

Authorizing auth token, china backend...

Successfully authenticated as YOUR\_USER\_NAME!

Current login will expire at 2024-05-13 15:43:53.

Successfully refreshed auth token for YOUR\_USER\_NAME!

4.3 同步笔记数据

```
evernote-backup sync
```

当看到提示 Synchronization completed! 就代表同步成功了。

示例：

$ evernote-backup sync

Reading database en\_backup.db...

Authorizing auth token, evernote backend...

Successfully authenticated as YOUR\_USER\_NAME!

Current login will expire at 2022-03-10 10:22:00.

Syncing latest changes...

  \[####################################\]  6763/6763

566 notes to download...

  \[####################################\]  566/566

Updated or added notebooks: 23

Updated or added notes: 566

Expunged notebooks: 0

Expunged notes: 0

Synchronization completed!

该方法支持断点续传，即可以随时中断再次运行本命令后可以从上次断开处继续下载数据，如报错

Aborting, please wait... Rate limit reached. Restart program in 14:30.

则需要等待对应的时间后再次执行命令

当看到 Synchronization completed! ，本次同步就完成了：

$ evernote-backup sync

Reading database en\_backup.db...

Authorizing auth token, china backend...

Successfully authenticated as YOUR\_USER\_NAME!

Current login will expire at 2024-05-13 15:43:53.

Syncing user notebooks...

User notebooks are up to date, nothing to sync!

Syncing linked notebooks...

113 note(s) to download...

Requesting access to 1 linked notebook(s)...

Downloading 113 note(s)...

  \[####################################\]  113/113

Updated or added notebooks: 0

Updated or added notes: 113

Expunged notebooks: 0

Expunged linked notebooks: 0

Expunged notes: 0

Synchronization completed!

## 4.4 导出为 \*.enex 文件

```
evernote-backup export output_dir/
```

其中 output\_dir 需要修改为自己需要输出的文件目录。

默认会按一个笔记本一个 \*.enex 文件方式导出。

如果希望按单个笔记 方式导出，则需要加上 --single-notes（经验证，没必要导出单个笔记）


Created at: 2026-02-08
Last updated at: 2026-02-09

 notebook:工具箱


---
./工具箱/其他/导出Evernote为enex的方法.md ---这是以上内容的文件名

---
