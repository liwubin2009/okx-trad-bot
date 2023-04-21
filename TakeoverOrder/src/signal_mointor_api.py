# -*- coding: utf-8 -*-

# Author : 'hxc'

# Time: 2023/2/10 12:47 PM

# File_name: 'modify_order_mointor_api.py'

"""
Describe: this is a demo!
"""
from openpyxl import load_workbook
import sys
sys.path.append(".")
from src.signal_mointor import EmaMonitor
file="./configs/user_info.xlsx"
book = load_workbook(file)
sheet = book['Sheet1']
timeframe=sheet["S2"].value
price=sheet["U2"].value
style=sheet["T2"].value
uid=sheet["Q2"].value
ip=sheet["M2"].value
port=sheet["N2"].value
api_key=sheet["B2"].value
secret_key=sheet["C2"].value
passphrase=sheet["D2"].value

f = EmaMonitor()
f.run(Ema_timeframe=timeframe,Price_timeframe=price,style=style,uid=uid,ip=ip,port=port,api_key=api_key,secret_key=secret_key,passphrase=passphrase,start="on")
