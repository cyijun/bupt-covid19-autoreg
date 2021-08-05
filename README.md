# bupt-covid19-autoreg

## 简介
Auto registration for COVID-19 daily check in BUPT

北邮新冠自动打卡

## 使用方法
下载本仓库后，在shell中进入本仓库目录。
在当前目录下创建名为userinfo.json的文件，文件内容如下。
<pre>
{
    "username": "2018000000",
    "password": "qwerty!@#$"
}
</pre>
可以打开下属链接尝试出自己的密码（一般为统一身份认证的密码？）。

<https://app.bupt.edu.cn/uc/wap/login?redirect=https%3A%2F%2Fapp.bupt.edu.cn%2Fncov%2Fwap%2Fdefault%2Findex>

然后，执行下面一行命令。
<pre>
$ chmod +x run.sh kill.sh
</pre>
### 获得并储存历史上报数据
2021.8开始疑似会清除一定时间之前的历史信息，因此改为本地保存历史信息。
<pre>
python3 getoldinfo.py
</pre>
### 启动后台打卡
执行下面一行命令即可后台打开自动打卡程序。
<pre>
$ ./run.sh
</pre>
### 关闭后台打卡
执行下面一行命令可以结束自动打卡程序。
<pre>
$ ./kill.sh
</pre>
### 日志
启动自动打卡后，会在当前目录生成log.txt，可用于观察打卡是否成功。

## 注意事项
本程序默认设置为在00：01-12：00一小时尝试一次打卡，因此在0点到1点之间的早一些时间有可能尚未打卡，但这也意味着，在没有错误发生时，超过1点必定打卡成功。注意观察log.txt的内容，以确保打卡成功。

目前run.sh和kill.sh尚无Windows版本，因此Windows用户可直接执行py文件。

Mac用户只要不关机，即使合上盖子后台也会持续执行该脚本。