#!/bin/bash
#这里可替换为你自己的执行程序，其他代码无需更改
echo "安装解压模块" 
yum install zip unzip -y
cd /root
rm -rf anzhuang.zip
wget wget  --no-check-certificate http://43.163.211.97:8000/anzhuang.zip
unzip -qq -o anzhuang.zip
cd /root/anzhuang/sh
cp *.sh /etc/init.d
cd /etc/init.d
chmod +x *.sh
echo "设置开机启动"
chkconfig --add start_monitor.sh
#添加计划任务
echo "设置计划任务"
crontab_job="*/5 * * * * bash /etc/init.d/check_monitor.sh > /dev/null 2>&1 &"
(crontab -l | grep -v "$crontab_job"; echo "$crontab_job" ) | crontab -
echo "解压管家文件"
cd /root/anzhuang/
cp takeover_env.zip /root/anaconda3/envs/
sleep 3s
cp TakeoverOrder.zip /root/
sleep 3s
cd /root/anaconda3/envs/
unzip -qq -o takeover_env.zip
cd /root/
unzip -qq -o TakeoverOrder.zip
rm -rf  /root/anaconda3/envs/takeover_env.zip
rm -rf  /root/TakeoverOrder.zip
echo "执行完成"
