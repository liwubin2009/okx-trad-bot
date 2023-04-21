# -*- coding: utf-8 -*-

# Author : 'hxc'

# Time: 2023/2/10 12:47 PM

# File_name: 'modify_order_mointor_api.py'
#本程序用于启动接管系统，请勿更改
"""
Describe: this is a demo!
"""
import sys
sys.path.append(".")
from src.modify_order_mointor import ModifyOrderMonitor

f = ModifyOrderMonitor()
f.onTick()
