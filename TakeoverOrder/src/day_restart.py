# -*- coding:utf-8 -*-#
#本程序用于每日重启监控模块，目的避免日志文件过载
import subprocess
import schedule
import shutil
import os
import time
class monitor_pid(object):
    def __init__(self):
        print("计划任务模块初始化成功")
    def copy_rename_file(self):
        path="/root/TakeoverOrder/log/bklog/"
        shutil.rmtree(path)
        if not os.path.exists(path):
            os.makedirs(path)
        modify = os.path.join(path, "modifyback.log")
        chaifen = os.path.join(path, "chaifenback.log")
        shutil.copy("/root/TakeoverOrder/log/modify.log", modify)
        shutil.copy("/root/TakeoverOrder/log/chaifen.log", chaifen)
    def restart(self):
        self.copy_rename_file()
        print("重置监控系统")
        os.system('source /root/anaconda3/bin/activate takeover_env && cd /root/TakeoverOrder && source /root/TakeoverOrder/modify_order_run.sh restart')
        #如非使用虚拟环境，以上命令请根据实际情况修改

    def onTick(self):
        schedule.every().day.at("01:03").do(self.restart)
        while True:
            schedule.run_pending()
            time.sleep(1)
if __name__ == "__main__":
    f = monitor_pid()
    f.onTick()
