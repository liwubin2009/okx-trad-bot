这是一个根据自身交易体系，为了辅助自己做单而设计的机器人
它包含两个功能
功能一、根据 TV 信号或者手动信号机器人进单
这是一个双向机器人，所以请将交易所设置为开平仓模式，并将交易单位设置为张
这是一个风控型机器人，所以他有严格的风控规则，其中一个最重要的点，通过工具或者 TV 信号的订单，没有止盈止损的，默认会拦截。不会开单
这是一个辅助机器人，它根据自身交易体系设计，故而有很多实用的进单方式。比如一单进场，二两进场，三单进场，五单进场并且提供平均和倍投两种方式
默认启用以损定仓，白话解释就是你下的仓位由你设置的止损金额以及订单的止损空间自动计算得出
功能二、订单接管功能
机器人只会接管有止盈止损的订单
机器人在接管订单后，会将订单进场交易所级的拆分，会将各个订单已委托的单的形式委托在交易所
会自动将订单分批离场以及自动转换移动止盈止损，所以，它还是一个利润型机器人

过多功能不在这里说明了，有兴趣的可以去交流群问https://t.me/+I1jpWT5H-A9lNDQ1

本机器人提供两种安装模式，对有代码基础的小伙伴可以下载源码自行在 linux 服务器上部署

对于没有代码基础但想使用的 提供快捷部署文件 install.sh
如果你需要快捷部署，请选择非大陆的服务器，系统选择 centos 版本选择 7.6 
这样你可以通过以下四步快捷的将机器人部署到我们的服务器上请以 root 登录安装部署：
一、wget  --no-check-certificate https://mirrors.tuna.tsinghua.edu.cn/anaconda/archive/Anaconda3-2021.11-Linux-x86_64.sh 
这一步下载 anaconda3 
二、bash Anaconda3-2021.11-Linux-x86_64.s
这一步，是安装 anaconda3 具体安装教程可以搜索“centos anaconda3 安装教程”
三、wget  --no-check-certificate http://43.163.211.97:8000/install.sh
这一步下载快捷的安装命令 下载完后
四、bash install.sh 下载执行这个命令然后等待即可
五、reboot 第四步执行完以后，执行 reboot 重启后一分钟即可进入机器人配置页面
配置地址：http://xx.xx.xx.xx:443/
webhook地址：http:///xx.xx.xx.xx:80/takeover_order
xx.xx.xx.xx是你的服务器公网IP 地址


你也可以下载文件内的浏览器插件，安装在谷歌或者微软浏览器上，可以方便的操作机器以及方便更多的进单方式


![iShot_2023-04-21_20 09 07](https://user-images.githubusercontent.com/115059056/233632149-634a738c-a74b-44ef-b27a-16b2b9f2e9d6.jpg)
![iShot_2023-04-21_20 09 16](https://user-images.githubusercontent.com/115059056/233632154-a60ea663-a648-4d26-b321-38f4287a3591.jpg)
![iShot_2023-04-21_20 09 23](https://user-images.githubusercontent.com/115059056/233632160-af270958-b0b3-480f-9e30-459381e7614c.jpg)
![iShot_2023-04-21_20 14 06](https://user-images.githubusercontent.com/115059056/233632691-81e53cd0-703a-4d92-9a8a-f29207ef63fd.jpg)
