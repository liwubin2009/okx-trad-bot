# -*- coding: utf-8 -*-

# Author : 'hxc'

# Time: 2022/11/14 5:13 PM

# File_name: 'child_follow_app.py'
#本程序用于处理信号信息，分发信号指令，如无必要，请勿修改
"""
Describe: this is a demo!
"""
import uvicorn
import logging.config
from os import path
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from src.takeoverOrderManger import SetOrderManger
from flask import Flask,render_template,request
import time
import os
from os import path
from werkzeug.utils import secure_filename
from werkzeug.datastructures import CombinedMultiDict
# from form import UploadForm
from openpyxl import load_workbook
app = Flask(__name__)

class InputDataItem(BaseModel):
    """输入数据对象"""

    symbol:str = ""    #交易对
    action:str = ""   #动作
    side : str = ""   #long short
    price:str = ""
    endprice:str = ""
    positionAmt:str = ""  #仓位大小
    loss_price:str = "" #止损价格
    win_price:str = "" #止盈价格
    lever: int = 1  # 杠杆
    position_mode :str = "" #逐仓还是全仓
    order_type:str = "" #limit or market
    key :str = "" #所属控制key
    uid :str = "" #所属控制key
    maxPx: str = "" #区间最高价
    minPx: str = "" #区间最低价
    gridNum: int = "" #网格数
    basePos: str = "" #区间最低价
    direction: str = "" #区间最低价
    endtime: str = "" #有效时间
    safeoder: str = "" #有效时间
    
    comment = str = ""






# 导入日志配置文件
log_file_path = path.join(path.dirname(path.abspath(__file__)), "configs/logging.conf")
logging.config.fileConfig(log_file_path)
# 创建日志对象
logger = logging.getLogger()
loggerInfo = logging.getLogger("TimeInfoLogger")
Consolelogger = logging.getLogger("ConsoleLogger")
app = FastAPI()

origins = [
    "*"
]
 
app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["GET", "POST"],
    allow_headers = ["*"]
)

to = SetOrderManger()

@app.post("/takeover_order")#接管系统接口
async def take_over_service(res_item:InputDataItem):
    res=""
    """接管订单服务"""
    try:
        res= to.run(req_data=res_item)
    except Exception as e:
        logging.error("app 服务报错，报错信息："+str(e))

        res = "服务报错，请关注管家信息"

    return res
##普通TV 策略接口暂未开放
# @app.post("/tradingview")#普通TV策略接口
# async def tradingview(res_item:InputDataItem):
#     res=""
#     """接管订单服务"""
#     try:
#         res= to.run(req_data=res_item)
#     except Exception as e:
#         logging.error("app 服务报错，报错信息："+str(e))

#         res = "服务报错，请关注管家信息"

#     return res



if __name__ == '__main__':
    uvicorn.run(app="take_over_order_app:app", host="127.0.0.1", port=80, reload=True)