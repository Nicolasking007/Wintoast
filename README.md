# Wintoast
借助win10+消息通知，提醒做某些事情

## 效果预览

- 全屏显示 

![](./image/09.png)

- 通知中心

![](./image/09_1.png)

## 借助window 任务计划程序 定时执行

### 配置定时任务

- 点击创建任务

![img_1.png](./image/img_1.png)

- 新建触发器

![img_2.png](./image/img_2.png)

![img_3.png](./image/img_3.png)

![img_4.png](./image/img_4.png)

- 新建操作

![img_5.png](./image/img_5.png)

- 设置完成

![img.png](./image/img.png)


### 使用vbs 无弹窗后台静默执行

- 复制文本，修改后缀为 `.vbs`

```commandline
set ws=WScript.CreateObject("WScript.Shell")
ws.Run "E:\CodeShare\toast\Run.bat /start",0

```

- 复制文本，修改后缀为 `.bat`

```commandline
cd/d E:\Wintoast\
python wintoast.py
```

### 获取APPID

![img.png](./image/id_img.png)