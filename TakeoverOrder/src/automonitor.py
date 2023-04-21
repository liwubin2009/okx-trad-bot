# -*- coding:utf-8 -*-#
#本程序用于监控进程是否正常启用，请勿更改或删除
import subprocess
import os
import datetime
import time
import shutil
class monitor_pid(object):
    def __init__(self):
        print("下单系统初始化成功！！！")
    def copy_rename_file(self):
        path="/root/TakeoverOrder/log/bklog/"
        shutil.rmtree(path)
        if not os.path.exists("/root/TakeoverOrder/log/modify.log"):
            os.mknod("/root/TakeoverOrder/log/modify.log")
        if not os.path.exists("/root/TakeoverOrder/log/chaifen.log"):
            os.mknod("/root/TakeoverOrder/log/chaifen.log")
        if not os.path.exists(path):
            os.makedirs(path)
        modify = os.path.join(path, "modifyback.log")
        chaifen = os.path.join(path, "chaifenback.log")
        shutil.copy("/root/TakeoverOrder/log/modify.log", modify)
        shutil.copy("/root/TakeoverOrder/log/chaifen.log", chaifen)
    def checkprocess(self):
        appname1="modify_order_mointor"
        appname2="take_over_order_app"
        appname3="upload.py"
        appname4="day_restart"
        output = subprocess.getstatusoutput('ps aux')
        p=str(output)
        if not p.count(appname1):
            self.copy_rename_file()
            print("程序停止，重启中……",appname1)
            os.system('source /root/anaconda3/bin/activate takeover_env && cd /root/TakeoverOrder && source /root/TakeoverOrder/modify_order_run.sh start')
        if not p.count(appname2):
            print("程序停止，重启中……",appname2)
            os.system('source /root/anaconda3/bin/activate takeover_env && cd /root/TakeoverOrder &&  source /root/TakeoverOrder/order_run.sh start')
        if not p.count(appname3):
            print("程序停止，重启中……",appname3)
            os.system('source /root/anaconda3/bin/activate takeover_env && cd /root/TakeoverOrder &&  source /root/TakeoverOrder/setting.sh start')
        if not p.count(appname4):
            print("程序停止，重启中……",appname4)
            os.system('source /root/anaconda3/bin/activate takeover_env && cd /root/TakeoverOrder && source /root/TakeoverOrder/autorestart.sh start')
    def onTick(self):
        while 1:
            time.sleep(30)
            self.checkprocess()
if __name__ == "__main__":
    f = monitor_pid()
    f.onTick()
